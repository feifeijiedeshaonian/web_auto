from selenium import webdriver
from time import sleep
import os
from login__zhixin import LoginZhiXin
from login__zhiyou import LoginZhiYou


driver = webdriver.Chrome()
# driver.maximize_window()
LoginZhiXin(driver).login_zhixin("13820921009", "1111qqqq")
LoginZhiYou(driver).login_zhiyou()   
driver.find_element_by_xpath('//*[@id="menu"]/li[3]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="addNew"]/div/div/div[1]').click()
sleep(1)
# 搜索收件人 添加收件人、主题、内容、点击确定发送
driver.find_element_by_class_name('add-btn').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="mail-chat"]/div[2]/div[3]/div/div[2]/div[1]/ul/li[3]/input').send_keys("张超")
sleep(1)
driver.find_element_by_xpath('//*[@id="mail-chat"]/div[2]/div[3]/div/div[2]/div[1]/ul/li[3]/div/div[2]/div[1]/ul/li/div/p[1]').click()
driver.find_element_by_xpath('//*[@id="mail-chat"]/div[2]/div[3]/div/div[2]/div[1]/div/button[1]').click()
driver.find_element_by_xpath('//*[@id="mail-chat"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/input').send_keys("测试发送个人智邮")
driver.find_element_by_xpath('//*[@id="mail-chat"]/div[2]/div[1]/div[2]/div[2]/div[3]/textarea').send_keys("测试个人智邮发送邮件测试个人智邮发送邮件测试\
\个人智邮发送邮件测试个人智邮发送邮件测试个人智邮发送邮件个人智邮发送邮件测试个人智邮发送邮件个人智邮发送邮件测试个人智邮发送邮件个人智邮发送邮件")
sleep(1)
driver.find_element_by_class_name("content-list").click()
sleep(1)
os.system('C:\\Users\\LENOVO\\Desktop\\张凯\\111.exe')
sleep(1)
driver.find_element_by_xpath('//*[@id="mail-chat"]/div[2]/div[1]/div[3]/div/button[1]').click()
