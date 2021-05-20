from find__element.capability import driver
import random

#进入注册界面选择并设置头像
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()

driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

driver.find_elements_by_id('com.tal.kaoyan:id/item_image')[1].click()

driver.find_element_by_id('com.tal.kaoyan:id/save').click()

#注册信息填写
'''
密码、邮箱报错，导致自动化注册不了的。
只要在send_keys（）之前，加上一个driver.find_elements_by_id（）.click（） 
因为用户名输入框，默认是有光标的。
密码和邮箱，默认的focused的值是false，也就是无光标，所以密码和邮箱输入不进去。
先获取光标，就能正常输入了。
'''
username='yuan2021'+'FLY'+str(random.randint(1000,9000))
print('username: %s' %username)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)


password='yuan89'+str(random.randint(1000,9000))
print('password: %s' %password)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)
driver.keyevent(61)
#调试脚本时注意 这里 调用
#问题已解决，Android8.0系统的，光标定位不到密码和邮箱上所以有误，
#输入账号、密码后加入driver.keyevent(61)就可以了



email='yuan99'+str(random.randint(1000,9000))+'@163.com'
print('email: %s' %email)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)
driver.keyevent(61)
'''
方法1：
问题已解决，Android8.0系统的，
光标定位不到密码和邮箱上，所以有误，
输入账号、密码后，加入driver.keyevent(61)就可以了
'''




'''
方法2：
密码、邮箱报错，导致自动化注册不了的。
只要在send_keys（）之前，加上一个driver.find_elements_by_id（）.click（） 
理解：意思是先点击一下这个输入框，然后再进行输入值？？？
因为用户名输入框，默认是有光标的。
密码和邮箱，默认的focused的值是false，
也就是无光标，所以密码和邮箱输入不进去。
先获取光标，就能正常输入了。 
亲测有效，大家都多交流学习，祝好

是这样？
driver.find_elements_by_id('com.tal.kaoyan:id/activity_register_username_edittext').click.send_keys(email) ？
'''




driver.implicitly_wait(2)

#点击立即注册按钮
print('开始点击立即注册按钮')
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
print('点击注册完毕')


#院校选择
driver.implicitly_wait(2)
print('开始院校选择')
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()

print('院校选择完毕')
#选择省份
#因为id和class都是一样的，所以取id相同的一组，然后按照下标取值
#同样也可以find_elements_by_class这个还没实践过
driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[1].click()

#选择具体院校--同济大学
#因为id和class都是一样的，所以取id相同的一组，然后按照下标取值
driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[1].click()


#专业选择
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()

#选择经济学类-统计学-经济统计学
#因为id和class都是一样的，所以取id相同的一组，然后按照下标取值
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[1].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[2].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[1].click()


#点击“进入考研帮”按钮
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()