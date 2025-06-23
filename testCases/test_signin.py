import pytest
from Pages.Signin_page import SigninPage

def test_sign_in(setup):
    driver = setup
    driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")

    login = SigninPage(driver)
    login.enter_email("mahi.mk476@gmail.com")
    login.enter_password("mahi@12345")
    login.click_sign_in()

    account_name = login.get_account_name()
    print("Logged in as:", account_name)

    # You can assert your expected username here (optional)
    assert account_name != ""

