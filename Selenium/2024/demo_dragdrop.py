
import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select # this to be added for selection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
e1 = driver.find_element(By.XPATH,"//div[@id='draggable']")
e2 = driver.find_element(By.ID,"droppable")
#ActionChains(driver).drag_and_drop(e1,e2).perform()
time.sleep(3)

ActionChains(driver).drag_and_drop_by_offset(e1,60,80).perform()
time.sleep(3)

