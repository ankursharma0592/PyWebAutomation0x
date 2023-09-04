import time

import allure
import pytest
from allure_commons.types import AttachmentType
from src.pageObjects.loginPage import LoginPage


@allure.epic("VWO App Positive")
@allure.feature("Login Positive Test")
class TestVWOLogin:

    @pytest.mark.usefixtures("setup")
    def test_vwologinTC1(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(self.username, "123")
        time.sleep(5)
        if "Dashboard" not in driver.title:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScree",
                          attachment_type=AttachmentType.PNG)
        assert "Dashboard" in driver.title
        time.sleep(5)

    @pytest.mark.usefixtures("setup")
    def test_vwologinTC2(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(1223, self.password)
        time.sleep(5)
        if "Dashboard" not in driver.title:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScree",
                          attachment_type=AttachmentType.PNG)
        assert "Dashboard" in driver.title
        time.sleep(5)

    @pytest.mark.usefixtures("setup")
    def test_vwologinTC3(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(self.username, self.password)
        time.sleep(5)
    # assert "Dashboard" in driver.title
    # time.sleep(5)
