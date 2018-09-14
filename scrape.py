import requests
import json
import csv
from requests_html import HTMLSession
from pandas.io.json import json_normalize

# new session
s = HTMLSession()

# use search URL to use as referer and get api
s.headers.update({'referer': 'https://turo.com/search?country=US&defaultZoomLevel=11&endDate=09%2F11%2F2018&endTime=10%3A00&international=true&isMapSearch=false&itemsPerPage=200&latitude=32.7766642&location=dallas&locationType=City&longitude=-96.79698789999999&maximumDistanceInMiles=30&region=TX&sortType=RELEVANCE&startDate=09%2F04%2F2018&startTime=10%3A00&type=6'})
r = s.get('https://turo.com/api/search?country=US&defaultZoomLevel=11&endDate=09%2F11%2F2018&endTime=10%3A00&international=true&isMapSearch=false&itemsPerPage=200&latitude=32.7766642&location=dallas&locationType=City&longitude=-96.79698789999999&maximumDistanceInMiles=30&region=TX&sortType=RELEVANCE&startDate=09%2F04%2F2018&startTime=10%3A00&type=6')
#print(r.content)

# jsonify the response and print some json

j = r.json()
#print(j['list'])
#print(json.dumps(j['list'][0]['reviewCount'], indent=2))

# Iterate through the list of entries and export to CSV
i = 0
max = range(150,200)
for i in max:
	car_data = j['list'][i]
	#print(car_data)
	with open('filecars.csv', 'a') as car_csv:  
		w = csv.DictWriter(car_csv, car_data.keys())
		#w.writeheader()
		w.writerow(car_data)
# create the csv writer object
#	with open('file.csv', 'w') as car_csv:  
#		w = csv.DictWriter(car_csv, car_data.keys())
#		w.writeheader()
#		w.writerow(car_data)