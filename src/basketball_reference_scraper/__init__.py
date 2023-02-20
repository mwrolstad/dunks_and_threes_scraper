from lxml import html

import argparse
import json
import os
import requests
import pandas as pd

from typing import Dict

BASE_URL = "https://www.basketball-reference.com"
NBA_ABRV = json.load(open(os.path.join(os.path.dirname(__file__), "nba_abbreviations.json")))


def cleanup_dataframes(data_df: pd.DataFrame):
    # clean up the rows we dont need
    data_df = data_df[(data_df.NAME != "Reserves") & (data_df.NAME != "Team Totals") & (data_df.MP != "Not With Team")]

    # replace the DnP and DnD text with 0s
    data_df = data_df.replace("Did Not Play", 0.0)
    data_df = data_df.replace("Did Not Dress", 0.0)
    data_df = data_df.replace("Player Suspended", 0.0)

    # split the MP into two columns
    data_df[["MIN", "SEC"]] = data_df["MP"].str.split(":", expand=True).apply(pd.to_numeric)
    data_df["MINS"] = data_df["MIN"] + data_df["SEC"] / 60

    data_df = data_df.fillna(0)
    return data_df


def select_basic_columns(df: pd.DataFrame):
    cols = [
        "NAME",
        "FG",
        "FGA",
        "3P",
        "3PA",
        "FT",
        "FTA",
        "ORB",
        "DRB",
        "TRB",
        "AST",
        "STL",
        "BLK",
        "TOV",
        "PF",
        "PTS",
        "MINS",
    ]
    return df[cols]


def select_advanced_columns(df: pd.DataFrame):
    cols = [
        "NAME",
        "MINS",
        "3PAr",
        "FTr",
        "ORtg",
        "DRtg",
        "USG",
        "BPM",
    ]
    return df[cols]


def get_columns(df: pd.DataFrame, bsc_adv: str):
    if bsc_adv != "basic" and bsc_adv != "advanced":
        raise Exception("bsc_adv variable is not valid, only accepts basic and advanced")

    bsc_columns = [
        "NAME",
        "MP",
        "FG",
        "FGA",
        "FG%",
        "3P",
        "3PA",
        "3P%",
        "FT",
        "FTA",
        "FT%",
        "ORB",
        "DRB",
        "TRB",
        "AST",
        "STL",
        "BLK",
        "TOV",
        "PF",
        "PTS",
        "PLUS_MINUS",
    ]
    adv_columns = [
        "NAME",
        "MP",
        "TS%",
        "eFG%",
        "3PAr",
        "FTr",
        "ORB%",
        "DRB%",
        "TRB%",
        "AST%",
        "STL%",
        "BLK%",
        "TOV%",
        "USG",
        "ORtg",
        "DRtg",
        "BPM",
    ]

    # renaming the columns
    if bsc_adv == "basic":
        df.columns = bsc_columns
    elif bsc_adv == "advanced":
        if len(df.columns) == 16:
            df = df.assign(BPM=lambda x: None)
        df.columns = adv_columns

    return df


def add_game_date_url(date_df: pd.DataFrame, date_str: str, url_str: str):
    date_df["GAME_DATE"] = date_str
    date_df["URL"] = url_str
    return date_df


def add_team_name(team_df: pd.DataFrame, team_name: str, opp_name: str):
    team_df["TEAM"] = team_name
    team_df["OPPONENT"] = opp_name
    team_df["TEAM_ABRV"] = NBA_ABRV[team_name]
    team_df["OPP_ABRV"] = NBA_ABRV[team_name]
    return team_df


def scrape_rosters(year: str, team_abrv: str = None, proxies: Dict[str, str] = None):
    game_url_template = "https://www.basketball-reference.com/teams/{team_abrv}/{year}.html"

    team_ls = []

    for team_abrv in [team_abrv] if team_abrv else list(set(NBA_ABRV.values())):
        team_dict = {"team_abrv": team_abrv}
        game_url = game_url_template.format(year=year, team_abrv=team_abrv)

        print("Crawling the URL: {url}".format(url=game_url))
        roster_resp = requests.get(url=game_url, proxies=proxies)
        roster_dfs = pd.read_html(roster_resp.text)
        roster_df = roster_dfs[0]
        team_dict["roster"] = roster_df.to_dict(orient="records")

    return team_ls


