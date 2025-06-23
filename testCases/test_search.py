import time

import pytest
from Pages.Home_page import HomePage

def test_search(setup):
    driver = setup
    driver.get("http://www.automationpractice.pl/")
    homepage = HomePage(driver)

    homepage.enter_search_item("dress")
    time.sleep(3)
    homepage.click_search()
    time.sleep(3)

    assert "search_query=dress" in driver.current_url
