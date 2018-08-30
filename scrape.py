import requests
import json
from requests_html import HTMLSession
from pandas.io.json import json_normalize

# new session
s = HTMLSession()

# use search URL to use as referer and get api
s.headers.update({'referer': 'https://turo.com/search?country=US&defaultZoomLevel=11&endDate=09%2F05%2F2018&endTime=10%3A00&international=true&isMapSearch=false&itemsPerPage=200&latitude=32.7766642&location=Dallas&locationType=City&longitude=-96.79698789999999&maximumDistanceInMiles=30&region=TX&sortType=RELEVANCE&startDate=08%2F30%2F2018&startTime=10%3A00'})
r = s.get('https://turo.com/api/search?country=US&defaultZoomLevel=11&endDate=09%2F05%2F2018&endTime=10%3A00&international=true&isMapSearch=false&itemsPerPage=200&latitude=32.7766642&location=Dallas&locationType=City&longitude=-96.79698789999999&maximumDistanceInMiles=30&region=TX&sortType=RELEVANCE&startDate=08%2F30%2F2018&startTime=10%3A00')

# jsonify the response and print some json
j = r.json()
#print(j['list'][0])
print(json.dumps(r['list'][0]['reviewCount'], indent=2))
