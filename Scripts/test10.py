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
# 根据name属性返回
data=driver.find_element_by_id("com.android.settings:id/search")
print("位置：",data.location)
print("包名：",driver.current_package)
print("启动名：",driver.current_activity)
time.sleep(3)
driver.quit()



