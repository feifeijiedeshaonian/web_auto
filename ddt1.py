from selenium import webdriver
import ddt
from login__zhixin import LoginZhiXin
import unittest
# 数据驱动


testdates = [{"name": "13820921009", "psw": "1111qqqq"},{"name": "15733189935", "psw": "1111qqqq"}]

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
