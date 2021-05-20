'''5 封装用例启动结束时的配置'''
import unittest
from desired_caps import appium_desired
from time import sleep
import logging

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('============setUp============')
        self.driver=appium_desired()
    def tearDown(self):
        logging.info('============tearDown============')
        sleep(5)
        self.driver.close_app()