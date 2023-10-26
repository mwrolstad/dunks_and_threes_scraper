import argparse
import json
import pandas as pd
import requests
import re
import ast

from typing import Dict

# JSON_REGEX = re.compile("const data = (.*);")
JSON_REGEX = re.compile("stats:(.*),ks:")


def parse_html(html: str):
    j = re.findall(JSON_REGEX, html)
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
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}

    r = requests.get(url=url_template.format(year=year), headers=headers, proxies=proxies)
    return parse_html(r.text)


class StatScraper:
    def scrape_stats(self, year: int, proxies: Dict[str, str] = None):
        try:
            return scrape_stats(year=year, proxies=proxies)
        except Exception as e:
            print(f"An error occurred:\n{e}")
            return


def main(year: int):
    g = StatScraper()
    stats = g.scrape_stats(year=year)
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crawl dunks and threes website for a specifc year and get data.")
    parser.add_argument(
        "--year",
        required=True,
        help="The year number to crawl...",
    )
    args = parser.parse_args()
    main(args.year)
