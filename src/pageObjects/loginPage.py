# Page Locators
# Page Actions
# Webdriver - Init
# custom Functions
# No Assertion here (They are not Test Cases)
# Page Class

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    #Webdriver - init
    def __init__(self, driver):
        self.driver = driver

    # PageLocators
    username = (By.ID, "login-username")
    password = (By.ID, "login-password")
    submit_button = (By.ID, "js-login-btn")
    error_message = (By.CSS_SELECTOR, "#https://app.vwo.com/#/dashboard")

    # Page Actions
    # Return a Webelement -> username
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    def login_to_vwo(self, username, password):

        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_submit_button().click()
        # get username and send keys - email
        # get password and send keys -  password
        # clik the submit button and navigate to dashboard page

    # def after_login(self, is_Invalid):
    #     if is_Invalid
