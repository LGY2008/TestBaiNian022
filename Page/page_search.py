from selenium.webdriver.common.by import By

from Base.base_init import BaseInit
search_btn=By.ID,"com.android.settings:id/search"
search_input_text=By.ID,"android:id/search_src_text"
search_back_btn=By.CLASS_NAME,"android.widget.ImageButton"
class PageSearch(BaseInit):
    # 点击搜索按钮
    def page_click_search_btn(self):
        self.base_click_element(search_btn)

    # 输入内容
    def page_input_text(self,text):
        self.base_input_text(search_input_text,text)

    # 点击返回按钮
    def page_click_back_btn(self):
        self.base_click_element(search_back_btn)
