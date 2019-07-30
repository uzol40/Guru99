from XLutils import xlutils

class Utilities():
    baseUrl = "http://www.demo.guru99.com/v4/"
    chromepath = executable_path = "C:/Users/Ujjwal/PycharmProjects/Guru99/driver/chromedriver.exe"
    Home_Title = "Guru99 Bank Manager HomePage"
    path = "C://Users/Ujjwal/Desktop/Data.xlsx"
    rows = xlutils.getRowCount(path, 'Sheet2')
    Alert = "User or Password is not valid"
