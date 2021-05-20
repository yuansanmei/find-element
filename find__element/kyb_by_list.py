from find__element.capability import driver

#前提条件：账号未登录过，第一次登录且已点击过跳过和升级按钮
#点击注册按钮
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()

#点击头像按钮
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

#按照list定位--图片
#images = driver.find_elements_by_id('com.tal.kaoyan:id/item_image')
#为什么images打印出来是个空数组？
#print(type(images)) #<class 'list'>
#点击选择头像 然后选择images数组下标=10的元素，下标从0开始
#images[0].click()



#点击选择头像,选择下标=1的头像
#把所有ID=com.tal.kaoyan:id/item_image的元素都找出来，然后按下标取值
driver.find_elements_by_id('com.tal.kaoyan:id/item_image')[1].click()
#选择完毕后，点击保存
driver.find_element_by_id('com.tal.kaoyan:id/save').click()