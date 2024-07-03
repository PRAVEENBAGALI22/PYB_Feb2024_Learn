import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.yatra.com")
driver.maximize_window()
yatra_page_title = driver.title
assert yatra_page_title == "Flight, Cheap Air Tickets , Hotels, Holiday, Trains Package Booking - Yatra.com"

driver.find_element(By.XPATH,"//a[@title='One Way']").click()
driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']").clear()
driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']").send_keys('BLR')
#select_city = driver.find_elements(By.XPATH,"//li[@class='active ac_over']").click()

time.sleep(5)
