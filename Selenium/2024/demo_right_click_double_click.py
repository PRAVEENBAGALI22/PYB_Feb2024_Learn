import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select # this to be added for selection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# action chains methods  to be used fo
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
# write click on the web element
# achains = ActionChains(driver)
# elem1 = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
# achains.context_click(elem1).perform()
# time.sleep(3)
# driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
# time.sleep(3)

# double-click on the web element
achains = ActionChains(driver)
elem2 = driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
achains.double_click(elem2).perform()
time.sleep(3)
alert_txt = driver.switch_to.alert.text
print(alert_txt)
driver.switch_to.alert.accept()

time.sleep(3)