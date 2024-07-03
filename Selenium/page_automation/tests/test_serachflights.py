import time

import pytest

from Selenium.page_automation.pages.YatraPage import LaunchPage


@pytest.mark.usefixtures("setup")
class TestSearchFlights:
    def test_search_flights(self):
        # Launching the browser
        # Provide departure from
        lp = LaunchPage(self.driver,self.wait)
        lp.depart_from("New Delhi")
        # Provide departure TO
        lp.dest_to("New York")
        # Provide departure date
        lp.journey_date("25/05/2024")
        # Click search flights
        lp.click_seach()


tsf = TestSearchFlights()
tsf.test_search_flights()
