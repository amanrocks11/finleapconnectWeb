from selenium.webdriver.common.by import By


class CreatePage:

    def __init__(self, driver):
        self.driver = driver

    create_btn = (By.ID, "bAdd")
    cancel_btn = (By.XPATH, "//button[@class='subButton bCancel']")
    first_name_field = (By.XPATH, "//form[@name=\"employeeForm\"]//input[@ng-model=\"selectedEmployee.firstName\"]")
    last_name_field = (By.XPATH, "//form[@name=\"employeeForm\"]//input[@ng-model=\"selectedEmployee.lastName\"]")
    start_date_field = (By.XPATH, "//form[@name=\"employeeForm\"]//input[@ng-model=\"selectedEmployee.startDate\"]")
    email_field = (By.XPATH, "//form[@name=\"employeeForm\"]//input[@ng-model=\"selectedEmployee.email\"]")
    add_btn = cancel_btn = (By.XPATH, "//button[@class='main-button']")

    def getCreateBtn(self):
        return self.driver.find_element(*CreatePage.create_btn)

    def getCancelBtn(self):
        return self.driver.find_element(*CreatePage.cancel_btn)

    def getFirstNameField(self):
        return self.driver.find_element(*CreatePage.first_name_field)

    def getLastNameField(self):
        return self.driver.find_element(*CreatePage.last_name_field)

    def getStartDateField(self):
        return self.driver.find_element(*CreatePage.start_date_field)

    def getEmailField(self):
        return self.driver.find_element(*CreatePage.email_field)

    def getAddBtn(self):
        return self.driver.find_element(*CreatePage.add_btn)

    def setData(self, data):
        self.getFirstNameField().clear()
        self.getFirstNameField().send_keys(data['firstname'])
        self.getLastNameField().clear()
        if data['lastname'] is not None:
            self.getLastNameField().send_keys(data['lastname'])
        self.getStartDateField().clear()
        self.getStartDateField().send_keys(data['sdate'].date().strftime("%Y-%m-%d"))
        self.getEmailField().clear()
        self.getEmailField().send_keys(data['email'])
