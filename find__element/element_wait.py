#注意这里导入的是登录的脚本 所以不需要再写登录部分的代码了。
from find__element.kby_login import driver
from selenium.webdriver.support.ui import WebDriverWait

WebDriverWait(driver,3).until(lambda x:x.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum'))
driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()