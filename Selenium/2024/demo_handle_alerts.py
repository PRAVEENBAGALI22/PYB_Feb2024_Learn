import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select # this to be added for selection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
driver.maximize_window()
driver.switch_to.frame("iframeResult")
""""
#accept the alert
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
time.sleep(4)
driver.switch_to.alert.accept()
time.sleep(3)

#dismiss the alert
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
time.sleep(4)
driver.switch_to.alert.dismiss()
time.sleep(3)
"""
#send some text to the alert
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
time.sleep(4)
print(driver.switch_to.alert.text) # to get the text written in the alert box
driver.switch_to.alert.send_keys("PYB")
driver.switch_to.alert.accept()
time.sleep(3)


