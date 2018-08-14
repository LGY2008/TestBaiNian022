import sys, os

import allure

sys.path.append( os.getcwd() )
from Page.page_setting import PageSetting
from Base.get_driver import getDriver
from Page.page_bainian import PageBiaNian
from Base.read_yml import ReadYaml
import pytest
def get_data(data_type):
    add_address = []
    edit_address = []
    datas = ReadYaml( "address_data" ).read_yaml()
    if data_type == "add":
        for data in datas.get( "add_address" ).values():
            add_address.append( (data.get( "name" ), data.get( "phone" ), data.get( "address" ), data.get( "post" )) )
        return add_address
    elif data_type == "edit":
        for data in datas.get( "edit_address" ).values():
            edit_address.append( (data.get( "name" ), data.get( "phone" ), data.get( "province" ), data.get( "city" ),
                                 data.get( "area" ), data.get( "detail_address" ), data.get( "expect_toast" )) )
        return edit_address
class TestAddress():
    def setup_class(self):
        self.driver = getDriver( "com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity" )
        self.pageSet = PageSetting( self.driver )
        self.pageBai = PageBiaNian( self.driver )
        # 登录
        self.pageBai.page_login_all()
        # 点击地址管理
        self.pageSet.page_click_address_manage()

    def teardown_class(self):
        self.driver.quit()

    @allure.step("添加地址方法")
    @pytest.mark.run( order=1 )
    @pytest.mark.parametrize("name,phone,address,post",get_data("add"))
    def test_add_address(self, name, phone, address, post):
        # 点击新增地址
        self.pageSet.page_click_new_address()
        # 输入收件人
        self.pageSet.page_input_recipients( name )
        # 输入手机号
        self.pageSet.page_input_phone( phone )
        # 所在地区
        self.pageSet.page_select_area()
        # 输入详细地址
        self.pageSet.page_detail_address( address )
        # 输入邮编
        self.pageSet.page_input_post( post )
        # 设为默认地址
        self.pageSet.page_default_address()
        # 点击保存地址按钮
        self.pageSet.page_click_save_address()
        try:
            # 1. 断言 地址是否新增成功 姓名+手机号
            str = name + "  " + phone
            assert str in self.pageSet.page_get_address_list()
            # print("获取的地址列表为：",self.pageSet.get_address_list())
            # 2. 断言 是否有默认按钮
            assert self.pageSet.page_find_default_mark_true_false()
            allure.attach("描述","地址添加成功！")
        except:
            # 截图
            self.pageSet.base_get_screen_shot()
            allure.attach( "添加地址描述", "地址添加失败！" )
            raise
    @allure.step("修改地址方法")
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name,phone,province,city,area,detail_address,expect_toast",get_data("edit"))
    def test_modifi_address(self,name,phone,province,city,area,detail_address,expect_toast):
        # 点击编辑
        self.pageSet.page_click_edit_btn()
        # 点击修改
        self.pageSet.page_click_edit_modify( name, phone, province, city, area, detail_address )
        try:
            # 断言 toast
            assert expect_toast in self.pageSet.page_get_toast( expect_toast )
            # 断言 姓名+电话
            str = name + "  " + phone
            assert str in self.pageSet.page_get_address_list()
            allure.attach("修改地址描述","地址修改成功！")
        except:
            print( "出错误了！" )
            pass

    @pytest.mark.run(order=3)
    @allure.step("删除地址")
    def test_delete_address(self):
        # 调用删除方法
        self.pageSet.page_delete_address()
        try:
            # 断言是否删除成功
            assert self.pageSet.page_if_address_list()
            allure.attach("删除描述","删除地址成功！")
        except:
            # 截图
            self.pageSet.base_get_screen_shot()
            allure.attach("删除地址","删除地址失败！")
            raise
