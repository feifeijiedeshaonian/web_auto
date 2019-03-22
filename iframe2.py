from selenium import webdriver
from time import sleep
# 玩转鼠标键盘操作（ActionChains）
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(12)
mouse = driver.find_element_by_link_text("设置")
# move_to_element(to_element) ——鼠标移动到某个元素
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
sleep(3)
# 定位到的元素
el = driver.find_element_by_id("nr")
Select(el).select_by_index(2)
el.click()
# 点击保存设置
driver.find_element_by_link_text("保存设置").click()
# alert弹窗处理
# 切换到alert
a = driver.switch_to.alert
# 获取文本
t = a.text 
print(t)
# 点确定的意思   取消a.dismiss()
a.accept()