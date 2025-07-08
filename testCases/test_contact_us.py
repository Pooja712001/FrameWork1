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











import pytest
from Pages.Contact_page import ContactPage
from my_utilities.logger import custom_logger

log = custom_logger()


def test_contact_us(setup):
    driver = setup
    log.info("Opening contact us page")
    driver.get("http://www.automationpractice.pl/index.php?controller=contact")

    contact = ContactPage(driver)
    contact.select_subject(1)
    contact.enter_email("mahi.mk476@gmail.com")
    contact.enter_message("This is a test message.")
    contact.send_message()
    log.info("Message sent successfully")











