import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
drop_elemet = driver.find_element(
    By.XPATH, "//select[@id='dropdown-class-example']")
select1 = Select(drop_elemet)
select1.select_by_index(1)
select1.select_by_visible_text("Option2")
select1.select_by_value("option3")


time.sleep(5)
