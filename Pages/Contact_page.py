from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ContactPage:
    def __init__(self, driver):
        self.driver = driver

    def open_contact_form(self):
        self.driver.find_element(By.ID, "contact-link").click()

    def select_subject(self, index):
        dropdown = self.driver.find_element(By.ID, "id_contact")
        Select(dropdown).select_by_visible_text("Customer service")

    def enter_email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def enter_message(self, message):
        self.driver.find_element(By.ID, "message").send_keys(message)

    def send_message(self):
        self.driver.find_element(By.ID, "submitMessage").click()








 # Select(dropdown).select_by_index(index)