def scrape_games(year: int, month: int, day: int, proxies: Dict[str, str] = None):
    nba_url = "https://www.basketball-reference.com/boxscores/?month={month}&day={day}&year={year}".format(
        month=str(month).zfill(2), day=str(day).zfill(2), year=str(year)
    )
    resp = requests.get(nba_url, proxies=proxies)
    tree = html.fromstring(resp.text)
    game_urls = tree.xpath('//td[@class="right gamelink"]/a/@href')
    print("Game URLs:\n" + str(game_urls))

    games_dict = {}
    games_dict["game_date"] = "{year}{month}{day}".format(
        year=str(year), month=str(month).zfill(2), day=str(day).zfill(2)
    )
    games_dict["games"] = []

    for url in game_urls:
        try:
            game_url = f"https://www.basketball-reference.com{url}"

            print("Processing URL", game_url)
            resp = requests.get(game_url, proxies=proxies)
            list_dfs = pd.read_html(resp.text)
            game_tree = html.fromstring(resp.text)

            # get the date and derive team names
            away_team = game_tree.xpath('//*[@id="content"]/div[2]/div[1]/div[1]/strong/a/text()')[0]
            home_team = game_tree.xpath('//*[@id="content"]/div[2]/div[2]/div[1]/strong/a/text()')[0]

            print("Processing teams:")
            print(away_team, home_team)

            basic_table = True
            home_away = "away"  # away teams process first

            game_dict = {
                "game_url": game_url,
                "home_team": home_team,
                "home_abrv": NBA_ABRV[home_team],
                "away_team": away_team,
                "away_abrv": NBA_ABRV[away_team],
                "home_stats": {},
                "away_stats": {},
            }

            for l_df in list_dfs:
                if len(l_df.columns) < 15:
                    print("Pass to next dataframe for processing...")
                    continue

                if basic_table is True:
                    l_df = select_basic_columns(cleanup_dataframes(get_columns(l_df, "basic")))
                    game_dict[f"{home_away}_stats"]["basic_stats"] = l_df.to_dict(orient="records")
                    basic_table = False  # process advanced next

                elif len(l_df.columns) in [16, 17]:
                    l_df = select_advanced_columns(cleanup_dataframes(get_columns(l_df, "advanced")))
                    game_dict[f"{home_away}_stats"]["advanced_stats"] = l_df.to_dict(orient="records")
                    basic_table = True  # process basic next
                    home_away = "home"  # process home teams next

            games_dict["games"].append(game_dict)

        except Exception as e:
            print("Exception:", e)
            continue

    return games_dict


class GameScraper:
    def scrape_games(self, year: int, month: int, day: int, proxies: Dict[str, str] = None):
        try:
            return scrape_games(year=year, month=month, day=day, proxies=proxies)
        except Exception as e:
            print(f"An error occurred:\n{e}")
            return

    def scrape_rosters(self, year: int, team_abrv: str = None, proxies: Dict[str, str] = None):
        try:
            return scrape_rosters(year=year, team_abrv=team_abrv, proxies=proxies)
        except Exception as e:
            print(f"An error occurred:\n{e}")
            return


def main(year: int, month: int, day: int):
    g = GameScraper()
    stats = g.scrape_games(year=year, month=month, day=day) if year and month and day else g.scrape_rosters(year=year)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl the baseball-reference game result pages for a specific day.")
    parser.add_argument(
        "--year",
        required=True,
        help="The year number to crawl...",
    )
    parser.add_argument(
        "--month",
        required=False,
        help="The month number to crawl...",
    )
    parser.add_argument(
        "--day",
        required=False,
        help="The day number to crawl...",
    )
    args = parser.parse_args()
    main(args.year, args.month, args.day)
