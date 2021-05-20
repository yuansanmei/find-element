from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

#随手记 这个脚本未跑通！！



desired_caps={}

desired_caps['automationName']='uiautomator2'
desired_caps['newCommandTimeout']='240'

desired_caps['platformName']='Android'
desired_caps['platformVersion']='9'
#desired_caps['deviceName']='SM-G9508'
desired_caps['deviceName']='988954324349574d45'
desired_caps['udid']='988954324349574d45'


desired_caps['app']=r'/Users/yuansanmei/Desktop/mymoney.apk'
desired_caps['appPackage']='com.mymoney'
desired_caps['appActivity']='com.mymoney.biz.splash.SplashScreenActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y
#从右边-->向左边滑动
def swipeLeft():
    l=get_size()
    x1=int(l[0]*0.9)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)

#向上滑动
def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)
    y1 = int(l[1] * 0.95)
    y2 = int(l[1] * 0.35)
    driver.swipe(x1,y1,x1,y2,1000)


#安装完毕
#点击总是允许-是否允许随手记访问您设备上的照片 媒体内容和文件？
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

#点击总是允许-是否随手记拨打电话和管理通话？
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()


#等待启动页面元素，然后向左滑动两次,跳过引导页面
#当出现下一步这个按钮时 再滑动，而不是app一启动就开始滑动
WebDriverWait(driver,7).until(lambda x:x.find_element_by_id("com.mymoney:id/next_btn"))
for i in range(2):
    swipeLeft()
    sleep(1)

#滑动2次结束后
#开始点击“开始随手记”按钮
driver.find_element_by_id('com.mymoney:id/begin_btn').click()

#检测是否有活动页面弹窗，如果有就点击关闭
try:
    closeBtn=driver.find_element_by_id('com.mymoney:id/close_iv')
except NoSuchElementException:
    pass
#else就是有就点击 没有就是上面情况
else:
    closeBtn.click()

#点击更多菜单
sleep(3)
driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()
#driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.mymoney:id/nav_setting_btn")').click()
#driver.find_element_by_android_uiautomator('new UiSelector().text("更多")').click()

#很奇怪 selenium.common.exceptions.NoSuchElementException:
# Message: An element could not be located on the page using the given search parameters.



#等待界面菜单加载出来，只要有一个出现就行，然后向上滑动
WebDriverWait(driver,7).until(lambda x:x.find_element_by_id("com.mymoney:id/content_container_ly"))
swipeUp()

#点击高级菜单  appium的name定位在1。5以后废弃了
#那么可以用uiautomater的text是唯一的
driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()
#点击密码与手势密码菜单
driver.find_element_by_id('com.mymoney:id/password_protected_briv').click()
#点击手势密码保护
driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv').click()

#连续滑动两次设置图案密码
for i in range(2):
    TouchAction(driver).press(x=248,y=583).wait(2000).move_to(x=541,y=583).wait(1000).move_to(x=830,y=867).wait(1000).move_to(x=838,y=1159).wait(1000).release().perform()
    #TouchAction(driver).press(x=248,y=583).wait(2000).move_to(x=541,y=583).wait(1000).move_to(x=830,y=867).wait(1000).move_to(x=838,y=1159).release().perform()