import requests
from fake_useragent import UserAgent
from Scrape import Scrape
from bs4 import BeautifulSoup
import urllib.request


class ScrapeOverbuff(Scrape):
    def __init__(self, url, name):
        super().__init__(url, name)

    def scrapeUrl(self):
        my_url = "https://www.overbuff.com/players/pc/Tevetron-1102"
        print(my_url)
        req = urllib.request.Request(my_url, headers={"User-Agent": "Chrome"})
        uClient = urllib.request.urlopen(req)

        #loading content into variable
        page_html = uClient.read()

        #close client
        uClient.close()

        page_soup = BeautifulSoup(page_html, "html.parser")

        #print(page_html)
        print(page_soup)



if __name__ == '__main__':
    scrape = ScrapeOverbuff('https://www.overbuff.com/heroes/', 'arjay12345#1967')
    print(scrape.name)
    scrape.scrapeUrl()
    

