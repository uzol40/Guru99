from selenium import webdriver
import unittest
import time
import sys
sys.path.append("C:/Users/Ujjwal/PycharmProjects/Guru99")
from pages.loginpage import Loginpage
# from pages.homepage import Logout
from utilities.utilities import Utilities
from XLutils import xlutils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):
    baseUrl = Utilities.baseUrl
    chromepath = Utilities.chromepath
    home_title = Utilities.Home_Title
    driver = webdriver.Chrome(chromepath)
    Alert = Utilities.Alert
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseUrl)
        cls.driver.maximize_window()
        print("Setup done!!!")

    def test_login(self):
        lp = Loginpage(self.driver)
        for r in range(2, Utilities.rows + 1):
            username = xlutils.readData(Utilities.path, "Sheet2", r, 1)
            # print(username)
            password = xlutils.readData(Utilities.path, "Sheet2", r, 2)
            # print(password)
            lp.enter_username(username)
            time.sleep(2)
            lp.enter_password(password)
            time.sleep(2)
            lp.click_login()
            time.sleep(5)
            try:
                text = self.driver.switch_to.alert.text
                if text == self.Alert:
                    print("fail")
                    xlutils.writeData(Utilities.path, "Sheet2", r, 3, "Test Failed")
                    self.driver.switch_to.alert.accept()

            except:
                if self.home_title == self.driver.title:
                    print("login successful!!")
                    xlutils.writeData(Utilities.path, "Sheet2", r, 3, "Test Passed")
                    self.driver.find_element_by_link_text("Log out").click()
                    print("logout successful")
                    self.driver.switch_to.alert.accept()

            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.NAME, Loginpage.username_textbox_name)))

    # def test_logout(self):
    #     lp1=Logout(self.driver)
    #     lp1.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("teardown done!!!")


if __name__ == '__main__':
    unittest.main()