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
parent_handle = driver.current_window_handle
print(parent_handle)
driver.find_element(By.XPATH,"//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()
all_handles = driver.window_handles
print(all_handles)
for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        time.sleep(4)
        driver.close()
        time.sleep(4)
        break
driver.switch_to.window(parent_handle)
driver.find_element(By.XPATH,"//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()