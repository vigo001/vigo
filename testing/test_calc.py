"""
课后作业
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()
"""

import pytest

from pythoncode.calculator import Calculator


class TestCalc:

    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [231312322, 100, 231312422], [0.1, 0.1, 0.2], [-1, -1, -2]])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect
        print(result)

    @pytest.mark.parametrize('a,b,expect', [[0.4, 0.5, 0.9], [2.7, 1.1, 3.8]])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert round(result, 2) == expect

    @pytest.mark.parametrize('a,b', [[100, 0], [-22, 0], [0.4, 0]])
    def test_div(self, a, b):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(a, b)

    @pytest.mark.parametrize('a,b,expect', [[0, 100, -100], [-1, 1, -2], [-2, -2, -0]])
    def test_div(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect
        print(result)
