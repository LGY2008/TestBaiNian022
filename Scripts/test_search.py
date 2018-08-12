import pytest,os,sys
sys.path.append(os.getcwd())
from Page.page_search import PageSearch
from Base.get_driver import getDriver
from Base.read_yml import ReadYaml
def get_data():
    datas=ReadYaml("search_data").read_yaml()
    arrs=[]
    for data in datas.values():
        arrs.append(data.get("input_text"))
    return arrs
class TestSearch():
    def setup_class(self):
        # 获取Driver
        self.driver=getDriver()
        # 实例化Page页面
        self.search=PageSearch(self.driver)
    def teardown_class(self):
        self.driver.quit()
    @pytest.mark.parametrize("text",get_data())
    def test_click_search_btn(self,text):
        # 点击搜索按钮
        self.search.page_click_search_btn()
        # 输入文本内容
        self.search.page_input_text(text)
        # 点击返回按钮
        self.search.page_click_back_btn()
    # def test_getdata(self):
    #     print(get_data())