import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select # this to be added for selection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# action chains methods  to be used fo
driver.get("https://www.yatra.com")
driver.maximize_window()
morebuttons = driver.find_element(By.XPATH,"//span[@class='more-arr']")
myacc = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
achains = ActionChains(driver) # this method to be used
achains.move_to_element(myacc).perform()
time.sleep(2)
achains.move_to_element(morebuttons).perform()
time.sleep(4)
driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
time.sleep(4)