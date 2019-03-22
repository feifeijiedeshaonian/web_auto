from selenium import webdriver
from time import sleep
from selenium. webdriver. common. by import By
from login__zhixin import LoginZhiXin
from login__zhiyou import LoginZhiYou
from common import Base
from login__zhiyou__guanli import LoginZhiYouGuanLi


class CreateCompanyProject():

    def __init__(self, driver):
        self.driver = driver
    
    # name子项目的名称，namea为父项目的名称

    def create_combaby_project(self, name, namea):
        sleep(1)
        # 点击正式项目管理
        Base.click(self, [By.XPATH, "//*[@id='leftBox']/ul/li[2]/ul/li/ul/li[1]"], self.driver)
        # 点击创建正式项目
        Base.click(self, [By.XPATH, "//*[@id='pane-first']/div/div[1]/div/div[1]/button"], self.driver)
        # 点击创建子项目
        Base.click(self, [By.CLASS_NAME, "hasFirm"], self.driver)
        # 输入项目名称
        Base.sendKeys(self, [By.XPATH, '//*[@id="el_main"]/div/form/div[1]/div/div/input'], name, self.driver)
        # 关联父项目
        Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/form/div[2]/div/div/div[1]/input'], self.driver)
        for num in range(1, 8):
            sleep(1)
            name1 = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[" + str(num) + "]/span").text
            if name1 == str(namea):
                driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[" + str(num) + "]/span").click()
                break
        # 添加子项目成员
        for num1 in range(5, 20):
            ele1 = "//*[@id='el_main']/div/form/div[4]/div/div/div/div[" + str(num1) + "]/p"
            abc1 = Base.isElementExist(self, ele1)
            if not abc1:
                driver.find_element_by_xpath("//*[@id='el_main']/div/form/div[4]/div/div/div/div[" + str(num1) + "]/img").click()
                break
        # 选择天津美腾
        sleep(1)
        for num2 in range(1, 18):
            ele2 = "/html/body/div[" + str(num2) + "]/div/div[2]/div/div[2]/div/ul/div[1]/li/p"
            abc2 = Base.isElementExist(self, ele2)
            if abc2:
                driver.find_element_by_xpath("/html/body/div[" + str(num2) + "]/div/div[2]/div/div[2]/div/ul/div[1]/li/p").click()    
                # 选择美腾智冠信息事业部
                sleep(1)
                Base.click(self, [By.XPATH, "/html/body/div[" + str(num2) + "]/div/div[2]/div/div[2]/div/ul/div[1]/li[2]/p"], self.driver)
                # 选择智能工厂研发部
                sleep(1)
                Base.click(self, [By.XPATH, "/html/body/div[" + str(num2) + "]/div/div[2]/div/div[2]/div/ul/div[1]/li[1]/p"], self.driver)
                # 选择web组
                sleep(1)
                Base.click(self, [By.XPATH, "/html/body/div[" + str(num2) + "]/div/div[2]/div/div[2]/div/ul/div[1]/li[2]/label/span[1]/span"], self.driver)              
                # 点击确定
                Base.click(self, [By.XPATH, "/html/body/div[" + str(num2) + "]/div/div[3]/span/button[2]"], self.driver)
                self.driver.get_screenshot_as_file("E:\\screenshot\\renyuan.png")
                # 点击确定
                sleep(1)
                Base.click(self, [By.XPATH, '//*[@id="el_main"]/div/div/div[2]/button[2]'], self.driver)
                self.driver.get_screenshot_as_file("E:\\screenshot\\tijiao.png")


if __name__ == "__main__":

    driver = webdriver.Chrome()
    LoginZhiXin(driver).login_zhixin("15733189935", "2222wwww")
    LoginZhiYou(driver).login_zhiyou()
    LoginZhiYouGuanLi(driver).login_zhiyou_guanli()
    CreateCompanyProject(driver).create_combaby_project("测试公司项目1.4", "测试公司项目1.6") 