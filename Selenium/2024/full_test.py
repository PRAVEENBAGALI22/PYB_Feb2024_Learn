import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)
driver.get("https://www.yatra.com/")
driver.maximize_window()
org = wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
org.click()
org.send_keys("New Delhi")
org.send_keys(Keys.ENTER)

dest = wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
dest.click()
time.sleep(2)
dest.send_keys("New")

search_lst = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))

for result in search_lst:
    if "New York (JFK)" in result.text:
        result.click()
        break

wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()

# all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")
# for date in all_dates:
#     if date.get_attribute("data.date") == "26/05/2024":
#         date.click()
#         time.sleep(5)
#         break


wait.until(ec.element_to_be_clickable((By.XPATH, "//td[@id='29/05/2024']"))).click()
time.sleep(6)

wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@value='Search Flights']"))).click()
time.sleep(10)

driver.find_element(By.XPATH, "//section[@id='Flight-APP']//label[2]").click()
time.sleep(5)
