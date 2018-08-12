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
# 存储滑到更多
save=driver.find_element_by_xpath("//*[contains(@text,'存储')]")
more=driver.find_element_by_xpath("//*[contains(@text,'更多')]")
wlan=driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")

# 轻敲 wlan
# TouchAction(driver).tap(wlan).perform()

# 多指操作
# driver.tap([(save.location.get('x'),save.location.get('y')),(more.location.get('x'),more.location.get('y'))],1000)

# 按下、释放
# TouchAction(driver).press(wlan).release().perform()
# TouchAction(driver).press(x=wlan.location.get("x"),y=wlan.location.get("y")).release().perform()

# ssid=driver.find_element_by_xpath("//*[contains(@text,'SSID')]")
# 等待
# TouchAction(driver).press(ssid).wait(5000).release().perform()
# xgwl=driver.find_element_by_xpath("//*[contains(@text,'修改网络')]")
# xgwl.click()
# driver.find_element_by_xpath("//*[contains(@text,'保存')]").click()

# 长按操作
# TouchAction(driver).long_press(ssid,5000).release().perform()
# 存储滑到更多
save=driver.find_element_by_xpath("//*[contains(@text,'存储')]")
more=driver.find_element_by_xpath("//*[contains(@text,'更多')]")
# move_to 存储滑到更多
# TouchAction(driver).press(save).move_to(more).release().perform()
TouchAction(driver).press(x=save.location.get('x'),y=save.location.get('y'))\
    .move_to(x=0,y=-100).release().perform()



time.sleep(3)
driver.quit()



