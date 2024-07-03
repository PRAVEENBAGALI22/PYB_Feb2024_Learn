import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.snapdeal.com/products/mobiles-screen-guards?sort=plrty")
driver.maximize_window()

left1 = driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
right1 = driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]")
ActionChains(driver).drag_and_drop_by_offset(left1,60,0).perform()
ActionChains(driver).
time.sleep(5)

#ActionChains(driver).click_and_hold(left1).pause(1).move_by_offset(50,0).release().perform()
time.sleep(5)

ActionChains(driver).drag_and_drop_by_offset(right1,-60,0).perform()
time.sleep(5)