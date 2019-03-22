from selenium import webdriver
from time import sleep
from selenium. webdriver. common. by import By
from selenium.webdriver.common.action_chains import ActionChains
from common2 import Base
from login__zhixin1 import LoginZhiXin
from pymouse import PyMouse
from pykeyboard import PyKeyboard


class Common():

    def __init__(self, driver):
        self.driver = driver

    # name是搜索人姓名
    def search(self, name="张超"):
        sleep(1)
        Base.sendKeys(self, [By.ID, "search-input"], name, self.driver)
        sleep(1)
        self.driver.get_screenshot_as_file("E:\\screenshot\\搜索人" + name + ".png")
        Base.click(self, [By.XPATH, "//*[@id='app']/div/section/header/div[1]/ul/li[1]"], self.driver)
    
    # 发送文字,words是输入的文字内容
    def sendWord(self, words):
        Base.sendKeys(self, [By.CLASS_NAME, "editor"], words, self.driver)
        Base.click(self, [By.XPATH, '//*[@id="app"]/div/section/section/div[2]/div/div[2]/div/div[2]/div[2]/div/button'], self.driver)

    def withdraw(self):
        sleep(1)
        right_click = self.driver.find_element_by_xpath('//*[@id="scroll-body"]/li/div/div[2]/div/p')
        # 对定位到的元素执行右击操作
        ActionChains(driver).context_click(right_click).perform()
        # 撤回
        Base.click(self, [By.XPATH, '//*[@id="message-container"]/ul[2]/li[1]/button'], self.driver)
        sleep(1)
        self.driver.get_screenshot_as_file("E:\\screenshot\\撤回.png")


if __name__ == "__main__":

    driver = webdriver.Chrome()
    LoginZhiXin(driver).login_zhixin("13820921009", "1111qqqq")
    Common(driver).search()
    Common(driver).sendWord("故上的束缚，造成纯真的人性的扭曲，造成入选初中语文，人民教育出版社九年级")
    pym = PyMouse()
    pyk = PyKeyboard()
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/div[2]/div/div[2]/div/div[2]/div[1]/span[2]').click()
    sleep(1)
    pyk.tap_key(pyk.shift_key) # 切换为英文，看实际情况是否需要
    sleep(1)
    pyk.type_string("C:\\Users\\LENOVO\\Desktop\\zhangkai\\webv1.1.xlsx")# 打开文件所在目录，方便多个文件上传
    sleep(1)
    pyk.tap_key(pyk.enter_key)
    sleep(1)
