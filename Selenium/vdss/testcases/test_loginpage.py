import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import ec
from Selenium.vdss.conftest import setup


# from Selenium.vdss.pages.loginpage import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_page(self):
        # username_input = driver.find_element(By.XPATH, "//input[@id='_58_login']")
        # username_input = self.driver.find_element(By.XPATH, "//input[contains(@id,'login')]")
        username_input = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[contains(@id,'login')]")))
        username_input.clear()
        username_input.send_keys("pyb@esi-group.com")
        # # password_input = driver.find_element(By.XPATH, "//input[@id='_58_password']")
        # password_input = self.driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        # password_input.clear()
        # password_input.send_keys('pyb@pvk8')
        # # login_btn_clc = driver.find_element(By.XPATH,"//button[contains(@id,'_58_')]")# this button is dynamic in
        # # nature so using
        # login_btn_clc = self.driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]")
        # login_btn_clc.click()
        print("Logged In Successfully")
        # admore_app = self.driver.find_element(By.XPATH, "//div[contains(text(),'ADMORE')]")
        # admore_app.click()
        #
        # ####################################################################################
        # # delete_project= driver.find_element(By.XPATH,"//div[@class='cardAction']//div//a[@class='col-xs-4 ng-isolate-scope']")
        # # ach = ActionChains(driver)
        # # ach.context_click(delete_project).perform()
        # ####################################################################################
        #
        # # time.sleep(10)
        #
        # # sadd_project = driver.find_element(By.XPATH, "//i[@class='addIconBtn vdss-icons vdss-add-btn-icon']")
        # add_project = self.driver.find_element(By.XPATH, "//span[contains(text(),'Add Project')]")
        #
        # add_project.click()
        #
        # # projectname = driver.find_element(By.XPATH, "//input[contains(@id,'project_name')]")
        # projectname = self.driver.find_element(By.XPATH, "//input[@id='project_name']")
        # projectname.send_keys("PYB")
        #
        # # project_description = driver.find_element(By.XPATH, "//textarea[@id='description']")
        # project_description = self.driver.find_element(By.XPATH, "//textarea[contains(@id,'description')]")
        # project_description.send_keys("This is sample project")
        #
        # time.sleep(2)
        #
        # # add_project = driver.find_element(By.XPATH, "//button[contains(text(),'Add ')]")
        # add_project = self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
        # add_project.click()
        # print("Project successfully added")
        # time.sleep(15)
        #
        # # add_study = driver.find_element(By.XPATH, "//span[@class='addStudyBtn']")
        # add_study = self.driver.find_element(By.XPATH, "//span[contains(text(),'Add Study')]")
        # add_study.click()
        #
        # # study_name = driver.find_element(By.XPATH, "//input[@id='study_name']")
        # study_name = self.driver.find_element(By.XPATH, "//input[contains(@id,'study_name')]")
        # study_name.send_keys("NEW STUDY")
        #
        # # study_description = driver.find_element(By.XPATH, "//textarea[@id='description']")
        # study_description = self.driver.find_element(By.XPATH, "//textarea[contains(@id,'description')]")
        # study_description.send_keys("SAMPLE STUDY ")
        #
        # time.sleep(2)
        #
        # # add_study_click = driver.find_element(By.XPATH, "//button[@id='myBtn']")
        # add_study_click = self.driver.find_element(By.XPATH, "//button[contains(@id,'myBtn')]")
        # add_study_click.click()
        #
        # time.sleep(10)
        #
        # dashboard = self.driver.find_element(By.XPATH, "//a[normalize-space()='Dashboard']")
        # dashboard.click()
        #
        # proj_to_delete = self.driver.find_element(By.XPATH, "//i[@title='Delete']")
        # proj_to_delete.click()
        # time.sleep(10)
        #
        # confirm_pro_delete = self.driver.find_element(By.XPATH, "//span[contains(text(),'Delete')]")
        # confirm_pro_delete.click()
        # print("Project successfully deleted")
        # time.sleep(10)
        #
        # self.driver.find_element(By.XPATH, "//span[@class='user-full-name']").click()
        # self.driver.find_element(By.XPATH, "//span[normalize-space()='Sign Out']").click()


c1 = TestLogin()
c1.test_login_page()
