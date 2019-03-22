from selenium import webdriver
from login__zhixin import LoginZhiXin
import unittest

testdates = [{"name": "13820921009", "psw": "1111qqqq"},{"name": "15733189935", "psw": "1111qqqq"}]


class Ddt(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test1(self): 
        u'''qqq:4454545'''
        data1 = testdates[0]
        LoginZhiXin(self.driver).login_zhixin(data1["name"], data1["psw"])

    def test2(self): 
        u'''qqq:4454545'''
        data2 = testdates[1]
        LoginZhiXin(self.driver).login_zhixin(data2["name"], data2["psw"])

if __name__=="__main__":

    unittest.main()
