import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.youtube.com/@RaghavsValueInvesting/videos")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@value = 'radio2']").click()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Praveen")
driver.find_element(By.XPATH, "//input[@id='name']").clear()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("PYB")

# this is example of 2 selectors which can be selected
# driver.find_element(By.XPATH, "//input[@type='submit' and @id='alertbtn']").click()

alert_eg = driver.find_element(
    By.XPATH, "//legend[text()='Switch To Alert Example']")
alert_eg_text = alert_eg.text
print(alert_eg_text)
driver.find_element(By.XPATH, "//input[@id='name']").clear()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys(alert_eg_text)


time.sleep(3)
