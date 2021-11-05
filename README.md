# fangraph-splits-scraper

WIP for downloading seasonal splits from Fangraphs

Right now, downloads a CSV for Home pitcher splits for Pitchers with > 20 IP"

```
{
  "splitArr":9,
  "splitArrPitch":'',
  "position":"P",
  "autoPt":"false",
  "splitTeams":"false",
  "statType":"player",
  "statgroup":1,
  "startDate":"2021-03-01",
  "endDate":"2021-11-01",
  "players":'',
  "filter":"IP|gt|20",
  "groupBy":"season",
  "sort":"-1,1",
  "pageitems":10000000000000,
  "pg":0,
}
```

# Getting Started

```
$ pipenv install 
$ python3 splits.py
$ pipenv run python3 splits.py
https://www.fangraphs.com/leaders/splits-leaderboards?splitArr=9&splitArrPitch=&position=P&autoPt=false&splitTeams=false&statType=player&statgroup=1&startDate=2021-03-01&endDate=2021-11-01&players=&filter=IP%7Cgt%7C20&groupBy=season&sort=-1%2C1&pageitems=10000000000000&pg=0
$ cat data.csv | sed -e 's/,,/, ,/g' | column -s, -t | tail -n 4
column: line too long
2021    "Drew Rasmussen"        "2 Tms"  18  143  3.81818182   28   4   2   17  14  3   16  2    0    36   0.22047244  0.30769231  0.35433071  0.287293589284234    25385
2021    "Alek Manoah"           "TOR"    9   214  2.31901841   29   5   0   15  14  4   17  0    7    56   0.15343915  0.24766355  0.24338624  0.22723509106680612  26410
2021    "Kwang Hyun Kim"        "STL"    13  224  2.94545455   42   4   0   18  18  4   20  1    2    44   0.21        0.28828829  0.29        0.26003272635904373  27458
2021    "Garrett Crochet"       "CHW"    27  118  1.97560976   21   5   0   10  6   1   16  1    1    31   0.21428571  0.32758621  0.29591837  0.28259429776150247  27463
```