from find__element.capability import driver

#匹配所有控件类型=android.widget.EditText且属性=请输入用户名
driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('zxw1234')

#//*匹配所有节点
#中括号是匹配的属性
driver.find_element_by_xpath('//*[@class="android.widget.EditText" and @index="3"]').send_keys('zxw123456')

driver.find_element_by_xpath('//android.widget.Button').click()

# driver.find_element_by_xpath('//*[@class="android.widget.Button"]').click()