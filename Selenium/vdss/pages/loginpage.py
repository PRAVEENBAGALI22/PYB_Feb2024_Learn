# from selenium.webdriver.common.by import By
#
# from Selenium.vdss.pages.basepage import BasePage
#
#
# class LoginPage(BasePage):
#     enter_username = (By.XPATH, "//input[contains(@id,'login')]")
#     enter_password = (By.XPATH, "//input[contains(@id,'password')]")
#     login_btn_clc = (By.XPATH, "//button[contains(text(),'Log In')]")
#
#     def user_name(self, username):
#         # self.find_element(self.enter_username).clear()
#         self.find_element(self.enter_username).send_keys(username)
#
#     def password(self, password):
#         # self.find_element(self.enter_password).clear()
#         self.find_element(self.enter_password).send_keys(password)
#
#     def login_click(self):
#         self.find_element(self.login_btn_clc).click()
