import os,sys
import pytest
sys.path.append(os.getcwd())
from Base.get_driver import getDriver
from Page.page_bainian import PageBiaNian
from Base.read_yml import ReadYaml
from Page.page_setting import PageSetting

def get_login_data():
    data=ReadYaml("bainian_data").read_yaml()
    arr=[]
    for i in data.values():
        arr.append((i.get("username"),i.get("password"),i.get("expect"),i.get("expect_toast"),i.get("message")))
    return arr

class TestBai():
    def setup_class(self):
        self.driver=getDriver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        self.page=PageBiaNian(self.driver)
        self.page_set=PageSetting(self.driver)
        # 点击我的
        self.page.page_click_my_btn()
        # 点击登录连接
        self.page.page_click_link_btn()
    def teardown_class(self):
        self.driver.quit()
    @pytest.mark.parametrize("username,password,expect,expect_toast,message",get_login_data())
    def test_login(self,username,password,expect,expect_toast,message):
        if expect:
            try:
                # 登录
                self.page.page_input_username_pwd( username, password )
                # 断言登录成功 Nickname
                assert expect in self.page.page_get_login_nickname()
                # 点击设置
                self.page.page_click_set_btn()
                # 退出登录
                self.page_set.page_logout()
                # 点击我的
                self.page.page_click_my_btn()
                # 点击登录连接
                self.page.page_click_link_btn()
            except:
                # 截图
                self.page.base_get_screen_shot()
                # 点击设置
                self.page.page_click_set_btn()
                # 退出登录
                self.page_set.page_logout()
                # 点击我的
                self.page.page_click_my_btn()
                # 点击登录连接
                self.page.page_click_link_btn()
                raise
        else:
            try:
                # 逆向登录
                self.page.page_input_username_pwd(username,password)
                # 获取toast消息
                msg=self.page.page_get_toast(message)
                assert msg in expect_toast
            except:
                self.page.base_get_screen_shot()
                raise


