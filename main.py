# Getting data from the internet is called web-scraping

from bs4 import BeautifulSoup
import requests

search = input("Enter search term :")
params = {'q' : search}

r = requests.get("http://bing.com/search",params=params)

soup = BeautifulSoup(r.text)

print(soup.prettify())