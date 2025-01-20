import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from resource import locators as locators

def read_data_from_file(file_path):
    input_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                input_data[key.strip()] = value.strip()
    return input_data


def create_lead(browser):

    input_data = read_data_from_file("C:/Users/sandhiya.murugav/PycharmProjects/pytestBDDProject2/resource/input_data")
    # Wait for the lead page to load
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, locators.lead_name_xpath))
    )
    # Create lead
    browser.find_element(By.XPATH, locators.lead_name_xpath).click()
    time.sleep(2)
    browser.find_element(By.XPATH, locators.lead_first_name_xpath).send_keys(input_data['lead_first_name'])
    time.sleep(2)
    browser.find_element(By.XPATH, locators.lead_last_name_xpath).send_keys(input_data['lead_last_name'])
    time.sleep(1)
    browser.find_element(By.XPATH, locators.lead_company_xpath).send_keys(input_data['lead_company'])
    browser.find_element(By.XPATH, locators.lead_save_button_xpath).click()
    time.sleep(1)
