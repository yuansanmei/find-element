#从capability模块导入这两个driver,NoSuchElementException
from find__element.capability  import driver,NoSuchElementException


def login():
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('自学网2018')

    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

try:
    driver.find_element_by_id('com.paic.zhifu.wallet.activity:id/home_card_login_txt')

    #注意这里先判断是否有登录按钮click
except NoSuchElementException:
    #如果没有-我-这样的元素，那么直接调用login()
    login()
else:
    #如果存在-登录按钮---那么点击登录按钮，然后点击---然后点击请输入用户名---点击请输入密码---
    driver.find_element_by_id('com.paic.zhifu.wallet.activity:id/home_card_login_txt').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()

    login()