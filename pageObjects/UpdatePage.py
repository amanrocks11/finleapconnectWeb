from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class UpdatePage:

    def __init__(self, driver):
        self.driver = driver

    update_btn = (By.XPATH, "//button[@class='main-button']")
    delete_btn = (By.XPATH, "//div[@class=\"formFooter\"]/p[@ng-click=\"deleteEmployee()\"]")

    def getUpdateBtn(self):
        return self.driver.find_element(*UpdatePage.update_btn)

    def getDeleteBtn(self):
        return self.driver.find_element(*UpdatePage.delete_btn)

    def clickDeleteBtn(self):
        self.getDeleteBtn().click()
        try:
            WebDriverWait(self.driver, 3).until(expected_conditions.alert_is_present(),
                                                'Timed out waiting for Deletion confirmation alert')
            self.driver.switch_to.alert.accept()
        except TimeoutException:
            log = self.getLogger()
            log.error('No alert seen')
