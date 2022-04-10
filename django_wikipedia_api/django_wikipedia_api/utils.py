import requests
from bs4 import BeautifulSoup




def search_wikipedia(search_term):
    site = requests.get(f"https://en.wikipedia.org/w/index.php?search={search_term}&title=Special:Search&profile=advanced&fulltext=1&ns0=1").text
    soup = BeautifulSoup(site, 'html.parser')

    results = soup.select(selector="#bodyContent .mw-search-result .searchresult")

    if results:
        print(results[0])

    if not results:
        print("No results found")

search_wikipedia("fdsd")