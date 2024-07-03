import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select # this to be added for selection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
dropdwn = driver.find_element(By.NAME,"UserTitle")
dd = Select(dropdwn)
dd.select_by_index(1)
time.sleep(2)
dd.select_by_visible_text("Marketing / PR Manager")
time.sleep(2)
dd.select_by_value("IT_Manager_AP")
time.sleep(2)

