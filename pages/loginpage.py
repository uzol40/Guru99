from locators.locators import Locators


class Loginpage():
    username_textbox_name = Locators.username_textbox_name
    password_textbox_name = Locators.password_textbox_name
    login_button_name = Locators.login_button_name
    find_text_classname = Locators.find_text_classname

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_name(self.login_button_name).click()

    def find_text(self):
        self.driver.find_element_by_class_name(self.find_text_classname).text()



