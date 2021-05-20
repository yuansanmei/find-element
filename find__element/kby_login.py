#从capability模块导入这两个driver,NoSuchElementException
from find__element.capability  import driver,NoSuchElementException


def login():
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('自学网2018')

    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

#开始捕获这个异常
try:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
#注意这里只是判断没有click
#如果没有-我-这样的元素，那么直接调用login()
#不存在这样的元素 那么直接调用login()
except NoSuchElementException:
    login()
else:
    #如果存在-我---那么点击我，然后点击未登录按钮---然后点击请输入用户名---点击请输入密码---
    #如果存在这样的元素，那么点击我--然后点击未登录按钮--再调用login()
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_username').click()
    login()



#场景：账号之前登录过
#要先去点击-我--com.tal.kaoyan:id/mainactivity_button_mysefl
#未登录--com.tal.kaoyan:id/activity_usercenter_username
#请输入用户名--com.tal.kaoyan:id/login_email_edittext
#请输入密码--com.tal.kaoyan:id/login_password_edittext
#登录按钮--com.tal.kaoyan:id/login_login_btn

#场景：账号之前未登录过
#是否是第一次进来
    #是
    #存在取消和跳过按钮，然后到登录界面
    #取消id=android:id/button2
    #跳过id=com.tal.kaoyan:id/tv_skip

    #否
    #不存在取消和跳过按钮，直接到登录界面
    #请输入用户名--com.tal.kaoyan:id/login_email_edittext
    #请输入密码--com.tal.kaoyan:id/login_password_edittext
    #登录按钮--com.tal.kaoyan:id/login_login_btn