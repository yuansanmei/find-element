from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


desired_caps={}

desired_caps['automationName']='uiautomator2'
desired_caps['newCommandTimeout']='240'


desired_caps['platformName']='Android'
desired_caps['platformVersion']='9'
#desired_caps['deviceName']='SM-G9508'
desired_caps['deviceName']='988954324349574d45'
desired_caps['udid']='988954324349574d45'



desired_caps['app']=r'/Users/yuansanmei/Desktop/baidu_ditu.apk'
desired_caps['appPackage']='com.baidu.BaiduMap'
desired_caps['appActivity']='com.baidu.baidumaps.WelcomeScreen'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

#安装完毕
#点击同意权限按钮
driver.find_element_by_id('com.baidu.BaiduMap:id/ok_btn').click()

#点击总是允许-是否允许百度地图访问您设备上的照片 媒体内容和文件？
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

#点击立即体验按钮
sleep(5)
#driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.baidu.BaiduMap:id/btn_enter_map")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("立即体验")').click()
#driver.find_element_by_android_uiautomator('com.baidu.BaiduMap:id/btn_enter_map').click()

#点击总是允许-是否允许百度地图获取此设备的位置信息？---前提把定位打开，不然需要去开启GPS定位
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()

#关闭明星语音包录制花絮的弹框按钮
driver.find_element_by_id('com.baidu.BaiduMap:id/guide_close').click()







#点击进入地图按钮
#driver.find_element_by_id('com.baidu.BaiduMap:id/dj2').click()
#点击弹框的退出按钮
#driver.find_element_by_id('com.baidu.BaiduMap:id/byo').click()

x=driver.get_window_size()['width']
y=driver.get_window_size()['height']

def pinch():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    zoom_action=MultiAction(driver)


    action1.press(x=x*0.2,y=y*0.2).wait(1000).move_to(x=x*0.4,y=y*0.4).wait(1000).release()
    action2.press(x=x*0.8,y=y*0.8).wait(1000).move_to(x=x*0.6,y=y*0.6).wait(1000).release()

    print('start pinch...')
    zoom_action.add(action1,action2)
    zoom_action.perform()

def zoom():
    action1=TouchAction(driver)
    action2=TouchAction(driver)
    zoom_action=MultiAction(driver)


    action1.press(x=x*0.4,y=y*0.4).wait(1000).move_to(x=x*0.2,y=y*0.2).wait(1000).release()
    action2.press(x=x*0.6,y=y*0.6).wait(1000).move_to(x=x*0.8,y=y*0.8).wait(1000).release()

    print('start zoom...')
    zoom_action.add(action1,action2)
    zoom_action.perform()

if __name__ == '__main__':
    for i in range(3):
        pinch()

    for i in range(3):
        zoom()