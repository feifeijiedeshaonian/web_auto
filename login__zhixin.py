from selenium import webdriver
from common import Base
from time import sleep
from selenium. webdriver. common. by import By


class LoginZhiXin():

    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()
        
    def login_zhixin(self, user="17694804822", psw="rsl123456"):
        # 输入网址
        self.driver.get("http://192.168.5.54/")
        sleep(1)
        # 输入账号密码
        loc1 = (By.XPATH, '//*[@id="mobile"]/input')
        loc2 = (By.XPATH, '//*[@id="password"]/input')
        loc3 = (By.ID, "loginBtn")
        # loc4 = (By.XPATH, '//*[@id="mobile"]/input')
        # self.driver.find_element_by_xpath('//*[@id="mobile"]/input').clear()
        Base(self.driver).clear([By.XPATH, '//*[@id="mobile"]/input'])
        Base(self.driver).sendKeys(loc1, user)
        Base(self.driver).sendKeys(loc2, psw)
        # Base(self.driver).screenShot("登录")
        # 点击登陆
        Base(self.driver).click(loc3)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    zhixin = LoginZhiXin(driver)
    zhixin.login_zhixin()
