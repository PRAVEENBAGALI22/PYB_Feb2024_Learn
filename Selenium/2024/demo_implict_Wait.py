import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select # this to be added for selection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10) # this will checked for all web elements

driver.get("https://login.salesforce.com/?locale=in")
driver.maximize_window()
driver.find_element(By.ID,"username").clear()
driver.find_element(By.ID,"username").send_keys("pyb")
driver.find_element(By.ID,"password").clear()
driver.find_element(By.ID,"password").send_keys("pyb")