import allure, pytest


class Test_01():

    @allure.step(title="这是测试步骤一")
    def test_001(self):
        print("------>")
        allure.attach("登录模块", "输入手机号和密码才能登录")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是测试步骤二")
    def test_002(self):
        print("<------------")
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是测试步骤三")
    def test_003(self):
        print("<------------")
        assert False

    def test_004(self):
        with open("C:\\Users\\Y\\Desktop\\app_allure\\scripts\\捕获.PNG", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
