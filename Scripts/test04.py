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
driver.close_app()

# 发送文件到手机
with open("./push07.txt","r",encoding="utf-8") as f:
    data=str(base64.b64encode(f.read().encode("utf-8")),"utf-8")
    driver.push_file("/sdcard/push07.txt",data)

# 拉取文件到桌面
data=driver.pull_file("sdcard/push07.txt")
data=str(base64.b64decode(data),"utf-8")
filename="./w.txt"
with open(filename,"w",encoding="utf-8") as f:
    f.write(data)

print(type(data))