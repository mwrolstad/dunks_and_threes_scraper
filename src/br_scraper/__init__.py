from lxml import html

import argparse
import json
import os
import re
import requests
import pandas as pd

BASE_URL = "https://www.baseball-reference.com"
MLB_ABRV = json.load(open(os.path.join(os.path.dirname(__file__), "mlb_abbreviations.json")))

def convert_date_to_number(dt, override_year=None):
    try:
        yr = re.search("(20|19)[0-9]{2}", dt, re.IGNORECASE)
        yr = str(dt.datetime.today().year) if yr is None else yr.group(0)

        mt = re.search(
            "(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)",
            dt,
            re.IGNORECASE,
        ).group(0)
        mt = month_string_to_number(mt)

        if override_year is not None:
            yr = str(override_year - 1 if int(mt.replace("0", "")) < 8 else override_year)

        dy = re.search("[0-9]{1,2}", dt, re.IGNORECASE).group(0).zfill(2)

        return f"{yr}{mt}{dy}"

    except:
        return ""


def month_string_to_number(string):
    m = {
        "jan": "01",
        "feb": "02",
        "mar": "03",
        "apr": "04",
        "may": "05",
        "jun": "06",
        "jul": "07",
        "aug": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dec": "12",
    }

    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError("Not a month")


def scrape_previews():
    url = "{base_url}/previews".format(base_url=BASE_URL)
    response = requests.get(url)

    tree = html.fromstring(response.content)
    games_count = len(tree.xpath('//*[@class="game_summary nohover"]'))

    ls_games = []

    for g in range(1, games_count + 1):

        game_dict = {}

        away_team_link = tree.xpath(f'//*[@id="content"]/div[1]/div[{g}]/table/tbody/tr[1]/td[1]/a')
        home_team_link = tree.xpath(f'//*[@id="content"]/div[1]/div[{g}]/table/tbody/tr[2]/td[1]/a')
        game_url_ls = tree.xpath(f'//*[@id="content"]/div[1]/div[{g}]/table/tbody/tr[1]/td[3]/a')

        if len(away_team_link) > 0 and len(home_team_link) > 0 and len(game_url_ls) > 0:

            game_dict["game_url"] = f"https://www.baseball-reference.com{game_url_ls[0].attrib['href']}"
            print("Crawling the URL:", game_dict["game_url"])

            game_response = requests.get(game_dict["game_url"])
            game_tree = html.fromstring(game_response.content)

            game_date = game_tree.xpath('//*[@id="content"]/h1/text()')

            if len(game_date) > 0:

                game_dict["away_team"] = away_team_link[0].text
                game_dict["home_team"] = home_team_link[0].text
                game_dict["away_abrv"] = MLB_ABRV[game_dict["away_team"]]
                game_dict["home_abrv"] = MLB_ABRV[game_dict["home_team"]]

                game_date_num = convert_date_to_number(game_date[0])
                teams = [game_dict["away_abrv"], game_dict["home_abrv"]]
                print("The date we're working with is...", game_date_num)

                for i in range(0, 2):

                    game_dict["team"] = teams[i]
                    stats_df = requests.get(game_dict["game_url"])

                    game_dict["home_away"] = 1 if game_dict["team"] == game_dict["home_abrv"] else 0
                    game_dict["record"] = stats_df[i][1][1]
                    game_dict["game_num"] = stats_df[i][1][3]
                    game_dict["last_10"] = stats_df[i][1][10]
                    game_dict["last_20"] = stats_df[i][1][11]
                    game_dict["last_30"] = stats_df[i][1][12]
                    game_dict["home_rec"] = stats_df[i][1][13]
                    game_dict["away_rec"] = stats_df[i][1][14]
                    game_dict["extras_rec"] = stats_df[i][1][15]
                    game_dict["vs_RHP"] = stats_df[i][1][16]
                    game_dict["vs_LHP"] = stats_df[i][1][17]
                    game_dict["onerun_rec"] = stats_df[i][1][18]
                    game_dict["vs_east"] = stats_df[i][1][19]
                    game_dict["vs_central"] = stats_df[i][1][20]
                    game_dict["vs_west"] = stats_df[i][1][21]
                    game_dict["vs_interleague"] = stats_df[i][1][22]

                    if teams[i] == "WSH":
                        pitch_abrv = "WSN"
                    elif teams[i] == "TB":
                        pitch_abrv = "TBR"
                    elif teams[i] == "KC":
                        pitch_abrv = "KCR"
                    elif teams[i] == "SF":
                        pitch_abrv = "SFG"
                    elif teams[i] == "SD":
                        pitch_abrv = "SDP"
                    else:
                        pitch_abrv = teams[i]

                    pitcher_table = game_tree.xpath(f'//*[@id="sp_{pitch_abrv}_sh"]/h2/a')
                    game_dict["pitcher"] = pitcher_table[0].text if len(pitcher_table) > 0 else None

                    ls_games.append(game_dict)

    return ls_games


