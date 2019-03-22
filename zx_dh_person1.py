from selenium import webdriver
import os
from time import sleep
from selenium. webdriver. common. by import By
# 复制 import keys模块
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from common import Base
from login__zhixin import LoginZhiXin


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

    def delete(self):
        sleep(1)
        right_click = self.driver.find_element_by_xpath('//*[@id="scroll-body"]/li/div/div[2]/div/p')
        # 对定位到的元素执行右击操作
        ActionChains(driver).context_click(right_click).perform()
        # 删除
        Base.click(self, [By.XPATH, '//*[@id="message-container"]/ul[2]/li[2]/button'], self.driver)
        sleep(1)
        self.driver.get_screenshot_as_file("E:\\screenshot\\撤回.png")

    # 复制
    def copy(self):
        sleep(1)
        right_click = self.driver.find_element_by_xpath('//*[@id="scroll-body"]/li/div/div[2]/div/p')
        # 对定位到的元素执行右击操作
        ActionChains(driver).context_click(right_click).perform()
        # 删除
        Base.click(self, [By.XPATH, '//*[@id="message-container"]/ul[2]/li[3]/button'], self.driver)
        # 模拟鼠标复制（ctrl+v）
        self.driver.find_element_by_class_name('editor').send_keys(Keys.CONTROL,'v')
        sleep(1)
        self.driver.get_screenshot_as_file("E:\\screenshot\\复制.png")
        # 将复制内容发送出去
        Base.click(self, [By.XPATH, '//*[@id="app"]/div/section/section/div[2]/div/div[2]/div/div[2]/div[2]/div/button'], self.driver)
        self.driver.get_screenshot_as_file("E:\\screenshot\\复制1.png")

    # 转发
    def transpond(self, transpond_name="任少龙"):
        sleep(1)
        right_click = self.driver.find_element_by_xpath('//*[@id="scroll-body"]/li[2]/div/div[2]/div/p')
        # 对定位到的元素执行右击操作
        ActionChains(driver).context_click(right_click).perform()
        Base.click(self, [By.XPATH, '//*[@id="message-container"]/ul[2]/li[4]/button'], self.driver)
        # 选择收件人
        Base.sendKeys(self, [By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/section/div[1]/div/div/input'], transpond_name, self.driver)
        sleep(1)
        Base.click(self, [By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/section/div[1]/ul/li[1]'], self.driver)
        # 点击确定
        Base.click(self, [By.XPATH, '/html/body/div[3]/div[2]/div/div/div[3]/div/button'], self.driver)
        # 切换到任少龙界面
        sleep(1)
        Base.click(self, [By.XPATH, '//*[@id="app"]/div/section/section/div[1]/div/ul[1]/li[1]'], self.driver)
        # driver.get_screenshot_as_file("E:\\screenshot\\转发.png")


if __name__ == "__main__":

    driver = webdriver.Chrome()
    LoginZhiXin(driver).login_zhixin("13820921009", "1111qqqq")
    Common(driver).search()
    Common(driver).sendWord("故上的束缚，造成纯真的人性的扭曲，造成入选初中语文，人民教育出版社九年级")
    Common(driver).withdraw()
    Common(driver).sendWord("间客房哈萨克发动机哈斯卡拉答复哈士大夫快速减肥还是卡及地方海事局卡的发挥看大夫撒反抗撒旦发萨科范德萨科技孵化\
        zxc,mvzx.vxmvxzvm.xzvcmxz,.vx.zv,mx,.cvmxz,cvmxcz,vmx,zvm看看撒开发撒士大夫卡萨开发；拉框受到法律飒飒离开对方 啊撒飞洒领导啊打发啊士\
        离开房间拉萨的房间爱上了的看法金属拉丝卢萨卡发动机萨拉丁飞机撒赖扩大飞机加快速度khkj")
    Common(driver).delete()
    Common(driver).sendWord("《故乡》是现代文学家鲁迅于1921年创作的一篇短篇小说。小说以“我”回故乡的活动为线索，按照“回故乡”——“在故乡”——“离故\
        乡”的情节安排，依据“我”的所见所闻所忆所感，着重描写了闰土和杨二嫂的人物形象，从而反映了辛亥革命前后农村破产、农民痛苦生活的现实；同时深刻\
        指出了由于受封建社会传统观念的影响，劳苦大众所受的精神上的束缚，造成纯真的人性的扭曲，造成人与人之间的冷漠、隔膜，表达了作者对现实的强烈\
        不满和改造旧社会、创造新生活的强烈愿望。该小说入选初中语文，人民教育出版社九年级")
    Common(driver).copy()
    Common(driver).transpond()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/section/section/div[2]/div/div[2]/div/div[2]/div[1]/span[2]').click()
    sleep(1)
    # 发送附件
    path = "E:\\screenshot\\登录.png"
    os.system('E:\\python\\zk1\\autoit1.au3 %s' % path)