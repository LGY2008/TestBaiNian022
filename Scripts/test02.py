import time, threading
from selenium import webdriver

def more_browser(port,browser):
    desired_capabilities={
        'platform': 'ANY',
        'browserName': browser,
        'version': '',
        'javascriptEnabled': True
        }

    driver = webdriver.Remote(command_executor="http://127.0.0.1:%s/wd/hub" % port,desired_capabilities=desired_capabilities)
    if port == "5555":
        driver.get("http://www.baidu.com")
    else:
        driver.get("https://github.com")
    # time.sleep(10)
    #
    # driver.quit()

if __name__ == '__main__':
    # port_list = ["5555","8888"]
    port_list=[{"port":"5555","browser":"chrome"},{"port":"8888","browser":"firefox"}]
    for i in port_list:
        th = threading.Thread(target=more_browser, kwargs=i)
        th.start()