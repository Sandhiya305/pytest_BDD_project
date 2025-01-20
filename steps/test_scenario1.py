import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.lead_creation import read_data_from_file
from resource import locators as locators
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import given, when, then, scenarios
from selenium.webdriver.common.alert import Alert
from pages import login_page
from pages import lead_creation
from pages import lead_to_account_conversion

scenarios('../features/salesforce.feature')

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(3)
    yield driver
    driver.quit()

@given('I am logged in to salesforce')
def login_salesforce(browser):
    login_page.login_to_salesforce(browser, 'sandhiya.murugav-jchq@force.com', 'Sand@305A')


@when('I am create a lead')
def lead_create(browser):
    lead_creation.create_lead(browser)


@then('I am converting the lead to account using create new account successfully')
def check_lead(browser):
    data = read_data_from_file("C:/Users/sandhiya.murugav/PycharmProjects/pytestBDDProject2/resource/input_data")
    #locators = read_locators_from_file("resource/locators.txt")
    lead_to_account_conversion.create_account(browser, locators)
    try:
        time.sleep(2)
        converted = browser.find_element(By.XPATH, locators.convert_msg_xpath)
        success_msg = converted.text
        expected_message = data['lead_convert_success_msg']
        print("done: ", success_msg)
        assert success_msg == expected_message, f"Expected: '{expected_message}', but got: '{success_msg}'"

    except Exception as e:
        print(f"Error: {e}")
        raise e

