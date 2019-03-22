from selenium import webdriver
# 内嵌式滚动条   js命令
driver = webdriver.Chrome()
driver.get("file:///E:/python/zk1/div.html")
# 上下滚动
js = "document.getElementById('yoyoketang').scrollTop=10000;"
# 左右滚动
js1 ='document.getElementById("yoyoketang").scrollLeft=1000;'
driver.execute_script(js)
driver.execute_script(js1)