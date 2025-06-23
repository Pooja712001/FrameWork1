import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()
