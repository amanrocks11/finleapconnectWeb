from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    logout_btn = (By.XPATH, "//div[@class=\"header-container\"]/p[@class=\"main-button\"]")

    def getLogoutBtn(self):
        return self.driver.find_element(*HomePage.logout_btn)

    def selectEmployee(self, name):
        employee = "//*[@id=\"employee-list\"]/li[contains(text(),'" + name + "')]"
        action_chains = ActionChains(self.driver)
        action_chains.double_click(self.driver.find_element(By.XPATH, employee)).perform()
