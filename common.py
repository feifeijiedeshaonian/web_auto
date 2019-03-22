from selenium import webdriver
from selenium. webdriver. support. wait import WebDriverWait
from selenium. webdriver. common. by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Base():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    # 判断title是否相等
    def is_title(self, _title):
        # 返回bool值
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t). until(EC.title_is(_title))
            return result
        except:
            return False

    # 判断title是否包含
    def is_title_contains(self, _title):
        # 返回bool值
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t). until(EC.title_contains(_title))
            return result
        except:
            return False

    # 判断某个元素中的text是否包含预期的字符串
    def is_text_in_element(self, locator, _text):
        # 返回bool值
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t). until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    # 判断某个元素中的value属性是否包含预期的字符串
    def is_value_in_element(self, locator, _value):
        # 返回bool值  value为空字符串返回False
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t). until(EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def is_alert(self):
        # 返回alert对象
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t). until(EC.alert_is_present())
            return result
        except:
            return False

    def findElementNew(self, locator):
        # 定位到元素，返回元素对象，没定位到返回timeout异常
        ele = WebDriverWait(self.driver, self.timeout, self.t). until(EC.presence_of_element_located(locator))
        return ele

    def findElement(self, locator):
        ele = WebDriverWait(self.driver, self.timeout, self.t). until(lambda x: x.find_element(*locator))
        return ele

    def findElements(self, locator):
        ele = WebDriverWait(self.driver, self.timeout, self.t). until(lambda x: x.find_elements(*locator))
        return ele
        
    def sendKeys(self, locator, text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self, locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self, locator):
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self, locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位到元素的个数：%s"%n)
            return True

    def screenShot(self, picture_name):
        localtime = time.strftime("%Y-%m-%d %H-%M", time.localtime())
        picname = picture_name + localtime
        self.driver.get_screenshot_as_file("E:\\screenshot\\" + picname + ".png")

    # 鼠标悬停
    def move_to_element(self, locator):
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()

    # 通过索引，index是索引第几个，从0开始。默认选第一个
    def select_by_index(self, locator, index=0):
        element = self.findElement(locator)
        Select(element).select_by_index(index)

    # 通过value属性
    def select_by_value(self, locator, value):
        element = self.findElement(locator)
        Select(element).select_by_value(value)

    # 通过文本值定位
    def select_by_text(self, locator, text):
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    # 滚动鼠标到底部
    def js_scroll_end(self):
        js_heig = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js_heig)

    # 滚动鼠标到顶部
    def js_scroll_top(self):
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)

    # 滚动到元素出现的位置
    def js_focus(self, locator):
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

if __name__ == "__main__":
    driver = webdriver. Firefox()
    driver.get("https://www.zentao.net/user-login.html")
    zentao = Base(driver)
    loc1 = (By.ID, "account")
    loc2 = (By.NAME, "password")
    loc3 = (By.ID, "submit")
    zentao.sendKeys(loc1, "admin1")
    zentao.sendKeys(loc2, "123456")
    zentao.click(loc3)