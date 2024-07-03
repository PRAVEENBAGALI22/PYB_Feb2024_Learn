import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.maximize_window()

# in any additional GUI pops us to close the UI > use the text method to close the UI
close_btn = driver.find_element(By.XPATH, "//button[text()='✕']")
close_btn.click()

search_box = driver.find_element(
    By.XPATH, "//input[@type='text']")
search_box.send_keys("one plus headphones")
time.sleep(2)
# whee there is no proper classname, id use contains
# when we have multiple options listing then use the [1] to list the first item of list of items
first_option = driver.find_element(
    By.XPATH, "(//form[contains(@class,'header-form-search')]//a)[1]")
print(first_option.get_attribute("href"))
print(first_option.text)
first_option.click()

time.sleep(6)
