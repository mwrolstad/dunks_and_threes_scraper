import argparse
import json
import pandas as pd
import requests
import re

from typing import Dict

JSON_REGEX_EPM = re.compile("stats:(.*),season:")
JSON_REGEX = re.compile("stats:(.*),ks")
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}

def parse_epm(html: str):
    j = re.findall(JSON_REGEX_EPM, html)
    if len(j) > 0:
        json_str = (
            j[0]
            .strip()
            .replace(":", '":')
            .replace(",", ',"')
            .replace("{", '{"')
            .replace( '"{"', '{"')
            .replace(",.", ",0.")
            .replace(",-.", ",-0.")
            .replace(":.", ":0.")
            .replace(":-.", ":-0.")
        )
        json_list = json.loads(json_str)
        json_df = pd.DataFrame(json_list)
        json_df.columns = [
            'season', 'game_dt', 'player_id', 'player_name', 'team_id',
            'team_abrv', 'age', 'inches', 'weight', 'rookie_year', 'position',
            'epm_off', 'epm_def', 'epm_tot', 'idk', 'idk', 'mpg', 'usage',
            'ppg', 'idk', 'efg_%"', 'rim_at', 'mid_at',
            '2p_at', '3p_at', 'ft_at', 'rim_%', 'mid_%',
            '2p_%', '3p_%', 'ft_%', 'ast', 'tov',
            'orb', 'drb', 'stl', 'blk', 'idk', 'idk',
            'idk', 'idk', 'idk', 'idk', 'idk',
            'idk', 'idk', 'idk',
            'idk', 'idk', 'idk', 'idk',
            'idk', 'idk', 'idk', 'idk',
            'idk', 'idk', 'idk', 'idk',
            'idk', 'idk', 'idk', 'idk', 'mpg_z', 'usage_z',
            'ppg_z', 'idk', 'efg_%_z"', 'rim_at_z', 'mid_at_z',
            '2p_at_z', '3p_at_z', 'ft_at_z',
            'rim_%_z', 'mid_%_z', '2p_%_z', '3p_%_z', 'ft_%_z', 'ast_z', 'tov_z',
            'orb_z', 'drb_z', 'stl_z', 
            'blk_z', 'epm_off_z', 'epm_def_z', 'epm_tot_z'
        ]
        json_df.drop("idk", axis=1, inplace=True)
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
    # url_template = "https://dunksandthrees.com/?season={year}"
    url_template = "https://dunksandthrees.com/stats/team?season={year}"

    r = requests.get(url=url_template.format(year=year), headers=HEADERS, proxies=proxies)
    return parse_html(r.text)


def scrape_epm(year: str = None, proxies: Dict[str, str] = None):
    url_template_base = "https://dunksandthrees.com/epm"
    url_template = f"{url_template_base}?season={year}" if year else url_template_base
    print(f"Processing {url_template}")

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
        required=False,
        default=None,
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
