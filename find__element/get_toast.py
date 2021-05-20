'''
注意：Toast内容为中文时，顶部必须注释
# coding=utf-8
否则会因为编解码导致文字识别失败。
'''


# coding=utf-8
from find__element.capability import driver
from selenium.webdriver.support.ui import WebDriverWait

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('zxss018')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()


#error_message="用户名或密码错误，你还可以尝试4次"
error_message="账号不存在"
limit_message="验证失败次数过多，请15分钟后再试"


#使用xpath定位
message='//*[@text=\'{}\']'.format(error_message) #等同于把error_message的文字部分放到大括号那里，但是现在这种写法可读性好，如果修改文字，只修改上面的就行
# message='//*[@text=\'{}\']'.format(limit_message)


#等待这个元素出现，最多一共等待5s 如果出现就把它的text属性打印出来
toast_element=WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)