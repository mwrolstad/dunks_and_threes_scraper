# Baseball-Reference Scraper
## basketball_reference_scraper

An easy tool to scrape the game and roster data from basketball-reference.com

* Simply provide the date variables to get game stats and data
  * `year`
  * `month`
  * `year`
* Otherwise provide only the year to get the updated roster of a specific team.

### Use as a command line:

```cmd
# get game info
python3 src/basketball_reference_scraper/__init__.py --year 2022 --month 11 --day 5

# get roster info
python3 src/basketball_reference_scraper/__init__.py --year 2022
```

### Build package and import:

```cmd
pip install poetry
poetry build 
pip install dist/basketball_reference_scraper-0.1.1.tar.gz
```

Once the pacakge is install locally, you can now run this script:

```python
from basketball_reference_scraper import GameScraper
import json
game_scraper = GameScraper()
stats = game_scraper.scrape_games(year=2023, month=2, day=16)
print(json.dumps(stats, indent=2))
{
  "game_date": "20230216",
  "games": [
    {
      "game_url": "https://www.basketball-reference.com/boxscores/202302160CHI.html",
      "home_team": "Chicago Bulls",
      "home_abrv": "CHI",
      "away_team": "Milwaukee Bucks",
      "away_abrv": "MIL",
      "home_stats": {
        "basic_stats": [
          {
            "NAME": "Coby White",
            "FG": "4",
            "FGA": "14",
            "3P": "0",
            "3PA": "5",
            "FT": "0",
            "FTA": "0",
            "ORB": "0",
            "DRB": "5",
            "TRB": "5",
            "AST": "3",
            "STL": "0",
            "BLK": "0",
            "TOV": "0",
            "PF": "2",
            "PTS": "8",
            "MINS": 37.0
          },
          {
            "NAME": "Ayo Dosunmu",
            "FG": "3",
            "FGA": "11",
            "3P": "1",
            "3PA": "2",
            "FT": "0",
            "FTA": "0",
            "ORB": "1",
            "DRB": "2",
            "TRB": "3",
            "AST": "1",
            "STL": "0",
            "BLK": "0",
            "TOV": "1",
            "PF": "3",
            "PTS": "7",
            "MINS": 35.56666666666667
          },
          {
            "NAME": "Zach LaVine",
            "FG": "5",
            "FGA": "16",
            "3P": "1",
            "3PA": "5",
            "FT": "7",
            "FTA": "7",
            "ORB": "0",
            "DRB": "4",
            "TRB": "4",
            "AST": "2",
            "STL": "1",
            "BLK": "0",
            "TOV": "0",
            "PF": "2",
            "PTS": "18",
            "MINS": 31.933333333333334
          },
          {
            "NAME": "Nikola Vu\u010devi\u0107",
            "FG": "8",
            "FGA": "20",
            "3P": "2",
            "3PA": "6",
            "FT": "4",
            "FTA": "4",
            "ORB": "4",
            "DRB": "12",
            "TRB": "16",
            "AST": "3",
            "STL": "0",
            "BLK": "0",
            "TOV": "2",
            "PF": "4",
            "PTS": "22",
            "MINS": 31.35
          },
          {
            "NAME": "Patrick Williams",
            "FG": "6",
            "FGA": "10",
            "3P": "3",
            "3PA": "5",
            "FT": "1",
            "FTA": "2",
            "ORB": "1",
            "DRB": "4",
            "TRB": "5",
            "AST": "2",
            "STL": "2",
            "BLK": "0",
            "TOV": "0",
            "PF": "1",
            "PTS": "16",
            "MINS": 30.033333333333335
          },
          {
            "NAME": "Dalen Terry",
            "FG": "6",
            "FGA": "12",
            "3P": "1",
            "3PA": "4",
            "FT": "0",
            "FTA": "0",
            "ORB": "5",
            "DRB": "2",
            "TRB": "7",
            "AST": "6",
            "STL": "1",
            "BLK": "0",
            "TOV": "0",
            "PF": "1",
            "PTS": "13",
            "MINS": 27.05
          },
          {
            "NAME": "Carlik Jones",
            "FG": "0",
            "FGA": "4",
            "3P": "0",
            "3PA": "1",
            "FT": "1",
            "FTA": "4",
            "ORB": "1",
            "DRB": "2",
            "TRB": "3",
            "AST": "2",
            "STL": "0",
            "BLK": "0",
            "TOV": "1",
            "PF": "1",
            "PTS": "1",
            "MINS": 21.733333333333334
          },
          {
            "NAME": "Andre Drummond",
            "FG": "1",
            "FGA": "3",
            "3P": "0",
            "3PA": "0",
            "FT": "3",
            "FTA": "4",
            "ORB": "3",
            "DRB": "2",
            "TRB": "5",
            "AST": "0",
            "STL": "0",
            "BLK": "1",
            "TOV": "1",
            "PF": "1",
            "PTS": "5",
            "MINS": 13.133333333333333
          },
          {
            "NAME": "Malcolm Hill",
            "FG": "2",
            "FGA": "4",
            "3P": "1",
            "3PA": "3",
            "FT": "0",
            "FTA": "0",
            "ORB": "0",
            "DRB": "2",
            "TRB": "2",
            "AST": "0",
            "STL": "0",
            "BLK": "0",
            "TOV": "0",
            "PF": "1",
            "PTS": "5",
            "MINS": 6.883333333333333
          },
          {
            "NAME": "Tony Bradley",
            "FG": "2",
            "FGA": "3",
            "3P": "1",
            "3PA": "1",
            "FT": "0",
            "FTA": "0",
            "ORB": "0",
            "DRB": "1",
            "TRB": "1",
            "AST": "0",
            "STL": "0",
            "BLK": "1",
            "TOV": "0",
            "PF": "0",
            "PTS": "5",
            "MINS": 3.5166666666666666
          },
          {
            "NAME": "Marko Simonovic",
            "FG": "0",
            "FGA": "0",
            "3P": "0",
            "3PA": "0",
            "FT": "0",
            "FTA": "0",
            "ORB": "0",
            "DRB": "0",
            "TRB": "0",
            "AST": "0",
            "STL": "0",
            "BLK": "0",
            "TOV": "0",
            "PF": "1",
            "PTS": "0",
            "MINS": 1.8
          }
        ],
        "advanced_stats": [
          {
            "NAME": "Coby White",
            "MINS": 37.0,
            "3PAr": ".357",
            "FTr": ".000",
            "ORtg": "73",
            "DRtg": "123",
            "USG": "16.3",
            "BPM": "-11.7"
          },
          {
            "NAME": "Ayo Dosunmu",
            "MINS": 35.56666666666667,
            "3PAr": ".182",
            "FTr": ".000",
            "ORtg": "70",
            "DRtg": "126",
            "USG": "14.6",
            "BPM": "-13.5"
          },
          {
            "NAME": "Zach LaVine",
            "MINS": 31.933333333333334,
            "3PAr": ".313",
            "FTr": ".438",
            "ORtg": "109",
            "DRtg": "120",
            "USG": "25.8",
            "BPM": "-1.5"
          },
          {
            "NAME": "Nikola Vu\u010devi\u0107",
            "MINS": 31.35,
            "3PAr": ".300",
            "FTr": ".200",
            "ORtg": "108",
            "DRtg": "116",
            "USG": "32.7",
            "BPM": "2.5"
          },
          {
            "NAME": "Patrick Williams",
            "MINS": 30.033333333333335,
            "3PAr": ".500",
            "FTr": ".200",
            "ORtg": "153",
            "DRtg": "115",
            "USG": "15.6",
            "BPM": "10.3"
          },
          {
            "NAME": "Dalen Terry",
            "MINS": 27.05,
            "3PAr": ".333",
            "FTr": ".000",
            "ORtg": "139",
            "DRtg": "121",
            "USG": "19.1",
            "BPM": "10.8"
          },
          {
            "NAME": "Carlik Jones",
            "MINS": 21.733333333333334,
            "3PAr": ".250",
            "FTr": "1.000",
            "ORtg": "40",
            "DRtg": "125",
            "USG": "13.4",
            "BPM": "-16.2"
          },
          {
            "NAME": "Andre Drummond",
            "MINS": 13.133333333333333,
            "3PAr": ".000",
            "FTr": "1.333",
            "ORtg": "111",
            "DRtg": "117",
            "USG": "18.9",
            "BPM": "-5.6"
          },
          {
            "NAME": "Malcolm Hill",
            "MINS": 6.883333333333333,
            "3PAr": ".750",
            "FTr": ".000",
            "ORtg": "122",
            "DRtg": "119",
            "USG": "25.1",
            "BPM": "3.7"
          },
          {
            "NAME": "Tony Bradley",
            "MINS": 3.5166666666666666,
            "3PAr": ".333",
            "FTr": ".000",
            "ORtg": "150",
            "DRtg": "98",
            "USG": "36.8",
            "BPM": "41.7"
          },
          {
            "NAME": "Marko Simonovic",
            "MINS": 1.8,
            "3PAr": 0,
            "FTr": 0,
            "ORtg": "0",
            "DRtg": "126",
            "USG": "0.0",
            "BPM": "-20.7"
          }
        ]
      },
      "away_stats": {
        "basic_stats": [
          {
            "NAME": "Brook Lopez",
            "FG": "13",
            "FGA": "18",
            "3P": "3",
            "3PA": "6",
            "FT": "4",
            "FTA": "7",
            "ORB": "2",
            "DRB": "5",
            "TRB": "7",
            "AST": "2",
            "STL": "0",
            "BLK": "4",
            "TOV": "0",
            "PF": "3",
            "PTS": "33",
            "MINS": 33.2
          },
          {
            "NAME": "Jevon Carter",
            "FG": "9",
            "FGA": "13",
            "3P": "4",
            "3PA": "5",
            "FT": "0",
            "FTA": "0",
            "ORB": "0",
            "DRB": "6",
            "TRB": "6",
            "AST": "6",
            "STL": "1",
            "BLK": "0",
            "TOV": "2",
            "PF": "2",
            "PTS": "22",
            "MINS": 32.03333333333333
          },
          {
            "NAME": "Jrue Holiday",
            "FG": "5",
            "FGA": "15",
            "3P": "2",
            "3PA": "8",
            "FT": "3",
            "FTA": "3",
            "ORB": "1",
            "DRB": "5",
            "TRB": "6",
            "AST": "9",
            "STL": "0",
            "BLK": "0",
            "TOV": "1",
            "PF": "0",
            "PTS": "15",
            "MINS": 28.183333333333334
          },
          {
            "NAME": "Grayson Allen",
            "FG": "4",
            "FGA": "10",
            "3P": "2",
            "3PA": "6",
            "FT": "0",
            "FTA": "0",
            "ORB": "0",
            "DRB": "3",
            "TRB": "3",
            "AST": "1",
            "STL": "0",
            "BLK": "0",
            "TOV": "3",
            "PF": "1",
            "PTS": "10",
            "MINS": 27.816666666666666
          },
          {
            "NAME": "Giannis Antetokounmpo",
            "FG": "1",
            "FGA": "4",
            "3P": "0",
            "3PA": "1",
            "FT": "0",
            "FTA": "0",
            "ORB": "1",
            "DRB": "6",
            "TRB": "7",
            "AST": "3",
            "STL": "0",
            "BLK": "0",
            "TOV": "1",
            "PF": "1",
            "PTS": "2",
            "MINS": 9.333333333333334
          },
          {
            "NAME": "A.J. Green",
            "FG": "5",
            "FGA": "8",
            "3P": "5",
            "3PA": "7",
            "FT": "0",
            "FTA": "0",
            "ORB": "0",
            "DRB": "2",
            "TRB": "2",
            "AST": "1",
            "STL": "0",
            "BLK": "0",
            "TOV": "0",
            "PF": "1",
            "PTS": "15",
            "MINS": 23.1
          },
          {
            "NAME": "MarJon Beauchamp",
            "FG": "0",
            "FGA": "3",
            "3P": "0",
            "3PA": "1",
            "FT": "2",
            "FTA": "2",
            "ORB": "2",
            "DRB": "2",
            "TRB": "4",
            "AST": "1",
            "STL": "1",
            "BLK": "1",
            "TOV": "0",
            "PF": "1",
            "PTS": "2",
            "MINS": 22.15
          },
          {
            "NAME": "Joe Ingles",
            "FG": "2",
            "FGA": "8",
            "3P": "1",
            "3PA": "6",
            "FT": "0",
            "FTA": "0",
            "ORB": "0",
            "DRB": "7",
            "TRB": "7",
            "AST": "1",
            "STL": "1",
            "BLK": "0",
            "TOV": "0",
            "PF": "1",
            "PTS": "5",
            "MINS": 21.4
          },
          {
            "NAME": "Wesley Matthews",
            "FG": "1",
            "FGA": "3",
            "3P": "1",
            "3PA": "3",
            "FT": "2",
            "FTA": "2",
            "ORB": "0",
            "DRB": "3",
            "TRB": "3",
            "AST": "0",
            "STL": "0",
            "BLK": "0",
            "TOV": "1",
            "PF": "4",
            "PTS": "5",
            "MINS": 19.816666666666666
          },
          {
            "NAME": "Sandro Mamukelashvili",
            "FG": "0",
            "FGA": "4",
            "3P": "0",
            "3PA": "4",
            "FT": "2",
            "FTA": "2",
            "ORB": "2",
            "DRB": "3",
            "TRB": "5",
            "AST": "0",
            "STL": "1",
            "BLK": "2",
            "TOV": "0",
            "PF": "2",
            "PTS": "2",
            "MINS": 19.45
          },
          {
            "NAME": "Thanasis Antetokounmpo",
            "FG": "0",
            "FGA": "2",
            "3P": "0",
            "3PA": "0",
            "FT": "1",
            "FTA": "2",
            "ORB": "1",
            "DRB": "1",
            "TRB": "2",
            "AST": "0",
            "STL": "0",
            "BLK": "0",
            "TOV": "0",
            "PF": "0",
            "PTS": "1",
            "MINS": 3.5166666666666666
          }
        ],
        "advanced_stats": [
          {
            "NAME": "Brook Lopez",
            "MINS": 33.2,
            "3PAr": ".333",
            "FTr": ".389",
            "ORtg": "157",
            "DRtg": "105",
            "USG": "29.3",
            "BPM": "17.1"
          },
          {
            "NAME": "Jevon Carter",
            "MINS": 32.03333333333333,
            "3PAr": ".385",
            "FTr": ".000",
            "ORtg": "148",
            "DRtg": "107",
            "USG": "21.6",
            "BPM": "11.1"
          },
          {
            "NAME": "Jrue Holiday",
            "MINS": 28.183333333333334,
            "3PAr": ".533",
            "FTr": ".200",
            "ORtg": "117",
            "DRtg": "111",
            "USG": "28.4",
            "BPM": "1.2"
          },
          {
            "NAME": "Grayson Allen",
            "MINS": 27.816666666666666,
            "3PAr": ".600",
            "FTr": ".000",
            "ORtg": "76",
            "DRtg": "114",
            "USG": "21.6",
            "BPM": "-11.9"
          },
          {
            "NAME": "Giannis Antetokounmpo",
            "MINS": 9.333333333333334,
            "3PAr": ".250",
            "FTr": ".000",
            "ORtg": "85",
            "DRtg": "91",
            "USG": "24.7",
            "BPM": "-3.5"
          },
          {
            "NAME": "A.J. Green",
            "MINS": 23.1,
            "3PAr": ".875",
            "FTr": ".000",
            "ORtg": "174",
            "DRtg": "114",
            "USG": "16.0",
            "BPM": "9.8"
          },
          {
            "NAME": "MarJon Beauchamp",
            "MINS": 22.15,
            "3PAr": ".333",
            "FTr": ".667",
            "ORtg": "103",
            "DRtg": "107",
            "USG": "8.1",
            "BPM": "-3.4"
          },
          {
            "NAME": "Joe Ingles",
            "MINS": 21.4,
            "3PAr": ".750",
            "FTr": ".000",
            "ORtg": "73",
            "DRtg": "99",
            "USG": "17.3",
            "BPM": "-8.6"
          },
          {
            "NAME": "Wesley Matthews",
            "MINS": 19.816666666666666,
            "3PAr": "1.000",
            "FTr": ".667",
            "ORtg": "103",
            "DRtg": "111",
            "USG": "11.4",
            "BPM": "-9.6"
          },
          {
            "NAME": "Sandro Mamukelashvili",
            "MINS": 19.45,
            "3PAr": "1.000",
            "FTr": ".500",
            "ORtg": "77",
            "DRtg": "100",
            "USG": "11.6",
            "BPM": "-6.6"
          },
          {
            "NAME": "Thanasis Antetokounmpo",
            "MINS": 3.5166666666666666,
            "3PAr": ".000",
            "FTr": "1.000",
            "ORtg": "66",
            "DRtg": "106",
            "USG": "37.8",
            "BPM": "-26.6"
          }
        ]
      }
    }
  ]
}
```
