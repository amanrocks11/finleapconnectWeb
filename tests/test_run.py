from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest
import time
from TestData.CreatePageData import CreatePageData
from pageObjects.CreatePage import CreatePage
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from pageObjects.UpdatePage import UpdatePage
from utilities.BaseClass import BaseClass

login_completion = False


class TestHomePage(BaseClass):

    def test_invalid_login(self):
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        log.info("Trying Login using invalid credentials")
        login_page.login("Luke", "test")
        error_text = login_page.getErrorMsg().text
        assert ("Invalid username or password!" in error_text)

    def test_valid_login(self):
        global login_completion
        log = self.getLogger()
        login_page = LoginPage(self.driver)
        log.info("Trying Login using valid credentials")
        login_page.login("Luke", "Skywalker")
        welcome_text = login_page.getLoginMessage().text
        assert ("Luke" in welcome_text), "Login failed, correct greeting message not seen"
        login_completion = True

    def test_create_invalid_employee(self, getInvalidData):
        log = self.getLogger()
        create_page = CreatePage(self.driver)
        log.info("Trying to create invalid employee")
        global login_completion
        if not login_completion:
            login_page = LoginPage(self.driver)
            login_page.login("Luke", "Skywalker")
        create_page.getCreateBtn().click()
        time.sleep(2)
        create_page.setData(getInvalidData)
        create_page.getAddBtn().click()
        time.sleep(2)
        assert (create_page.getAddBtn().is_displayed()), "Creation successful with invalid data"
        self.driver.refresh()
        time.sleep(2)

    def test_create_valid_employee(self, getValidData):
        log = self.getLogger()
        create_page = CreatePage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.login("Luke", "Skywalker")
        log.info("Trying to create a valid employee")
        # Add code to check if the login was successful
        create_page.getCreateBtn().click()
        time.sleep(2)
        create_page.setData(getValidData)
        create_page.getAddBtn().click()
        time.sleep(2)
        assert (create_page.getCreateBtn().is_displayed()), "Creation not successful, invalid data"

    def test_update_employee(self, getUpdateData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        create_page = CreatePage(self.driver)
        update_page = UpdatePage(self.driver)
        # Add code to check if the create employee was successful
        home_page.selectEmployee(getUpdateData['firstname'])
        time.sleep(1)
        create_page.setData(getUpdateData)
        update_page.getUpdateBtn().click()
        time.sleep(2)
        assert (create_page.getCreateBtn().is_displayed()), "Update not successful, invalid data"

    def test_delete_employee(self, getUpdateData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        create_page = CreatePage(self.driver)
        update_page = UpdatePage(self.driver)
        # Add code to check if the create employee was successful
        home_page.selectEmployee(getUpdateData['firstname'])
        time.sleep(1)
        update_page.clickDeleteBtn()
        time.sleep(1)
        assert (create_page.getCreateBtn().is_displayed()), "Delete not successful"

    def test_logout(self):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        home_page.getLogoutBtn().click()
        time.sleep(1)
        assert (login_page.getLoginBtn().is_displayed()), "Logout not successful"

    @pytest.fixture(params=CreatePageData.getTestData("invalid"))
    def getInvalidData(self, request):
        return request.param

    @pytest.fixture(params=CreatePageData.getTestData("valid"))
    def getValidData(self, request):
        return request.param

    @pytest.fixture(params=CreatePageData.getTestData("valid"))
    def getUpdateData(self, request):
        return request.param
