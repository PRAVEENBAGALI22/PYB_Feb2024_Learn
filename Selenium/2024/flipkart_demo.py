import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//span[contains(text(),'Mobiles')]").click()

ac = ActionChains(driver)
ele = driver.find_element(By.XPATH, "//span[normalize-space()='Electronics']")
ac.move_to_element(ele).click().perform()
ap = driver.find_element(By.XPATH, "//a[normalize-space()='Apple']")
ac.move_to_element(ap).click().perform()

time.sleep(5)