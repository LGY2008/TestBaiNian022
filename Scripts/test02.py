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
driver.close_app()

time.sleep(3)
# 卸载腾讯新闻
# driver.start_activity("com.tencent.news",".activity.SplashActivity")
driver.remove_app("com.tencent.news")
time.sleep( 5 )
# 安装腾讯新闻
driver.install_app("c:\\tengxunxinwen_5610.apk")

driver.quit()

# com.tencent.news/.activity.SplashActivity