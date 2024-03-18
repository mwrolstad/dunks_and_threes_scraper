import argparse
import json
import pandas as pd
import requests
import re

from typing import Dict

JSON_REGEX_EPM = re.compile("stats:(.*),k")
JSON_REGEX = re.compile("stats:(.*),ks")
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}

def parse_epm(html: str):
    j = re.findall(JSON_REGEX_EPM, html)
    if len(j) > 0:
        json_str = (
            j[0]
            .strip()
            .replace("z:", '"z":')
            .replace("pctl:", '"pctl":')
            .replace("rk:", '"rk":')
            .replace(",.", ",0.")
            .replace(",-.", ",-0.")
            .replace(":.", ":0.")
            .replace(":-.", ":-0.")
        )
        json_list = json.loads(json_str)
        json_df = pd.DataFrame(json_list)
        json_df.columns = [
            "year",
            "player_number",
            "idk",
            "idk",
            "id",
            "team_abrv",
            "team",
            "idk",
            "player_name",
            "idk",
            "position",
            "games_played",
            "total_games",
            "gp",
            "idk",
            "idk",
            "games",
            "idk",
            "mpg",
            "mpg_stats",
            "epm_off",
            "epm_def",
            "epm_tot",
            "estimated_wins",
            "epm_off_stats",
            "epm_def_stats",
            "epm_tot_stats",
            "estimated_wins_stats",
            "usage",
            "true_shooting_%",
            "efg_%",
            "rim_%",
            "mid_%",
            "idk",
            "3p_%",
            "ft_%",
            "offensive_rebound_%",
            "defensive_rebound_%",
            "assist_%",
            "turnover_%",
            "steal_%",
            "block_%",
            "usage_stats",
            "true_shooting_stats",
            "efg_stats",
            "rim_stats",
            "mid_stats",
            "idk",
            "3p_stats",
            "ft_stats",
            "offensive_rebound_stats",
            "defensive_rebound_stats",
            "assist_stats",
            "turnover_stats",
            "steal_stats",
            "block_stats",
            "idk",
            "idk",
            "idk",
            "idk",
            "idk",
        ]
        return json_df.to_dict(orient="records")
    else:
        return []


def parse_html(html: str):
    j = re.findall(JSON_REGEX, html)
    if len(j) > 0:
        print("Found the regex match...")
        json_str = (
            j[0]
            .strip()
            .replace("z:", '"z":')
            .replace("pctl:", '"pctl":')
            .replace("rk:", '"rk":')
            .replace(",.", ",0.")
            .replace(",-.", ",-0.")
            .replace(":.", ":0.")
            .replace(":-.", ":-0.")
        )
        print(json_str)
        json_list = json.loads(json_str)
        json_df = pd.DataFrame([json[0:48] for json in json_list])
        json_df.columns = [
            "id",
            "team_abrv",
            "tot_gms",
            "wins",
            "losses",
            "wpct",
            "seed",
            "aortg",
            "adrtg",
            "anet",
            "idk",
            "osos",
            "dsos",
            "sos",
            "ortg",
            "drtg",
            "net",
            "pace",
            "opl",
            "dpl",
            "oefg%",
            "oto%",
            "oor%",
            "ortrt",
            "orim%",
            "omid%",
            "o3p%",
            "oft%",
            "orim",
            "omid",
            "o3pt",
            "oast%",
            "ostl%",
            "oblk%",
            "defg%",
            "dto%",
            "dor%",
            "drtrt",
            "drim%",
            "dmid%",
            "d3p%",
            "dft%",
            "drim",
            "dmid",
            "d3pt",
            "dast%",
            "dstl%",
            "dblk%",
        ]
        return json_df.to_dict(orient="records")
    else:
        return []


def scrape_stats(year: str, proxies: Dict[str, str] = None):
    url_template = "https://dunksandthrees.com/?season={year}"

    r = requests.get(url=url_template.format(year=year), headers=HEADERS, proxies=proxies)
    return parse_html(r.text)


def scrape_epm(year: str, proxies: Dict[str, str] = None):
    url_template = "https://dunksandthrees.com/epm?season={year}"

    r = requests.get(url=url_template.format(year=year), headers=HEADERS, proxies=proxies)
    return parse_epm(r.text)


class StatScraper:
    def scrape_stats(self, year: int, proxies: Dict[str, str] = None):
        try:
            return scrape_stats(year=year, proxies=proxies)
        except Exception as e:
            print(f"An error occurred:\n{e}")
            return

    def scrape_epm(self, year: int, proxies: Dict[str, str] = None):
        try:
            return scrape_epm(year=year, proxies=proxies)
        except Exception as e:
            print(f"An error occurred:\n{e}")
            return


def main(year: int, epm: bool):
    g = StatScraper()
    if epm:
        stats = g.scrape_epm(year=year)
    else:
        stats = g.scrape_stats(year=year)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl dunks and threes website for a specifc year and get data.")
    parser.add_argument(
        "--year",
        required=True,
        help="The year number to crawl...",
    )
    parser.add_argument(
        "--epm",
        required=False,
        action="store_true",
        help="EPM data indicator",
    )
    args = parser.parse_args()
    main(args.year, args.epm)
