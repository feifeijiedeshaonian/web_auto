from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# 判断title是否与预期一致
r1 = EC.title_is("百度一下，你就知道")(driver)
print(r1)
assert r1
# 判断是否包含
r2 = EC.title_contains("百度一下")(driver)
print(r2)





driver = webdriver.Chrome()
driver.get("https://www.zentao.net/user-login.html")

# 判断元素是否存在
loc1 = ("xpath", "//*[text()='忘记密码']")
r1 = EC.presence_of_element_located(loc1)(driver)
print(r1)  # 存在返回WebElement元素对象

# 判断是否为文本属性
loc2 = ("xpath","/html/body/div[1]/div[2]/div/div[2]/div/div/div/div[2]/form/span[2]/a[1]")
r2 = EC.text_to_be_present_in_element(loc2, "忘记密码")(driver)
print(r2)