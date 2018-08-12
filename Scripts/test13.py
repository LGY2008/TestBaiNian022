import base64

from appium import webdriver
import time
# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

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
driver.implicitly_wait(30)

# 获取手机时间
print(driver.device_time)

# 获取手机款高
print(driver.get_window_size())

# 发送键到设备
for i in range(3):
    driver.keyevent(24)

# 操作手机通知栏
driver.open_notifications()

# 获取手机网络
print(driver.network_connection)

# # 设置网路为0
# driver.set_network_connection(6)
#
# # 获取手机网络
# print(driver.network_connection)

# 截屏
driver.get_screenshot_as_file("./img01.png")


time.sleep(3)
driver.quit()