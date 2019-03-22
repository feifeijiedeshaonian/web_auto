from selenium import webdriver
from time import sleep
import unittest
from HTMLTestRunner import HTMLTestRunner


# 继承unittest.TestCase框架
class TestMethod(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        
    def setUp(self):
        self.driver.get("https://www.zentao.net/user-login.html")

    def get_login_username(self):
        # 判断是否登录成功
        try:
            t = self.driver.find_element_by_xpath(".//*[@id='siteNav']/a[5]").text        
            print(t)
            return t
        except:
            return ""

    def test01(self):
       
        self.driver.find_element_by_id("account").send_keys("admin1")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_id("submit").click()
        sleep(3)
        # 判断是否登录成功
        t = self.get_login_username()
        print("获取的结果：" + t)
        self.assertTrue(t == "退出")

    def tearDown(self):
        # 清空登录
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__=="__main__":
  
    # 测试报告的存放路径及文件名
    filename = 'C:/Users/LENOVO/Desktop/zhangkai/testresult.html'
    # 测试报告html文件，此时还是个空文件
    fp = open(filename, 'wb')
    # 调用unittest的TestSuite(),理解为管理case的一个容器（测试套件）
    suite = unittest.TestSuite()
    # 向测试套件中添加用例，"TestMethod"是上面定义的类名，"test01"是用例名 
    suite.addTest(TestMethod('test01'))  
    # runner = unittest.TextTestRunner()   # 执行套件中的用例
    # stream = fp  引用文件流
    # title  测试报告标题
    # description  报告说明与描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下: ')
    # stream = fp  引用文件流
    # title  测试报告标题
    # description  报告说明与描述
    runner.run(suite)   # 执行测试
    fp.close()   # 关闭文件流，将HTML内容写进测试报告文件