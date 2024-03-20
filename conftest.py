import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get(Config.MAIN_PAGE_STELLAR_BURGERS)
    yield driver
    driver.quit()
