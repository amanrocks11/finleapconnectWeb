from selenium.webdriver.common.by import By
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username_field = (By.XPATH, "//*[@ng-model='user.name']")
    password_field = (By.XPATH, "//*[@ng-model='user.password']")
    login_btn = (By.XPATH, "//button[@class='main-button']")
    error_message = (By.XPATH, "//p[@class='error-message ng-binding']")
    login_message = (By.ID, 'greetings')

    def getUsernameField(self):
        return self.driver.find_element(*LoginPage.username_field)

    def getPasswordField(self):
        return self.driver.find_element(*LoginPage.password_field)

    def getLoginBtn(self):
        return self.driver.find_element(*LoginPage.login_btn)

    def getErrorMsg(self):
        return self.driver.find_element(*LoginPage.error_message)

    def getLoginMessage(self):
        return self.driver.find_element(*LoginPage.login_message)

    def setUsernameField(self, user):
        self.getUsernameField().clear()
        self.getUsernameField().send_keys(user)

    def setPasswordField(self, pwd):
        self.getPasswordField().clear()
        self.getPasswordField().send_keys(pwd)

    def login(self, username, password):
        self.setUsernameField(username)
        self.setPasswordField(password)
        self.getLoginBtn().click()
        time.sleep(2)

