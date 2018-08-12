from selenium.webdriver.common.by import By
"""
百年奥莱
"""
# 按钮-我
set_me_btn=By.ID,"com.yunmall.lc:id/tab_me"
# 连接-已有账户，去登录
set_link_login=By.ID,"com.yunmall.lc:id/textView1"
# 用户-输入账户
set_input_username=By.ID,"com.yunmall.lc:id/logon_account_textview"
# 密码-输入密码
set_input_pwd=By.ID,"com.yunmall.lc:id/logon_password_textview"
# 按钮-登录
set_login_btn=By.ID,"com.yunmall.lc:id/logon_button"
# 昵称
set_nick_name=By.ID,"com.yunmall.lc:id/tv_user_nikename"
# 设置
set_login_set=By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 修改密码
set_modify_pwd=By.ID,"com.yunmall.lc:id/setting_modify_pwd"
# 短信提醒
set_sms_msg=By.ID,"com.yunmall.lc:id/setting_sms_notify"

# 退出
set_logout=By.ID,"com.yunmall.lc:id/setting_logout"

# 退出确认
set_logout_ok=By.ID,"com.yunmall.lc:id/ymdialog_right_button"

# 地址管理
set_address=By.ID,"com.yunmall.lc:id/setting_address_manage"
# 新增地址
set_new_address_btn=By.ID,"com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name=By.ID,"com.yunmall.lc:id/address_receipt_name"
# 手机号
address_add_phone=By.ID,"com.yunmall.lc:id/address_add_phone"
# 所在地区
address_add_province=By.ID,"com.yunmall.lc:id/address_province"
address_add_province02=By.XPATH,"//*[contains(@resource-id,'com.yunmall.lc:id/address_province') and contains(@class,'android.widget.TextView')]"

# 详细地址
address_add_info=By.ID,"com.yunmall.lc:id/address_detail_addr_info"
# 邮编
address_add_post=By.ID,"com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_add_default=By.ID,"com.yunmall.lc:id/address_default"
# 保存新增地址
address_save_address=By.ID,"com.yunmall.lc:id/button_send"
# 省 北京市 166,372
address_area_sheng=By.XPATH,"//*[contains(@text,'北京')]"
# 市 北京市 166,372
# address_area_shi=By.XPATH,"//*[contains(@text,'北京') and contains(@resource-id,'com.yunmall.lc:id/area_title')]"
address_area_shi=By.ID,"com.yunmall.lc:id/area_title"
# 北京市 --》通过外侧大框定位
address_area_shi_kuang=By.CLASS_NAME,"android.widget.RelativeLayout"
# 区 东城区 166,372
address_area_qu=By.XPATH,"//*[contains(@text,'东城')]"
# 编辑按钮
address_add_edit=By.ID,"com.yunmall.lc:id/ymtitlebar_right_btn"
# 修改按钮
address_edit_modify=By.ID,"com.yunmall.lc:id/modify"
# 修改按钮-》保存
address_edit_modify_save=By.ID,"com.yunmall.lc:id/button_send"
# 修改按钮-》返回
address_edit_modify_back=By.ID,"com.yunmall.lc:id/back"
# 删除按钮
address_edit_delete=By.ID,"com.yunmall.lc:id/delete"
# 删除文字
address_delete_text=By.XPATH,"//*[contains(@text,'删除')]"
# 删除确认按钮
address_edit_delete_yes=By.ID,"com.yunmall.lc:id/ymdialog_left_button"
# 删除取消按钮
address_edit_delete_cancel=By.ID,"com.yunmall.lc:id/ymdialog_right_button"
# 默认地址 蓝色标志字体
address_is_default_btn=By.ID,"com.yunmall.lc:id/address_is_default"
# 获取地址列表
address_get_address_list=By.ID,"com.yunmall.lc:id/receipt_name"
# 测试地址的index.text值
address_test_address_index=By.XPATH,"//*[contains(@text,'北京市北京市东城区清河三街93号')]"