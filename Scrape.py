import requests
from bs4 import BeautifulSoup

class Scrape():
    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.page = ''

    def scrapeUrl(self):
        self.page = requests.get(self.url)
