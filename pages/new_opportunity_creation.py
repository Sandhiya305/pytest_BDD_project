from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from resource import locators as locators
import time
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

def create_new_opportunity(browser):
    input_data = read_data_from_file("C:/Users/sandhiya.murugav/PycharmProjects/pytestBDDProject2/resource/input_data")
    # Wait for the opportunity page to load
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.XPATH, locators.Create_new_opportunity_button))
    )
    browser.find_element(By.XPATH, locators.Create_new_opportunity_button).click()
    time.sleep(2)
    browser.find_element(By.XPATH, locators.opportunity_name).send_keys(
        input_data['new_opportunity_name'])
    time.sleep(2)
    browser.find_element(By.XPATH, locators.Search_account_name_xpath).send_keys(input_data['new_account_name'])
    time.sleep(2)
    browser.find_element(By.XPATH, locators.dropdown_account_name_xpath1).click()
    time.sleep(2)
    browser.find_element(By.XPATH, locators.Closing_date_xpath).send_keys(input_data['opportunity_closing_date'])
    time.sleep(2)
    element = browser.find_element(By.XPATH, locators.scroll_xpath)
    actions = ActionChains(browser)
    actions.move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(2)
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, locators.stage_xpath))
    )
    browser.find_element(By.XPATH, locators.stage_xpath).click()
    time.sleep(5)
    browser.find_element(By.XPATH, locators.select_stage).click()
    time.sleep(3)
    browser.find_element(By.XPATH, locators.create_opportunity_save_button_xpath).click()
    time.sleep(1)
