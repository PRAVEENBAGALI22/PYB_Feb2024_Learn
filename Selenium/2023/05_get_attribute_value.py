import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
link1 = driver.find_element(By.XPATH, "//a[@class='blinkingText']")
get_link_text = link1.get_attribute('href')
print(get_link_text)

assert get_link_text == "https://rahulshettyacademy.com/documents-request"
print(f"The text of above link is as expected ",
      get_link_text, "Hence the test case is passed")


time.sleep(3)
