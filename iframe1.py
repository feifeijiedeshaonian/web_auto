from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://tj.ganji.com/")
driver.implicitly_wait(12)
driver.find_element_by_link_text("工作").click()


t = driver.window_handles
r = driver.current_window_handle
new_handle = t[-1]
driver.switch_to_window(new_handle)
sleep(3)
driver.find_element_by_id("search_keyword").send_keys("ceshi")
