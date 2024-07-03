# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
#
#
# class BasePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def open(self, url):
#         self.driver.get(url)
#
#     def find_element(self, locator):
#         return self.wait.until(ec.visibility_of_element_located(locator))
