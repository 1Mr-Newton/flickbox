from bs4 import BeautifulSoup
import requests
import json
import time


class Movie:
    def __init__(self):
        self.baseURL = "https://ww2.fmovies.cab"
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Thunder Client (https://www.thunderclient.com)",
            "x-requested-with": "XMLHttpRequest",
        }

    def _sendRequest(self, reqUrl):
        response = requests.get(reqUrl, headers=self.headers)
        return response.json()

    def searchMovie(self, movieName):
        reqUrl = f"{self.baseURL}/search/{movieName}"
        return self._sendRequest(reqUrl)

    def searchSuggestions(self, movieName):
        reqUrl = f"{self.baseURL}/ajax_search/{movieName}"
        return self._sendRequest(reqUrl)

    def parseMovieSearch(self, html):
        soup = BeautifulSoup(html, "html.parser")
        search_items = soup.find_all("a", class_="search-point")
        results = []
        for item in search_items:
            _title = item.get("title")
            description = _title.split(":")[-1].strip()
            title = "".join(_title.split(":")[:-1]).strip()
            link = self.baseURL + item.get("href")

            img = item.find("img").get("data-loaderdata")
            img = json.loads(img)
            img = img["src"]
            if title and link:

                results.append(
                    {
                        "title": title,
                        "link": link,
                        "description": description,
                        "cover": img if "http" in img else self.baseURL + img,
                    }
                )
        return results


movie = Movie()
res = movie.searchMovie("after")["html"]

print(json.dumps(movie.parseMovieSearch(res), indent=4))
# with open("test.html", "w", encoding="utf-8") as f:
#     f.write()
