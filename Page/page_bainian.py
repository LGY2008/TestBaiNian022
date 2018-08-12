from selenium.webdriver.common.by import By
from Base.base_init import BaseInit
import Page
class PageBiaNian(BaseInit):
    # 点击我的
    def page_click_my_btn(self):
        self.base_click_element(Page.set_me_btn)
    # 点击已有账号，去登录
    def page_click_link_btn(self):
        self.base_click_element(Page.set_link_login)
    # 登录 输入用户名/密码
    def page_input_username_pwd(self,username,pwd):
        # 输入用户名
        self.base_input_text(Page.set_input_username,username)
        # 输入密码
        self.base_input_text(Page.set_input_pwd,pwd)
        # 点击登录按钮
        self.base_click_element(Page.set_login_btn)
    # 一次性登录专用
    def page_login_all(self,username="18610453007",pwd="123456"):
        # 点击我的
        self.page_click_my_btn()
        # 点击登录连接
        self.page_click_link_btn()
        # 输入用户名和密码
        self.page_input_username_pwd(username,pwd)
        # 点击设置按钮
        self.page_click_set_btn()
    # 判断是否登录成功
    def page_get_login_nickname(self):
        # 获取登录后的昵称
        return self.base_get_text(Page.set_nick_name)

    # 点击设置按钮
    def page_click_set_btn(self):
        # 点击设置
        self.base_click_element(Page.set_login_set)