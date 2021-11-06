import urllib.request

from bs4 import BeautifulSoup

my_url = "https://www.overbuff.com/players/pc/Tevetron-1102"
req = urllib.request.Request(my_url, headers={"User-Agent": "Chrome"})

#opening connection and grabbing page
uClient = urllib.request.urlopen(req)

#loading content into variable
page_html = uClient.read()

#close client
uClient.close()

page_soup = BeautifulSoup(page_html, "html.parser")

#print(page_html)
print(page_soup)