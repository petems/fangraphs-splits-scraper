import urllib

import pickle
from bs4 import BeautifulSoup as bs
from selenium import webdriver

HOME_PITCHER_SPLITS = {
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


HEADERS = {
    'origin': "https://github.com/petems/fangraphs-splits-scraper",
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "https://github.com/petems/fangraphs-splits-scraper",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6",
    'cache-control': "no-cache"
}

PATH_COOKIE = "/tmp/"

def save_cookie(driver):
    pickle.dump(driver.get_cookies(), open(PATH_COOKIE + "cookies.pkl", "wb"))

def create_driver():
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--host-resolver-rules=MAP www.google-analytics.com 127.0.0.1")
    option.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
    return webdriver.Chrome(options=option)

def selenium_download_file(url):
    driver = create_driver()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)

    driver.get(url)
    html = driver.page_source

    soup = bs(html, "html.parser")
    results = soup.find_all('a', attrs={"class":"data-export"})

    _, encoded = results[0]["href"].split(",", 1)

    data = urllib.parse.unquote(encoded)

    with open("data.csv", "w") as fp:
      fp.write(data)

    print("Saved to data.csv!")


def build_url(base_url, path, args_dict):
  url_parts = list(urllib.parse.urlparse(base_url))
  url_parts[2] = path
  url_parts[4] = urllib.parse.urlencode(args_dict)
  return urllib.parse.urlunparse(url_parts)

def pitch_split_url_maker(start_date="2021-03-01",end_date="2021-11-01"):

  fangraphs_split_url = "https://www.fangraphs.com/leaders/splits-leaderboards"

  custom_url = fangraphs_split_url.format(start_date=start_date, end_date=end_date)

  print("URL IS: " + custom_url)

  return custom_url

new_url = build_url("https://www.fangraphs.com", "leaders/splits-leaderboards", HOME_PITCHER_SPLITS)

print(new_url)

selenium_download_file(new_url)