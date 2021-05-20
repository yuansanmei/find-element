'''封装通用公共类'''
'''类Common会继承baseView文件的类BaseView'''
from appium_advance.page_object.baseView import BaseView
from appium_advance.page_object.desired_caps import appium_desired#desired_caps文件里面的appium_desired方法
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging


class Common(BaseView):
    '''取消按钮'''
    cancelBtn=(By.ID,'android:id/button2')
    '''跳过按钮'''
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')

    def check_cancelBtn(self):
        logging.info("============check_cancelBtn===============")

        try:
            element = self.driver.find_element(*self.cancelBtn)#这里的find_element指的是BaseView里面定义的方法 loc=self.cancelBtn
        except NoSuchElementException:
            logging.info('update element is not found!')
        else:
            logging.info('click cancelBtn')
            element.click()

    def check_skipBtn(self):
        logging.info("==========check_skipBtn===========")
        try:
            element = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('skipBtn element is not found!')
        else:
            logging.info('click skipBtn')
            element.click()

if __name__ == '__main__':

    driver=appium_desired()
    '''生成一个实例 因为Common继承的BaseView有参数driver 所以需要传'''
    com=Common(driver)
    '''这个实例开始调用类里面的方法'''
    com.check_cancelBtn()
    com.check_skipBtn()
