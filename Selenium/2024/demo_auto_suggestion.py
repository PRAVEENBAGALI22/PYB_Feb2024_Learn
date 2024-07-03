import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select # this to be added for selection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.yatra.com")
driver.maximize_window()
depart_from = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
depart_from.click()
depart_from.send_keys("New Delhi")
depart_from.send_keys(Keys.ENTER) # use of this is enters the name after sending

time.sleep(3)

going_to = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
going_to.clear()
going_to.send_keys("B")
time.sleep(2)
search_lst = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li ")
for city in search_lst:
    print(city.text)
    if "Bangalore (BLR)" in city.text:
        city.click()
        time.sleep(4)
        break


time.sleep(5)