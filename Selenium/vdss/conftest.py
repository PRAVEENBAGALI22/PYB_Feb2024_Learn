import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import ec
from webdriver_manager.chrome import ChromeDriverManager

# from Selenium.vdss.config import BASEURL
# from Selenium.vdss.pages.loginpage import LoginPage
import pytest


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)
    driver.get("https://vdss-kube-pv.esi-group.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()

# @pytest.fixture(scope="session")
# def chrome_options():
#     options = Options()
#     # options.add_argument("--headless")  # Run tests in headless mode
#     # options.add_argument("--disable-gpu")
#     options.add_argument("--window-size=1920,1080")
#     return options
#
#
# @pytest.fixture(scope="session")
# def driver(chrome_options):
#     driver = webdriver.Chrome(options=chrome_options)
#     yield
#     driver.close()
#
#
# @pytest.fixture(scope="function")
# def login_page(driver):
#     login_page = LoginPage(driver)
#     login_page.open(BASEURL)
#     return login_page
