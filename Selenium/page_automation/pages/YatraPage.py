import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class LaunchPage:

    def __init__(self, driver):
        self.driver = driver

    def depart_from(self, departloc):
        org = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        org.click()
        org.send_keys(departloc)
        org.send_keys(Keys.ENTER)

    def dest_to(self, destloc):
        dest = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        dest.click()
        time.sleep(2)
        dest.send_keys(destloc)

        search_lst = self.wait.until(
            ec.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]/li")))

        for result in search_lst:
            if "New York (JFK)" in result.text:
                result.click()
                break

    def journey_date(self, departuredate):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
        all_dates = self.wait.until(ec.element_to_be_clickable(
            (By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTDweekend(']")))
        for date in all_dates:
            if date.get_attribute("data.date") == departuredate:
                date.click()
                time.sleep(5)
                break

        # self.wait.until(ec.element_to_be_clickable((By.XPATH, "//td[@id='29/05/2024']"))).click()
        time.sleep(6)

    def click_search(self):
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@value='Search Flights']"))).click()
