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

# 592,944 # 592 2055

# driver.swipe(592,2055,592,944,5000)

# 存储滑到更多
save=driver.find_element_by_xpath("//*[contains(@text,'存储')]")
more=driver.find_element_by_xpath("//*[contains(@text,'更多')]")
# swipe 滑动
# driver.swipe(save.location.get('x'),save.location.get('y'),more.location.get('x'),more.location.get('y'),5000)

# scroll 从一个元素滑到另一个元素
# driver.scroll(save,more)

# 拖拽元素 从一个元素拖拽到另一个元素
# driver.drag_and_drop(save,more)

# 应用置于后台
driver.background_app(10)


time.sleep(3)
driver.quit()



