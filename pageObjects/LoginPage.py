from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
    loginBtn=(By.XPATH, "//*[@class='links']//*[text()='Login']")
    def clickLoginBtn(self):
        self.driver.find_element(*LoginPage.loginBtn)