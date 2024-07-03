import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# driver.find_element(By.XPATH, "//input[@value='radio1']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@value='radio2']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@value='radio3']").click()
# time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='checkBoxOption1']").click()
time.sleep(4)

drdn = driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")
dd = Select(drdn)
#dd.select_by_index(1)
#dd.select_by_visible_text('option2')
dd.select_by_value('option3')
time.sleep(2)


