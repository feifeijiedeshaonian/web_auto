from selenium import webdriver
from time import sleep
from selenium. webdriver. common. by import By
from login__zhixin import LoginZhiXin
from login__zhiyou import LoginZhiYou
from login__zhiyou__guanli import LoginZhiYouGuanLi
from common import Base


class ApprovalCompanyProject():

    def __init__(self, driver):
        self.driver = driver

    # name为要审批的项目名称
    def approval_company_project(self, name):
        sleep(1)
        base = Base(self.driver)
        # 点击正式项目管理
        base.click([By.XPATH, "//*[@id='leftBox']/ul/li[2]/ul/li/ul/li[1]"])
        # 选择要审批的项目
        sleep(1)
        for num in range(1, 6):
            companyname = self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[3]/div/div[3]/table/tbody/tr[' + str(num) + ']/td[3]/div').text
            if name == str(companyname):
                # 点击查看
                self.driver.find_element_by_xpath('//*[@id="pane-first"]/div/div[3]/div/div[4]/div[2]/table/tbody/tr[' + str(num) + ']/td[9]/div/div/div[1]').click()
                break
        # 点击同意
        base.click([By.XPATH, '//*[@id="printContent"]/div[1]/div[2]/div/span[1]'])
        base.sendKeys([By.CLASS_NAME, "el-textarea__inner"], "同意同意同意")
        base.click([By.XPATH, '//*[@id="approvalDetail"]/div[2]/div/div[3]/span/button[2]/span'])
        sleep(1)
        # 点击审批主题
        base.click([By.XPATH, '//*[@id="pane-first"]/div/div[1]/form/div[2]/div/div/div/input'])
        # 选择我已审批
        sleep(1)
        base.click([By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]/span'])
        # 点击查询
        base.click([By.XPATH, '//*[@id="pane-first"]/div/div[1]/div/div[2]/button[1]/span'])
        # self.driver.get_screenshot_as_file("E:\\screenshot\\审批项目.png")


if __name__ == "__main__":

    driver = webdriver.Chrome()
    LoginZhiXin(driver).login_zhixin("15733189935", "2222wwww")
    LoginZhiYou(driver).login_zhiyou()
    LoginZhiYouGuanLi(driver).login_zhiyou_guanli()
    ApprovalCompanyProject(driver).approval_company_project("张凯测试公司项目2.0")