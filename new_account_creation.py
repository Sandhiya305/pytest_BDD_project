from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from resource import locators as locators
import time

def read_data_from_file(file_path):
    input_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                input_data[key.strip()] = value.strip()
    return input_data

def create_new_account(browser):
    input_data = read_data_from_file("C:/Users/sandhiya.murugav/PycharmProjects/pytestBDDProject2/resource/input_data")
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, locators.Create_new_account_button))
    )
    browser.find_element(By.XPATH, locators.Create_new_account_button).click()
    time.sleep(2)
    browser.find_element(By.XPATH, locators.create_account_name_xpath).send_keys(input_data['new_account_name'])
    time.sleep(2)
    browser.find_element(By.XPATH, locators.create_account_save_button_xpath).click()
    time.sleep(5)
