from selenium.webdriver.common.by import By

class SigninPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.ID, "email").send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "passwd").send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(By.ID, "SubmitLogin").click()

    def get_account_name(self):
        return self.driver.find_element(By.CLASS_NAME, "account").text
