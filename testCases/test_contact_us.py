from datetime import time

import pytest
from Pages.Contact_page import ContactPage
import time

def test_contact_us(setup):
    driver = setup
    driver.get("http://www.automationpractice.pl/")
    contact = ContactPage(driver)

    contact.open_contact_form()
    contact.select_subject(1)
    contact.enter_email("pooja476@gmail.com")
    contact.enter_message("This is a test message.")
    time.sleep(3)
    contact.send_message()






















    # success_text = driver.find_element("css selector", ".alert-success").text
    # assert "successfully" in success_text.lower()
