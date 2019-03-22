from selenium import webdriver
from time import sleep
from login__zhixin import LoginZhiXin
from login__zhiyou import LoginZhiYou


driver = webdriver.Chrome()
# driver.maximize_window()
LoginZhiXin(driver).login_zhixin("13820921009", "1111qqqq")
LoginZhiYou(driver).login_zhiyou()   
driver.find_element_by_xpath('//*[@id="menu"]/li[2]').click()
sleep(1)
for num in range(1, 10):
    name5 = driver.find_element_by_xpath("//*[@id='temp']/div/div[" + str(num) + "]/div/div/div[2]/div[1]/p[1]").text
    # 选择项目主题
    qq = '测试临时项目1.1'
    if qq in name5:
        driver.find_element_by_xpath("//*[@id='temp']/div/div[" + str(num) + "]/div/div/div[2]/div[1]/p[1]").click()
sleep(1)
driver.find_element_by_xpath('//*[@id="addNew"]/div/div/div[1]/img').click()
sleep(1)
# 输入邮件主题、重要收件人、邮件内容、发送邮件
driver.find_element_by_xpath('//*[@id="mail-chat"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/input').send_keys("11112222")
driver.find_element_by_xpath('//*[@id="mail-chat"]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/input').send_keys("小明")
driver.find_element_by_xpath('//*[@id="mail-chat"]/div[2]/div[1]/div[2]/div[2]/div[3]/textarea').send_keys("小明122222222222222222222311111112452452452424525")
sleep(1)
driver.find_element_by_xpath('//*[@id="mail-chat"]/div[2]/div[1]/div[3]/div/button[1]').click()