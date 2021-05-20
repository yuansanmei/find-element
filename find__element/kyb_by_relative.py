from find__element.capability import driver

#先点击注册按钮跳转新页面
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()

#再找到父节点存到一个变量里面，然后在这个基础之上再去找；
# 那如果有多个ImageView就定位不到了，只能定位到第一个
# 那如果有多个ImageView后面可以用list
root_element = driver.find_element_by_id('com.tal.kaoyan:id/activity_register_parentlayout')
root_element.find_element_by_class_name('android.widget.ImageView').click()




#需求分析：
#添加图像 class    android.widget.ImageView
#父节点ID   com.tal.kaoyan:id/activity_register_parentlayout
#
#