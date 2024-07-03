import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select  # this to be added for selection

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 30)
driver.get("https://www.yatra.com/")
driver.maximize_window()

# org_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
# org_city.click()
# # time.sleep(2)
# org_city.send_keys("New Delhi")
# # time.sleep(2)
# org_city.send_keys(Keys.ENTER)
# # time.sleep(2)
# dest_city = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
# dest_city.click()
# # time.sleep(2)
# dest_city.send_keys("New York")
# # time.sleep(2)
# dest_city.send_keys(Keys.ENTER)
# # time.sleep(2)


first_city = wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
first_city.click()
first_city.send_keys("New Delhi")
first_city.send_keys(Keys.ENTER)

second_city = wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
second_city.click()
second_city.send_keys("New York")
second_city.send_keys(Keys.ENTER)

wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#BE_flight_origin_date"))).click()
# jou_date = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
# jou_date.click()
all_dates = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD "
                                                             "weekend']"))).find_elements(By.XPATH,
                                                                                          "//div["
                                                                                          "@id='monthWrapper']//tbody"
                                                                                          "//td[@class!='inActiveTD "
                                                                                          "weekend']")
# all_dates = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD weekend']")
for date in all_dates:
    if date.get_attribute("data-date") == "04/05/2024":
        date.click()
        time.sleep(4)
        break

driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()

time.sleep(5)