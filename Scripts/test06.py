import base64

from appium import webdriver
import time
# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'zzz'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote( 'http://localhost:4723/wd/hub', desired_caps )
time.sleep(3)
driver.find_element_by_xpath("//*[@resource-id='com.android.settings:id/search']").click()
time.sleep(3)
# driver.find_element_by_class_name("android.widget.ImageButton").click()
# driver.find_element_by_accessibility_id("收起").click()
# driver.find_element_by_xpath("//*[@content-desc='收起']").click()
time.sleep(3)
driver.quit()



