import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

session = HTMLSession()

r = requests.get('https://turo.com/search?country=US&defaultZoomLevel=11&endDate=09%2F05%2F2018&endTime=10%3A00&international=true&isMapSearch=false&itemsPerPage=200&latitude=32.7766642&location=Dallas&locationType=City&longitude=-96.79698789999999&maximumDistanceInMiles=30&region=TX&sortType=RELEVANCE&startDate=08%2F29%2F2018&startTime=10%3A00')
c = r.content
#print(c)

soup = BeautifulSoup(c, 'lxml')

for link in soup.select('a[href*="/rentals/"]'):
	print(link.get('href'))

