import requests
import simplejson as json

url = "https://www.googleapis.com/urlshortener/v1/url"

payload = {'longurl' : "http://example.com"}
headers = {"Content-type" : "application/json"}

r = requests.post(url, json=payload, headers = headers)

print(json.loads(r.text)["error"]['code'])