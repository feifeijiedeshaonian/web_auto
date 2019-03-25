import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from create__company__project2 import CreateCompanyProject
from approval_company_project import ApprovalCompanyProject
from login__zhixin import LoginZhiXin
from login__zhiyou import LoginZhiYou
from login__zhiyou__guanli import LoginZhiYouGuanLi
import time


localtime = time.strftime("%m-%d %H:%M", time.localtime())
project_name = "测试正式项目 "+localtime
# # 继承TestCase这个类
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

    # 测试报告的存放路径及文件名
    filename = 'C:/Users/LENOVO/Desktop/zhangkai/testresult.html'
    # 测试报告html文件，此时还是个空文件
    fp = open(filename, 'wb')
    # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）
    suite = unittest.TestSuite()
    # 向测试套件中添加用例，"TestMethod"是上面定义的类名，"test01"是用例名 
    suite.addTest(TestMethod('test1'))  
    suite.addTest(TestMethod('test2'))
    suite.addTest(TestMethod('test3'))
    # runner = unittest.TextTestRunner()   # 执行套件中的用例
    # stream = fp  引用文件流
    # title  测试报告标题
    # description  报告说明与描述
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试结果如下: ')
    # stream = fp  引用文件流
    # title  测试报告标题
    # description  报告说明与描述
    runner.run(suite)   # 执行测试
    fp.close()   # 关闭文件流，将HTML内容写进测试报告文件