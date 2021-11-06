import requests

print("Hello World")
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)