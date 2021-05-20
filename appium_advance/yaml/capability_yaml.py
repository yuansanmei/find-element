from appium import webdriver
import yaml

file=open('desired_caps.yaml','r')
data=yaml.load(file,Loader=yaml.FullLoader)

desired_caps={}
desired_caps['platformName']=data['platformName']
desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']
desired_caps['udid']=data['udid']

desired_caps['app']=data['app']
desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']

#desired_caps['noReset']='True'
desired_caps['noReset']=data['noReset']

#设置手机上的输入法键盘 设置后再修改回去 否则导致调不起本地的输入法
desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
desired_caps['resetKeyboard']=data['resetKeyboard']

#Appium 1.6.3开始支持识别Toast内容，主要是基于UiAutomator2，因此需要在Capablity配置如下参数
desired_caps['automationName']='uiautomator2'
desired_caps['ip']=data['ip']
desired_caps['port']=data['port']

driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
driver.implicitly_wait(2)




















