import requests
from fake_useragent import UserAgent
from Scrape import Scrape
from bs4 import BeautifulSoup


class ScrapeOverbuff(Scrape):
    def __init__(self, url, name):
        super().__init__(url, name)

    def scrapeUrl(self):
        super().scrapeUrl()

if __name__ == '__main__':
    scrape = ScrapeOverbuff('https://www.overbuff.com/heroes', 'arjay12345#1967')
    print(scrape.name)
    scrape.scrapeUrl()
    print(scrape.page.text)

    ua = UserAgent()

    def lovely_soup(u):
        r = requests.get(u, headers={'User-Agent': ua.chrome})
        print(r.text)
        return BeautifulSoup(r.text, 'lxml')

    url = 'https://www.overbuff.com'
    soup = lovely_soup(url)

    test = soup.find('div', {'class': 'layout-notification'}).text
    print(test.strip())

