import requests
from requests_oauthlib import OAuth1
import configparser
import json
import random

BASE_URL_TWITTER = "https://api.twitter.com/1.1/tweets/search/30day/dev.json"
BASE_URL_MAPBOX = "https://api.mapbox.com/geocoding/v5/mapbox.places/"

config = configparser.ConfigParser()
config.read("config.ini")

auth = OAuth1(
	config["TwitterAPI"]['API_KEY'],
	config["TwitterAPI"]['API_SECRET_KEY'],
	config["TwitterAPI"]['ACCESS_TOKEN'],
	config["TwitterAPI"]['ACCESS_TOKEN_SECRET']
)

def get_coords(loc):
	rr = requests.get(BASE_URL_MAPBOX + loc + ".json?access_token=" + config['mapboxAPI']['API_KEY'] + "&cachebuster=1549145420259&autocomplete=true")
	location = json.loads(rr.text)
	try:
		if 'bbox' in location['features'][0]:
			arr = location['features'][0]['bbox']
			x = random.uniform(arr[0], arr[2])
			y = random.uniform(arr[1], arr[3])
		elif 'center' in location['features'][0]:
			arr = location['features'][0]['center']
			x = arr[0]
			y = arr[1]
		return [x, y]
	except:
		return None
r = requests.get(BASE_URL_TWITTER + "?query=feeling", auth=auth)
print(r)
result = json.loads(r.text)
for t in result['results']:
	#print(t)
	loc = t['user']['location']
	if loc == None or loc == "Global":
		continue
	if 'extended_tweet' in t:
		text = t['extended_tweet']['full_text']
	else:
		text = t['text']
	coords = get_coords(loc)
	if coords == None:
		continue
	print(text, coords)
	