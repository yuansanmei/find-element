from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName']='Android'
#三星测试机真机
desired_caps['platformVersion']='9'
desired_caps['deviceName']='SM-G9508'
desired_caps['udid']='988954324349574d45'

desired_caps['app']=r'/Users/yuansanmei/Desktop/kaoyan3.1.0.apk'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

#desired_caps['noReset']='True'
desired_caps['noReset']='False'

#设置手机上的输入法键盘 设置后再修改回去 否则导致调不起本地的输入法
desired_caps['unicodeKeyboard']="True"
desired_caps['resetKeyboard']="True"

#Appium 1.6.3开始支持识别Toast内容，主要是基于UiAutomator2，因此需要在Capablity配置如下参数
desired_caps['automationName']='uiautomator2'


driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(2)

def check_cancelBtn():
    print('check cancelBtn')

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    print('check skipBtn')

    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()

check_cancelBtn()
#check_skipBtn()
#在测试滑动时需要把定义的跳过的方法给忽略掉，不再调用