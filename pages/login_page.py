import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def login_to_salesforce(browser, username, password):
    browser.get("https://login.salesforce.com")
    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "Login").click()
