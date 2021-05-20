'''封装登录操作'''
from appium_advance.page_object.desired_caps import appium_desired
from appium_advance.page_object.common_fun import Common
from selenium.webdriver.common.by import By
import logging

'''这个类继承Common类'''
class LoginView(Common):

    '''用户名输入框'''
    username_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    '''密码输入框'''
    password_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    '''登录按钮'''
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')


    def login_action(self,username,password):
        '''是继承的Common类的两个方法'''
        '''登录之前先是点击取消按钮---再点击跳过按钮'''
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('===============login===============')
        logging.info('start input username:%s'%username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('start input password:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('start click loginBtn.')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('start login finished ')

if __name__ == '__main__':
    driver=appium_desired()
    '''生成一个LoginView类实例/对象l 因为LoginView继承Common，Common又继承的BaseView有个初始化参数driver 所以必须传'''
    l=LoginView(driver)
    '''实例再去调类中定义的方法'''
    l.login_action('自学网2018','zxw2018')