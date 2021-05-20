#4-4 Appium元素定位相关操作-id定位的案例操作
#前提app未操作过取消和跳过

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

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

def check_cancelBtn():
    print("check_cancelBtn")
    #捕获异常
    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    #有异常走这个
    except NoSuchElementException:
        print('no CancelBtn')
    #没有异常走这个
    else:
        cancelBtn.click()


def check_skipBtn():
    print("check_skipBtn")
    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()

check_cancelBtn()
check_skipBtn()