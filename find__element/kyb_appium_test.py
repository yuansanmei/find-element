#前提appium desktop的server服务是启动的
#4-3 第一个Appium脚本
from appium import webdriver

desired_caps={}
desired_caps['platformName']='Android'

#三星测试机真机
desired_caps['platformVersion']='9'
desired_caps['deviceName']='SM-G9508'
desired_caps['udid']='988954324349574d45'

desired_caps['app']=r'/Users/yuansanmei/Desktop/kaoyan3.1.0.apk'

desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)