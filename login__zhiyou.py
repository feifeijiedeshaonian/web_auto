from selenium import webdriver
from login__zhixin import LoginZhiXin
from common import Base
from time import sleep
from selenium. webdriver. common. by import By


class LoginZhiYou():

    def __init__(self, driver):
        self.driver = driver

    def login_zhiyou(self):
        sleep(2)
        loc1 = (By.XPATH, '//*[@id="app"]/div/aside/ul/li[3]/button')
        sleep(1)
        Base(self.driver).click(loc1)
        # 切换光标定位
        a = self.driver.current_window_handle
        print(a)
        b = self.driver.window_handles
        self.driver.switch_to_window(b[-1])
        sleep(1)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    zhixin = LoginZhiXin(driver)
    zhiyou = LoginZhiYou(driver)
    zhixin.login_zhixin("13820921009", "1111qqqq")
    sleep(1)
    zhiyou.login_zhiyou()



    # loc1 = (By.XPATH, '//*[@id="mobile"]/input')
    #     loc2 = (By.XPATH, '//*[@id="password"]/input')
    #     loc3 = (By.ID, "loginBtn")
    #     Base.sendKeys(self, loc1, user, self.driver)
    #     Base.sendKeys(self, loc2, psw, self.driver)
    #     # 点击登陆
    #     Base.click(self, loc3, self.driver)