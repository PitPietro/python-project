import urllib.request
from bs4 import BeautifulSoup


# 3:44 of https://www.udemy.com/course/self-taught-programmer/learn/lecture/11742848#overview
class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            print("\n" + url)


if __name__ == '__main__':
    scrape = Scraper('https://news.google.com')
    scrape.scrape()
