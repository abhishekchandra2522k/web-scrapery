from bs4 import BeautifulSoup
import requests

search = input("Search for:")

params = {'q':search}

r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("ol", {"id":"b_results"})

links = results.findAll("li",{"class":"b_algo"})

for items in links:
    item_text = item.find("a").text
    item_href = item.find()