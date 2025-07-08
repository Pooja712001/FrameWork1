
import pytest
from Pages.Signin_page import SigninPage
from my_utilities.read_config import ReadConfig
from my_utilities.logger import custom_logger

log = custom_logger()


def test_sign_in(setup):
    driver = setup
    log.info("Opening Signin page")
    driver.get(ReadConfig.get_base_url())

    Signin = SigninPage(driver)
    log.info("Entering credentials")
    Signin.enter_email(ReadConfig.get_email())
    Signin.enter_password(ReadConfig.get_password())
    Signin.click_sign_in()

    account_name = Signin.get_account_name()
    log.info(f"Logged in as: {account_name}")

    assert account_name == "Mahi kumawat"




