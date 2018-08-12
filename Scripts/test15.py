import pytest


class Test001():

    @pytest.fixture()
    def before(self):
        print("before被执行")
    def test001(self):
        print("test001被执行")
    @pytest.mark.usefixtures("before")
    def test002(self):
        print("test002被执行")
    # 通过参数引用
    def test003(self,before):
        print("test003被执行")