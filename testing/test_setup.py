def setup_module():
    print("setup_module")
def teardown_module():
    print("teardown_module")

def test_case1():
    print("case1")

def setup_function():
    print("资源准备：setup function")

def teardown_function():
    print("资源销毁：teardown function")

class TestDemo:

    def setup_class(self):
        prin("setup class")
    def teardown_class(self):
        print("teardown class")
    def test_demo1(self):
        pass
    def test_demo2(self):
        pass
