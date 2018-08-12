import pytest


# @pytest.fixture(scope='class',autouse=True)
# def before():
#     print("before被执行")

# @pytest.fixture(params=[1,2,3,4])
# def get_data(request):
#     return request.param

# 函数返回列表
def get_data():
    return [(10,11),(20,21),(30,31)]


class Test001:
    def test001(self):
        print("test001被执行")
    # @pytest.mark.usefixtures("before")

    # def test002(self,get_data):
    #     print("test002被执行")
    #     print(get_data)

    # 跳过测试用例
    # @pytest.mark.skipif(condition=1>0,reason="跳过")
    # def test03(self):
    #     print("test03被执行")
    #
    # @pytest.mark.xfail(condition=1>0,reason="失败")
    # def test04(self):
    #     print("test04被执行")

    # 参数化方式1
    # @pytest.mark.parametrize("a,b",[(1,2),(3,4),(4,5)])
    # def test05(self,a,b):
    #     print("test005(a)--->",a)
    #     print("test005(b)--->",b)

    # 以参数的方式传递
    # @pytest.fixture(params=[1,2,3,4,5])
    # def _before(self,request):
    #     return request.param
    #
    # def test105(self,_before):
    #     print("test105--->",_before)

    @pytest.mark.parametrize("a,b",get_data())
    def test_parametrize(self,a,b):
        print("test_parametrize的值为(a)：",a)
        print("test_parametrize的值为(b)：",b)
