import requests
from bs4 import BeautifulSoup




def search_wikipedia(search_term):
    try:
        site = requests.get(f"https://en.wikipedia.org/w/index.php?search={search_term}&title=Special:Search&profile=advanced&fulltext=1&ns0=1").text
        soup = BeautifulSoup(site, 'html.parser')

        results = soup.select(selector="#bodyContent .mw-search-result .searchresult")
        if not results:
            return ["No results found"]


        else:
            list_of_results = [result.getText() for result in results]
            print(list_of_results)
            print(list_of_results[0])
            print(list_of_results[1])
            return list_of_results
    except:
        return ["An unexplained error occured"]


