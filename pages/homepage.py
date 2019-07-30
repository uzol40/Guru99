import time
from locators.locators import Locators


class Logout():
    logout_button_link_text = Locators.logout_button_link_text

    def __init__(self, driver):
        self.driver=driver

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_button_link_text).click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()
