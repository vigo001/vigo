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

    @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [100, 100, 200], [0.1, 0.1, 0.2], [-1, -1, -2]])
    def test_add(self, a, b, expect):
        result1 = self.calc.add(a, b)
        assert result1 == expect
        print(result1)

    @pytest.mark.parametrize('m,n,expect1',
                             [[0, 100, 0], [2, 1, 2], [0.9, 0.3, 3], [-1, -1, 1], [-2, 2, -1]])
    def test_div(self, m, n, expect1):
        result2 = self.calc.div(m, n)
        assert result2 == expect1
        print(result2)

    @pytest.mark.parametrize('i,j,expect2',
                             [[0, 100, -100], [2, 1, 1], [0.9, 0.3, 0.6], [-1, 1, -2], [-2, -2, -0]])
    def test_div(self, i, j, expect2):
        result3 = self.calc.sub(i, j)
        assert result3 == expect2
        print(result3)
