import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.go_to_accounts import check_contact_opp, read_data_from_file
from resource import locators as locators
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import given, when, then, scenarios, scenario
from selenium.webdriver.common.alert import Alert
from pages import login_page, new_opportunity_creation
from pages import new_account_creation
from pages import new_contact_creation
from selenium.webdriver.common.action_chains import ActionChains

scenarios('C:/Users/sandhiya.murugav/PycharmProjects/pytestBDDProject2/features/salesforce2.feature')

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


@when('I am able to create new account')
def create_account(browser):
    browser.get("https://agility-flow-7175.lightning.force.com/lightning/o/Account/list?filterName=Recent")
    new_account_creation.create_new_account(browser)

@when('I am create a new contact')
def create_new_contact(browser):
    browser.get("https://agility-flow-7175.lightning.force.com/lightning/o/Contact/list?filterName=Recent")
    new_contact_creation.create_new_contact(browser)

@when('I am create a new opportunity')
def create_new_contact(browser):
    browser.get("https://agility-flow-7175.lightning.force.com/lightning/o/Opportunity/list?filterName=Recent")
    new_opportunity_creation.create_new_opportunity(browser)

@then('I am attaching the contact and opportunity  to new account successfully')
def Validate(browser):
    data = read_data_from_file("C:/Users/sandhiya.murugav/PycharmProjects/pytestBDDProject2/resource/input_data")
    check_contact_opp(browser)
    try:
        time.sleep(2)
        attached_contact_name= browser.find_element(By.XPATH, locators.contact_created)
        attached_opp_name= browser.find_element(By.XPATH, locators.opp_created)
        success_msg1 = attached_contact_name.text
        success_msg2 = attached_opp_name.text
        expected_contact_name = data['success_msg_contact']
        expected_opp_name = data['success_msg_opp']
        print("done: ", success_msg1)
        assert expected_contact_name in success_msg1, f"Expected: '{expected_contact_name}', but got: '{success_msg1}'"
        assert expected_opp_name in success_msg2, f"Expected: '{expected_opp_name}', but got: '{success_msg2}'"

    except Exception as e:
        print(f"Error: {e}")
        raise e
