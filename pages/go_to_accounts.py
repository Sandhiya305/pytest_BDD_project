import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from resource import locators as locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def read_data_from_file(file_path):
    input_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                input_data[key.strip()] = value.strip()
    return input_data

def check_contact_opp(browser):
    input_data = read_data_from_file("C:/Users/sandhiya.murugav/PycharmProjects/pytestBDDProject2/resource/input_data")
    browser.get("https://agility-flow-7175.lightning.force.com/lightning/o/Account/list?filterName=Recent")
    # Wait for the account page to load
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, locators.locate_account))
    )
    browser.find_element(By.XPATH, locators.locate_account).click()
    time.sleep(3)
    element = browser.find_element(By.XPATH, locators.scroll)
    actions = ActionChains(browser)
    actions.move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(5)
