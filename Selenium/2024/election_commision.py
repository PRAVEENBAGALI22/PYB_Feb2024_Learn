
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select # this to be added for selection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://voters.eci.gov.in")
print(driver.title)
driver.maximize_window()

wait = WebDriverWait(driver,10)
#wait.until(ec.element_to_be_clickable((By.XPATH,"//p[normalize-space()='Know your Polling Station & Officer']")))
driver.find_element(By.XPATH,"//p[normalize-space()='Know your Polling Station & Officer']").click()

