from selenium import webdriver
from time import sleep
import time
from selenium. webdriver. common. by import By
from login__zhixin import LoginZhiXin
from login__zhiyou import LoginZhiYou
from common import Base


class CreateTemporaryProject():

    def __init__(self, driver):
        self.driver = driver

    def create_temporary_project(self):
        # 点击临时项目
        Base.click(self, [By.XPATH, '//*[@id="menu"]/li[2]/span'], self.driver)
        # 点击创建临时项目
        Base.click(self, [By.XPATH, '//*[@id="addNew"]/div/div/div[1]/span'], self.driver)
        sleep(1)
        # 输入项目名称
        localtime = time.strftime("%m-%d %H:%M", time.localtime())
        tem_name = "临时项目 "+localtime
        Base.sendKeys(self, [By.XPATH, '//*[@id="aside-tabs"]/div[3]/div/div[2]/div[1]/ul/li[1]/input'], tem_name, self.driver)
        # 点击美腾科技有限公司
        Base.click(self, [By.XPATH, '//*[@id="aside-tabs"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/ul/div[1]/li/p'], self.driver)
        # 点击智冠信息事业部
        Base.click(self, [By.XPATH, '//*[@id="aside-tabs"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/ul/div[1]/li[2]/p'], self.driver)
        # 点击智能工厂研发部
        sleep(1)
        Base.click(self, [By.XPATH, '//*[@id="aside-tabs"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/ul/div[1]/li[1]/p'], self.driver)
        # 选中测试组
        Base.click(self, [By.XPATH, '//*[@id="aside-tabs"]/div[3]/div/div[2]/div[2]/div[2]/div[1]/ul/div[1]/li[6]/label/span[1]/span'], self.driver)
        sleep(1)
        # 点击确定
        Base.click(self, [By.XPATH, '//*[@id="aside-tabs"]/div[3]/div/div[2]/div[1]/div/button[1]'], self.driver)
        
                
if __name__ == "__main__":
 
    driver = webdriver.Chrome()
    LoginZhiXin(driver).login_zhixin("13820921009", "1111qqqq")
    LoginZhiYou(driver).login_zhiyou()
    CreateTemporaryProject(driver).create_temporary_project()     