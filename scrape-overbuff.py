import requests
from Scrape import Scrape

class ScrapeOverbuff(Scrape):
    def __init__(self, url, name):
        super().__init__(url, name)

if __name__ == '__main__':
    scrape = ScrapeOverbuff('url_here', 'DaddyDerek')
    print(scrape.name)

