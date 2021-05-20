'''6 登录模块用例用例的封装 把需求中的3个场景写进来'''
import sys
from Start_End import StartEnd
from appium_advance.page_object_unittest.login_view import LoginView
# from login_view import LoginView

import unittest
import logging
sys.path.append('..')

'''继承哪个类 继承StartEnd类'''
class TestLogin(StartEnd):
    def test_login_zxw2018(self):
        logging.info('============test_login_zxw2018============')
        l=LoginView(self.driver)
        l.login_action('自学网2018','zxw2018')
    def test_login_zxw2017(self):
        logging.info('============test_login_zxw2017============')
        l=LoginView(self.driver)
        l.login_action('自学网2017','zxw2017')
    def test_login_error(self):
        logging.info('============test_login_error============')
        l=LoginView(self.driver)
        l.login_action('666','222')



'''
if __name__ == '__main__':
    unittest.main()
我没有写这段 而是封装成一个单独的运行用例的py文件，即runtest.py
'''