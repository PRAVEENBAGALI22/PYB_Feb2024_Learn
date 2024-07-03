import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.youtube.com/@RaghavsValueInvesting/videos")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID, "checkBoxOption1").click()
driver.find_element(By.NAME, "checkBoxOption2").click()
driver.find_element(By.CSS_SELECTOR, "[value='radio2']").click()
time.sleep(5)
