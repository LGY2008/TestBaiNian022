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

driver.find_element_by_xpath("//*[contains(@text,'WLAN')]").click()

# id 定位一组元素
# elements=driver.find_elements_by_id("com.android.settings:id/title")
# print("element长度：",len(elements))
# for element in elements:
#     print(element.get_attribute("text"))
#     if element.get_attribute("text")=="显示":
#         element.click()

# class 定位元素
elements=driver.find_elements_by_class_name("android.widget.TextView")
print("elements长度为：",len(elements))
for element in elements:
    print(element.text)



time.sleep(3)
driver.quit()



