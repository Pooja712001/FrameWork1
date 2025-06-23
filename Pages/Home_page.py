from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_search_item(self, item):
        self.driver.find_element(By.ID, "search_query_top").send_keys(item)

    def click_search(self):
        self.driver.find_element(By.NAME, "submit_search").click()
