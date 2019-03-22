from selenium import webdriver
import time


#只读型日期选择，去除属性后输入，利用js命令 
driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
time.sleep(3)
js = '''document.getElementById("train_date").removeAttribute("readonly");
        document.getElementById("train_date").value="2019-04-19"'''
driver.execute_script(js)