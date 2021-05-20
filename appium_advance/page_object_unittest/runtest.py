'''7 类似于这里是只关于登录的测试用例'''
'''5-15 PageObject实践(4)—unittest用例封装'''
import unittest
test_dir='./'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login*.py')

if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(discover)