from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re
import pandas as pd
import os
import time

#launch url
url = "https://turo.com/"

# create a new Chrome session
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-application-cache')
chrome_options.add_argument('media-cache-size=1')
chrome_options.add_argument('disk-cache-size=1')
driver = webdriver.Chrome(chrome_options=chrome_options)
time.sleep(10)
driver.get(url) 

# find the turo search bar and click into it
turo_search = driver.find_element_by_id('js-searchFormExpandedLocationInput')
turo_search.click()

# enter the location and datetime
turo_search.send_keys("dallas")
turo_search.send_keys(Keys.TAB)

start = driver.find_element_by_id('js-searchFormExpandedStartDate')
driver.execute_script("arguments[0].value = '08272018';", start)

# driver.find_element_by_id('js-searchFormExpandedStartTime')

end = driver.find_element_by_id('js-searchFormExpandedEndDate')
driver.execute_script("arguments[0].value = '08312018';", end)

# driver.find_element_by_id('js-searchFormExpandedEndTime')

# search 
turo_search.submit()
time.sleep(5)

#This code will scroll down to the end
while True:
	try:
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		break
	except:
		pass

post_elems = driver.find_elements_by_class_name("vehicleCard")

for link in post_elems:
    print (link.text)