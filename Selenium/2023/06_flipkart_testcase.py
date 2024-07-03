import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.flipkart.com/")
deals = driver.find_elements(By.XPATH, "//div[@data-clone='false']//a")
print(len(deals))
for deal in deals:
    print(deal.get_attribute("href"))
    print(deal.get_attribute("innerHTML"))
    print(deal.get_attribute("outerrHTML"))

    break

time.sleep(3)
