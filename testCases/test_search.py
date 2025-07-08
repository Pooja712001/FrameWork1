import pytest
from Pages.Home_page import HomePage
from my_utilities.logger import custom_logger

log = custom_logger()


def test_search(setup):
    driver = setup
    log.info("Opening homepage")
    driver.get("http://www.automationpractice.pl/index.php")

    search = HomePage(driver)
    search.enter_search_item("dress")
    search.click_search()
    log.info("Search completed")