def scrape_games(year: int, month: int, day: int):

    url = "{base_url}/boxes/?year={year}&month={month}&day={day}".format(
        base_url=BASE_URL,
        year=year,
        month=month,
        day=day,
    )
    print("Crawling the url: {url}".format(url=url))
    response = requests.get(url)

    game_date_num = "{year}{month}{day}".format(
        year=year,
        month=month,
        day=day,
    )
    # print("response.content", response.content)
    tree = html.fromstring(response.content)
    games_count = len(tree.xpath('//*[@class="game_summary nohover "]'))

    games_ls = []

    if games_count > 0:

        for game in range(1, games_count + 1): 
            game_num = str(game)

            away_team_link = tree.xpath(
                '//*[@id="content"]/div[3]/div[{game_num}]/table[1]/tbody/tr[1]/td[1]/a'.format(game_num=game_num)
            )
            home_team_link = tree.xpath(
                '//*[@id="content"]/div[3]/div[{game_num}]/table[1]/tbody/tr[2]/td[1]/a'.format(game_num=game_num)
            )
            game_url_ls = tree.xpath(
                '//*[@id="content"]/div[3]/div[{game_num}]/table[1]/tbody/tr[1]/td[3]/a'.format(game_num=game_num)
            )

            if len(away_team_link) == 0:
                away_team_link = tree.xpath(
                    '//*[@id="content"]/div[3]/div[{game_num}]/table[1]/tbody/tr[2]/td[1]/a'.format(game_num=game_num)
                )
            if len(home_team_link) == 0:
                home_team_link = tree.xpath(
                    '//*[@id="content"]/div[3]/div[{game_num}]/table[1]/tbody/tr[3]/td[1]/a'.format(game_num=game_num)
                )
            if len(game_url_ls) == 0:
                game_url_ls = tree.xpath(
                    '//*[@id="content"]/div[3]/div[{game_num}]/table[1]/tbody/tr[2]/td[3]/a'.format(game_num=game_num)
                )

            if len(away_team_link) > 0 and len(home_team_link) > 0 and len(game_url_ls) > 0:

                game_dict = {
                    "game_date": game_date_num,
                    "game_url": BASE_URL + game_url_ls[0].attrib["href"],
                    "away_team": away_team_link[0].text,
                    "home_team": home_team_link[0].text,
                    "away_abrv": MLB_ABRV[game_dict["away_team"]],
                    "home_abrv": MLB_ABRV[game_dict["home_team"]],
                    "pitcher_stats": [],
                    "hitter_stats": [],
                }
                print("About to gather the game data")

                game_dict["away_team"] = away_team_link[0].text
                game_dict["home_team"] = home_team_link[0].text
                game_dict["away_abrv"] = MLB_ABRV[game_dict["away_team"]]
                game_dict["home_abrv"] = MLB_ABRV[game_dict["home_team"]]

                game_response = requests.get(game_dict["game_url"])

                teams = [game_dict["away_abrv"], game_dict["home_abrv"], game_dict["away_abrv"], game_dict["home_abrv"]]

                hitters_tables = re.findall(
                    f'(<table class="sortable stats_table min_width shade_zero")(.*?)(<\/table>)',
                    game_response.text,
                    re.DOTALL | re.MULTILINE,
                )

                for i in range(0, 4):

                    stats_df = pd.read_html(f"<html>{hitters_tables[i]}</html>")[0]

                    team = teams[i]

                    if i == 0 or i == 2:
                        home_away = "away"
                    else:
                        home_away = "home"

                    stats_df["team"] = team
                    stats_df["game_url"] = game_dict["game_url"]
                    stats_df["home_away"] = home_away
                    stats_df["game_date"] = game_dict["game_date"]

                    if i <= 1:
                        stats_df["WPA-"] = stats_df["WPA-"].str.replace("%", "").astype(float).round(decimals=3)
                        stats_df["cWPA"] = stats_df["cWPA"].str.replace("%", "").astype(float).round(decimals=3)
                        stats_df = stats_df[stats_df["Batting"] != "Team Totals"]
                        stats_df = stats_df[stats_df["AB"].notna()]
                        stats_df["Batting"] = (
                            stats_df["Batting"].str.split(" ", n=0, expand=True)[0]
                            + " "
                            + stats_df["Batting"].str.split(" ", n=0, expand=True)[1]
                        )
                        game_dict["hitter_stats"] = game_dict["hitter_stats"] + stats_df.to_dict(orient="records")
                    else:
                        stats_df = stats_df[stats_df["Pitching"] != "Team Totals"]
                        stats_df["Pitching"] = stats_df["Pitching"].str.split(",", n=0, expand=True)[0]
                        stats_df["WPA"] = stats_df["WPA"].round(decimals=3)
                        stats_df["aLI"] = stats_df["aLI"].round(decimals=3)
                        stats_df["RE24"] = stats_df["RE24"].round(decimals=3)
                        stats_df["cWPA"] = stats_df["cWPA"].str.replace("%", "").astype(float).round(decimals=3)
                        game_dict["pitcher_stats"] = game_dict["pitcher_stats"] + stats_df.to_dict(orient="records")

                games_ls.append(game_dict)
            
    return games_ls


class GameScraper:
    def scrape_day(self, year: int, month: int, day: int):
        try:
            return scrape_games(year=year, month=month, day=day)
        except Exception as e:
            print(f"An error occurred:\n{e}")
            return
    def scrape_preview(self):
        try:
            return scrape_previews()
        except Exception as e:
            print(f"An error occurred:\n{e}")
            return


def main(year: int, month: int, day: int):
    g = GameScraper()
    stats = g.scrape_day(year=year, month=month, day=day) if year and month and day else g.scrape_preview()
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Crawl the baseball-reference game result pages for a specific day."
    )
    parser.add_argument(
        "--year",
        required=False,
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
