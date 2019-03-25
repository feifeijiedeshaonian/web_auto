import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from create__company__project import CreateCompanyProject
from approval_company_project import ApprovalCompanyProject
from login__zhixin import LoginZhiXin
from login__zhiyou import LoginZhiYou
from login__zhiyou__guanli import LoginZhiYouGuanLi
import time


localtime = time.strftime("%m-%d %H:%M", time.localtime())
project_name = "测试正式项目 "+localtime
# 继承TestCase这个类


class TestMethod(unittest.TestCase):
    '''创建正式项目与审批'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\LENOVO\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")

    def test1(self): 
    
        LoginZhiXin(self.driver).login_zhixin("13820921009", "1111qqqq")

    def test2(self): 
        LoginZhiYou(self.driver).login_zhiyou()
        
    def test3(self):
        LoginZhiYouGuanLi(self.driver).login_zhiyou_guanli()

    def test4(self):
        CreateCompanyProject(self.driver).create_company_project(project_name)

    def test5(self): 
        LoginZhiXin(self.driver).login_zhixin("15733189935", "1111qqqq")

    def test6(self): 
        LoginZhiYou(self.driver).login_zhiyou()
        
    def test7(self):
        LoginZhiYouGuanLi(self.driver).login_zhiyou_guanli()
 
    def test8(self): 
        ApprovalCompanyProject(self.driver).approval_company_project(project_name)


if __name__ == "__main__":

    unittest.main()