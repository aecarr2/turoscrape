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
# moved chromewebdriver to C:\Windows folder - PATH env var was incorrect ?
driver = webdriver.Chrome()
time.sleep(5)
driver.get(url) 

# find the turo search bar and click into it
turo_search = driver.find_element_by_id('js-searchFormExpandedLocationInput')
turo_search.click()

# enter the location and datetime
turo_search.send_keys("dallas")
time.sleep(5)
turo_search.send_keys(Keys.TAB)

time.sleep(10)

start = driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(25) > div > section.days > div.day.col-1-7.selected.boundary-from')
start.click()

driver.find_element_by_id('js-searchFormExpandedStartTime').click()

driver.find_element_by_id('js-searchFormExpandedEndDate').click()

driver.find_element_by_id('js-searchFormExpandedEndTime').click()


# search 
turo_search.submit()

