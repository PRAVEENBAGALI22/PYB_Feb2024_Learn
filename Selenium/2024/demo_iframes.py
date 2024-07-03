import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select # this to be added for selection

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
driver.maximize_window()
driver.find_element(By.XPATH,"/html[1]/body[1]/iframe[1]").click()