from find__element.capability import driver

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('55555')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')

driver.save_screenshot('login.png')
driver.get_screenshot_as_file('./images/login.png')#相对路径
#如果写的是绝对路径 需要转义 记得前面加r

driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()