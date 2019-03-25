from selenium import webdriver
import time
from time import sleep
from selenium. webdriver. common. by import By
from common import Base
from login__zhixin import LoginZhiXin
from login__zhiyou import LoginZhiYou
from login__zhiyou__guanli import LoginZhiYouGuanLi
from approval_company_project import ApprovalCompanyProject


class CreateCompanyProject():

    def __init__(self, driver):
        self.driver = driver

    def create_company_project(self, name):
        sleep(1)
        # 点击正式项目管理
        base = Base(self.driver)
        base.click([By.XPATH, "//*[@id='leftBox']/ul/li[2]/ul/li/ul/li[1]"])
        # 点击创建正式项目
        base.click([By.XPATH, "//*[@id='pane-first']/div/div[1]/div/div[1]/button"])
        # 点击创建新的正式项目
        base.click([By.XPATH, ' //*[@id="pane-first"]/div/div[5]/div/div[2]/div/div[1]'])
        # 公司项目命名
        base.sendKeys([By.XPATH, '//*[@id="el_main"]/div/div[1]/div[1]/form/div[1]/div/div/input'], name)
        # 选择立项部门
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[1]/div[1]/form/div[2]/div/div/input'])
        # 选择公司为立项部门
        base.click([By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/ul/div/li/label/span[1]/span'])
        # 点击确定
        base.click([By.XPATH, '/html/body/div[2]/div/div[3]/span/button[2]/span'])
        # 选择日期
        # base.click([By.XPATH, ' //*[@id="el_main"]/div/div[1]/div[1]/form/div[3]/div/div/input[1]'])
        sleep(1)
        base.sendKeys([By.XPATH, ' //*[@id="el_main"]/div/div[1]/div[1]/form/div[3]/div/div/input[1]'], "2019-12-31")
        # base.click([By.XPATH, ' //*[@id="el_main"]/div/div[1]/div[1]/form/div[3]/div/div/input[2]'])
        sleep(1)
        base.sendKeys([By.XPATH, ' //*[@id="el_main"]/div/div[1]/div[1]/form/div[3]/div/div/input[2]'], "2019-12-31")
        # 点击下一步
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[2]/button'])
        # 点击下一步
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[2]/button[2]'])
        # 点击下一步
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[2]/button[2]'])
        # 选择承担部门
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[1]/div[4]/form/div[1]/div/div/input'])
        base.click([By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div/ul/div/li/label/span[1]/span'])
        # 点击确定
        base.click([By.XPATH, '/html/body/div[4]/div/div[3]/span/button[2]'])
        # 添加人员
        sleep(1)
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[1]/div[4]/form/div[3]/div/button'])       
        # 点击天津美腾科技有限公司
        base.click([By.XPATH, '//*[@id="pane-first"]/div/div[2]/div/ul/div[1]/li/p'])
        # 选中综合服务部
        base.click([By.XPATH, '//*[@id="pane-first"]/div/div[2]/div/ul/div[1]/li[4]/label/span[1]/span'])
        # 分担职务
        base.click([By.XPATH, '//*[@id="tab-second"]'])
        # 输入内容
        base.sendKeys([By.XPATH, '//*[@id="pane-second"]/div/div/input'], "测试")
        # 选择时间阶段
        base.click([By.XPATH, '//*[@id="tab-third"]'])
        # 选择长期
        base.click([By.XPATH, '//*[@id="pane-third"]/div/p[2]/label/span[2]'])
        # 点击确定
        base.click([By.XPATH, '/html/body/div[5]/div/div[3]/span/button[2]/span'])
        # 项目参与人数
        base.sendKeys([By.XPATH, '//*[@id="el_main"]/div/div[1]/div[4]/form/div[4]/div/div[1]/input'], "6")      
        # 点击下一步
        sleep(1)
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[2]/button[2]'])
        # 点击下一步
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[2]/button[2]'])
        # 选择审批人
        sleep(1)
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[1]/div[6]/div[2]/div[1]/div/div/img'])     
        # 点击天津美腾科技有限公司
        base.click([By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li/p'])
        # 选择智冠信息事业部
        base.click([By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li[2]/p'])
        # 选择智能工厂研发部
        sleep(1)
        base.click([By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li[1]/p'])
        # 选择测试组
        base.click([By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[1]/li[6]/p'])
        # 选择具体审批人
        sleep(1)
        for num in range(1, 15):
            name1 = self.driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[2]/li[" + str(num) + "]/label/span[2]/span").text
            if name1 == '张凯1':
                self.driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div/ul/div[2]/li[" + str(num) + "]/label/span[2]/span").click()
        # 点击确定
        base.click([By.XPATH, '/html/body/div[6]/div/div[3]/span/button[2]'])
        # 选择抄送人
        sleep(1)
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[1]/div[6]/div[2]/div[2]/div/div/img'])
        # 点击天津美腾科技有限公司
        base.click([By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li/p'])
        # 选择智冠信息事业部
        base.click([By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li[2]/p'])
        # 选择智能工厂研发部
        sleep(1)
        base.click([By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li[1]/p'])
        # 选择测试组
        sleep(1)
        base.click([By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div/ul/div[1]/li[6]/label/span[1]/span'])
        # 点击确定
        base.click([By.XPATH, '/html/body/div[7]/div/div[3]/span/button[2]'])
        # 点击提交
        sleep(1)
        base.click([By.XPATH, '//*[@id="el_main"]/div/div[2]/button[2]'])


if __name__ == "__main__":

    driver = webdriver.Chrome()
    zhixin = LoginZhiXin(driver)
    zhiyou = LoginZhiYou(driver)
    zhiyou_guanli = LoginZhiYouGuanLi(driver)
    zhixin.login_zhixin("13820921009", "1111qqqq")
    sleep(1)
    zhiyou.login_zhiyou()
    sleep(1)
    zhiyou_guanli.login_zhiyou_guanli()
    creat = CreateCompanyProject(driver)
    localtime = time.strftime("%m-%d %H:%M", time.localtime())
    project_name = "测试正式项目 "+localtime
    creat.create_company_project(project_name)
    zhixin.login_zhixin("15733189935", "1111qqqq")
    sleep(1)
    zhiyou.login_zhiyou()
    sleep(1)
    zhiyou_guanli.login_zhiyou_guanli()
    approval = ApprovalCompanyProject(driver)
    approval.approval_company_project(project_name)