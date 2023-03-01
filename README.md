# Dunks & Threes Scraper
## dunks_and_threes_scraper

An easy tool to scrape the data from dunksandthrees.com/

* Simply provide the year to scrape
  * `year`
* This will give you the current statistics for the current year, or the year old stats for a previous year.

### Use as a command line:

```cmd
# get stats info
python3 src/dunks_and_threes_scraper/__init__.py --year 2023

# get previous year
python3 src/dunks_and_threes_scraper/__init__.py --year 2019
```

### Build package and import:

```cmd
pip install poetry
poetry build 
pip install dist/dunks_and_threes_scraper-0.1.0.tar.gz
```

Once the pacakge is install locally, you can now run this script:

```python
from dunks_and_threes_scraper import StatsScraper
import json
stats_scraper = StatsScraper()
stats = stats_scraper.scrape_stats(year=2023)
print(json.dumps(stats, indent=2))
[
  {
    "id": 1610612745,           # unique ID
    "team_abrv": "HOU",         # team abbreviation
    "tot_gms": 60,              # total games played
    "wins": 13,                 # wins
    "losses": 47,               # losses
    "wpct": "0.2167",           # win percentage
    "seed": 15,                 # current seed
    "aortg": 109.56,            # adjusted offensive rating
    "adrtg": 118.107,           # adjusted defensive rating
    "anet": -8.54659,           # adjusted net rating
    "idk": -0.5462188720703125,
    "osos": -0.0518111,         # offensive strength of schedule
    "dsos": 0.444039,           # defensive strength of schedule
    "sos": 0.392228,            # net strength of schedule
    "ortg": 109.612,            # offensive rating
    "drtg": 118.551,            # defensive rating
    "net": -8.93882,            # net rating
    "pace": 99.7078,            # possessions per 48 minutes
    "opl": 14.7428,             # offensive posession length in seconds
    "dpl": 11.8122,             # defensive posession length in seconds
    "oefg%": 0.51046,           # offensive effective field goal %
    "oto%": 0.15992,            # offensive turnover %
    "oor%": 0.29876,            # offensive offensive rebound %
    "ortrt": 0.290614,          # offensive free throw rate
    "orim%": 0.594243,          # offensive field goals made at the rim %
    "omid%": 0.394148,          # offensive field goals made from the mid range %
    "o3p%": 0.325126,           # offensive three point make %
    "oft%": 0.754215,           # offensive free throw make %
    "orim": 0.405956,           # offensive field goals taken at the rim %
    "omid": 0.218997,           # offensive field goals taken from the mid range %
    "o3pt": 0.375047,           # offensive field goals taken from three point line %
    "oast%": 0.564361,          # offensive field goals that were assisted
    "ostl%": 0.0719653,         # offensive steal %
    "oblk%": 0.0995228,         # offensive block %
    "defg%": 0.560692,          # defensive effective field goal %          
    "dto%": 0.128903,           # defensive turnover %
    "dor%": 0.240973,           # defensive offensive rebound %
    "drtrt": 0.27699,           # defensive free throw rate
    "drim%": 0.660312,          # defensive field goals made at the rim %
    "dmid%": 0.418953,          # defensive field goals made from the mid range %
    "d3p%": 0.373248,           # defensive three point make %
    "dft%": 0.797952,           # defensive free throw make %
    "drim": 0.327283,           # defensive field goals taken at the rim %
    "dmid": 0.227453,           # defensive field goals taken from the mid range %
    "d3pt": 0.445264,           # defensive field goals taken from three point line %
    "dast%": 0.609264,          # defensive field goals that were assisted
    "dstl%": 0.0894553,         # defensive steal %
    "dblk%": 0.10766            # defensive block %
  },
  {
    "id": 1610612759,
    "team_abrv": "SAS",
    "tot_gms": 61,
    "wins": 14,
    "losses": 47,
    "wpct": "0.2295",
    "seed": 14,
    "aortg": 110.487,
    "adrtg": 120.332,
    "anet": -9.84545,
    "idk": 2.6064529418945312,
    "osos": 0.414662,
    "dsos": 0.0370724,
    "sos": 0.451735,
    "ortg": 110.072,
    "drtg": 120.369,
    "net": -10.2972,
    "pace": 101.362,
    "opl": 13.9685,
    "dpl": 12.0371,
    "oefg%": 0.525259,
    "oto%": 0.147309,
    "oor%": 0.261999,
    "ortrt": 0.230989,
    "orim%": 0.619417,
    "omid%": 0.425211,
    "o3p%": 0.340234,
    "oft%": 0.747295,
    "orim": 0.367726,
    "omid": 0.295966,
    "o3pt": 0.336308,
    "oast%": 0.625858,
    "ostl%": 0.0679518,
    "oblk%": 0.0662196,
    "defg%": 0.578341,
    "dto%": 0.129478,
    "dor%": 0.255878,
    "drtrt": 0.263798,
    "drim%": 0.642016,
    "dmid%": 0.463599,
    "d3p%": 0.396579,
    "dft%": 0.772195,
    "drim": 0.385439,
    "dmid": 0.264343,
    "d3pt": 0.350218,
    "dast%": 0.578309,
    "dstl%": 0.0814458,
    "dblk%": 0.0828402
  }
]
```
