import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
check_btns = driver.find_elements(
    By.XPATH, "//input[starts-with(@name,'checkBoxOption')]")
print(len(check_btns))
for check_bt in check_btns:
    check_bt.click()

time.sleep(5)
