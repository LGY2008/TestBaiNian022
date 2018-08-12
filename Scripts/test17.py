from Base.get_driver import getDriver
driver=getDriver("com.android.settings",".Settings")
# driver.close_app()
driver.quit()
if driver.is_app_installed("com.vcooline.aike"):
    driver.remove_app("com.vcooline.aike")
    print("卸载完成")
else:
    driver.install_app("C:\\爱客CRM.apk")
    print("安装完成")