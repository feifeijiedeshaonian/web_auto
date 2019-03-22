from selenium import webdriver
import time
import unittest
from time import sleep
from login__zhixin import LoginZhiXin
from login__zhiyou import LoginZhiYou
from login__zhiyou__guanli import LoginZhiYouGuanLi
from create__company__project import CreateCompanyProject
from approval_company_project import ApprovalCompanyProject


class Creat_Approval(unittest.TestCase):
     
    def test_01(self):
        self.driver = webdriver.Chrome()
        zhixin = LoginZhiXin(self.driver)
        zhiyou = LoginZhiYou(self.driver)
        zhiyou_guanli = LoginZhiYouGuanLi(self.driver)
        zhixin.login_zhixin("13820921009", "1111qqqq")
        sleep(1)
        zhiyou.login_zhiyou()
        sleep(1)
        zhiyou_guanli.login_zhiyou_guanli()
        creat = CreateCompanyProject(self.driver)
        localtime = time.strftime("%m-%d %H:%M", time.localtime())
        project_name = "测试正式项目 "+localtime
        creat.create_company_project(project_name)
        zhixin.login_zhixin("15733189935", "1111qqqq")
        sleep(1)
        zhiyou.login_zhiyou()
        sleep(1)
        zhiyou_guanli.login_zhiyou_guanli()
        approval = ApprovalCompanyProject(self.driver)
        approval.approval_company_project(project_name)


if __name__ == "__main__":
    unittest.main()