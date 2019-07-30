from selenium import webdriver
import time
from XLutils import xlutils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import sys
sys.path.append("C:/Users/Ujjwal/PycharmProjects/Guru99")


class LoginTest(unittest.TestCase):
    # global driver
    Home_Title = "Guru99 Bank Manager HomePage"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = "C:/Users/Ujjwal/PycharmProjects/Guru99/driver/chromedriver.exe")
        cls.driver.get("http://www.demo.guru99.com/v4/")
        cls.driver.maximize_window()


    def test_login(self):
        path = "C://Users/Ujjwal/Desktop/Data.xlsx"
        rows = xlutils.getRowCount(path, 'Sheet2')
        for r in range(2, rows+1):

            username = xlutils.readData(path, "Sheet2", r, 1)
            # print(username)
            password = xlutils.readData(path, "Sheet2", r, 2)
            # print(password)
            time.sleep(2)
            self.driver.find_element_by_name("uid").send_keys(username)
            time.sleep(2)
            self.driver.find_element_by_name("password").send_keys(password)
            time.sleep(2)
            self.driver.find_element_by_name("btnLogin").click()
            time.sleep(2)
            try:
                text=self.driver.switch_to.alert.text
                if text=="User or Password is not valid":
                    print("fail")
                    xlutils.writeData(path, "Sheet2", r, 3, "test failed")
                    self.driver.switch_to.alert.accept()

            except:
                 if self.Home_Title == self.driver.title:
                    print("login successful!!")
                    xlutils.writeData(path,"Sheet2",r,3,"test Passed")
                    text=self.driver.find_element_by_class_name("layout").text
                    if username in text:
                        print("Valid manager ID")
                    self.driver.find_element_by_link_text("Log out").click()
                    print("logout successful")
                    self.driver.switch_to.alert.accept()

            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.visibility_of_element_located((By.NAME, "uid")))

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()

