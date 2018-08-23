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
turo_search.send_keys(Keys.TAB)


start = driver.find_element_by_id('js-searchFormExpandedStartDate')
driver.execute_script("arguments[0].value = '08272018';", start)

driver.find_element_by_id('js-searchFormExpandedStartTime').click()

end = driver.find_element_by_id('js-searchFormExpandedEndDate')
driver.execute_script("arguments[0].value = '08312018';", end)

driver.find_element_by_id('js-searchFormExpandedEndTime').click()


# search 
turo_search.submit()

