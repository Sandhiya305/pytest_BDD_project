import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from resource import locators as locators

# Function to read data from files and return as a dictionary
def read_data_from_file(file_path):
    input_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                input_data[key.strip()] = value.strip()
    return input_data

def create_account_using_existing_account(browser,locators):
    # Wait for the page to load
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, locators.convert_button_xpath))
    )

    # Create account
    browser.find_element(By.XPATH, locators.convert_button_xpath).click()
    time.sleep(10)
    browser.find_element(By.XPATH, locators.choose_existing_account_xpath).click()
    time.sleep(3)
    browser.find_element(By.XPATH, locators.account_search_box).click()
    time.sleep(3)
    browser.find_element(By.XPATH, locators.choose_existing_account).click()
    time.sleep(3)
    browser.find_element(By.XPATH, locators.choose_convert).click()
    time.sleep(3)
