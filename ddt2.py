from selenium import webdriver
import ddt
from login__zhixin import LoginZhiXin
import unittest
from read__excel import ExcelUtil


filepath = "C:\\Users\\LENOVO\\Desktop\\python\\13\\testdata.xlsx"
data = ExcelUtil(filepath)
testdates = data.dict_data()
print(testdates)

@ddt.ddt
class Ddt(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data(*testdates)
    def test1(self, data): 
        u'''qqq:4454545'''
        LoginZhiXin(self.driver).login_zhixin(data["name"], data["psw"])

    # def test2(self): 
    #     u'''qqq:4454545'''
    #     data2 = testdates[1]
    #     LoginZhiXin(self.driver).login_zhixin(data2["name"], data2["psw"])

if __name__=="__main__":

    unittest.main()
