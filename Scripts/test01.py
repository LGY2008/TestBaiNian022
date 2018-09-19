import threading
from appium import webdriver
def get_driver(port):
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.13.101:5555'
    # 获取使用toast
    # desired_caps['automationName'] = 'Uiautomator2'
    # desired_caps['udid'] = udid
    # 输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    driver= webdriver.Remote( 'http://localhost:%s/wd/hub'%port, desired_caps )
if __name__ == '__main__':
    # threading.Thread( target=get_driver, kwargs={"port": "4723", "udid": "192.168.13.101:5555"} ).start()
    # threading.Thread( target=get_driver, kwargs={"port": "4725", "udid": "192.168.13.102:5555"} ).start()
    get_driver("4723")