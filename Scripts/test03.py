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

# 判断腾讯新闻是否安装
try:
    if driver.is_app_installed("com.tencent.news"):
        print("腾讯新闻已安装，即将开始卸载！")
        driver.remove_app("com.tencent.news")
        print("腾讯新闻卸载完成！")
    else:
        print("未检测到腾讯新闻，准备安装...")
        driver.install_app("c:\\tengxunxinwen_5610.apk")
        print("腾讯新闻安装完毕！")
except:
    print("安装失败！")
driver.quit()

# com.tencent.news/.activity.SplashActivity