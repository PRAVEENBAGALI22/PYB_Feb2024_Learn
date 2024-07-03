import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
conti_demo = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
conti_demo.screenshot(".\\test.png")
conti_demo.click()
time.sleep(3)
conti_demo.screenshot(".\\test1.png")