from Base.base_init import BaseInit
import Page
class PageSetting(BaseInit):
    # 点击地址管理
    def page_click_address_manage(self):
        self.base_click_element(Page.set_address)
    # 点击新增地址
    def page_click_new_address(self):
        self.base_click_element(Page.set_new_address_btn)
    # 收件人
    def page_input_recipients(self,value):
        self.base_input_text(Page.address_receipt_name,value)
    # 手机号
    def page_input_phone(self,value):
        self.base_input_text( Page.address_add_phone, value )
    # 所在地区
    def page_select_area(self):
        # 点击选地区
        self.base_click_element(Page.address_add_province)
        # 选择省
        self.base_click_element(Page.address_area_sheng)
        # 选择市大框
        self.base_click_element(Page.address_area_shi_kuang)
        # 选择市
        self.base_click_element(Page.address_area_shi)
        # 选择区
        self.base_click_element(Page.address_area_qu)
    # 详细地址
    def page_detail_address(self,value):
        self.base_input_text(Page.address_add_info,value)
    # 设置邮编
    def page_input_post(self,value):
        self.base_input_text(Page.address_add_post,value)
    # 设为默认地址
    def page_default_address(self):
        self.base_click_element(Page.address_add_default)
    # 点击保存地址按钮
    def page_click_save_address(self):
        self.base_click_element(Page.address_save_address)
    # 点击编辑按钮
    def page_click_edit_btn(self):
        self.base_click_element(Page.address_add_edit)
    # 点击编辑-》修改
    def page_click_edit_modify(self,name,phone,province,city,area,detail_address):
        # 获取修改列表
        els=self.find_elements(Page.address_edit_modify)
        # 点击修改 默认修改列表第一个
        self.base_click(els,num=1)
        # 修改姓名
        self.base_input_text(Page.address_receipt_name,name)
        # 修改电话
        self.base_input_text(Page.address_add_phone,phone)
        # 点击所在地区
        self.base_click_element( Page.address_add_province02 )
        # 修改区域
        self.find_element_xpath_click(province)
        self.find_element_xpath_click(city)
        self.find_element_xpath_click(area)

        # 修改详细地址
        self.page_detail_address(detail_address)
        # 修改默认按钮
        self.base_click_element(Page.address_add_default)
        # 点击保存
        self.base_click_element(Page.address_edit_modify_save)
    # 点击编辑-》删除
    def page_click_edit_delete(self):
        # 获取删除列表
        els=self.find_elements(Page.address_get_address_list)
        for i in range(len(els)):
            # 点击编辑按钮
            self.page_click_edit_btn()
            # 获取删除文字列表
            del_list = self.find_elements( Page.address_delete_text )
            # 点击删除
            self.base_click(del_list)
            # 点击确定
            self.base_click_element(Page.address_edit_delete_yes)
    # 点击编辑-》修改-》保存
    def page_click_edit_modify_save(self):
        self.base_click_element(Page.address_edit_modify_save)
    # 点击编辑-》修改-》返回
    def page_click_edit_modify_back(self):
        self.base_click_element(Page.address_edit_modify_back)
    # 点击编辑-》删除
    def page_click_edit_delet(self):
        self.base_click_element(Page.address_edit_delete)
    # 点击编辑-》删除-》确定
    def page_click_edit_delete_ok(self):
        self.base_click_element(Page.address_edit_delete_yes)
    # 点击编辑-》删除-》取消
    def page_click_edit_delete_cancel(self):
        self.base_click_element(Page.address_edit_delete_cancel)
    # 查找默认地址 标志
    def page_find_default_mark_true_false(self):
        try:
            self.find_element(Page.address_is_default_btn)
            return True
        except:
            return False

    # 获取地址列表
    def page_get_address_list(self):
        elements=self.find_elements(Page.address_get_address_list)
        return [i.text for i in elements]
    # 判断列表
    def page_if_address_list(self):
        try:
            self.find_element(Page.address_get_address_list)
            return False
        except:
            return True
    # 删除地址
    def page_delete_address(self):
        # 删除操作
        self.page_click_edit_delete()


    # 退出登录
    def page_logout(self):
        # 消息推送元素
        sms_msg=self.find_element(Page.set_sms_msg)
        # 修改密码元素
        modify_pwd=self.find_element(Page.set_modify_pwd)
        # 滑动 找到退出按钮
        self.base_drag_and_drop(sms_msg,modify_pwd)
        # 点击退出登录
        self.base_click_element(Page.set_logout)
        # 点击确认退出
        self.base_click_element(Page.set_logout_ok)
