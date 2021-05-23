from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException
import logging
import logging.config

#相对路径导入desired_caps.yaml文件
file=open('../yaml/desired_caps.yaml','r')
data=yaml.load(file,Loader=yaml.FullLoader)

# logging.basicConfig(level=logging.INFO,filename='runlog.log',format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
#定义一个常量
CON_LOG='logs.conf'
logging.config.fileConfig(CON_LOG)
#定义一个采集器
logging=logging.getLogger()




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


logging.info('start app....')
driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)


def check_cancelBtn():
    logging.info("start check_cancelBtn....")
    #捕获异常
    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')#android:id/button2
    #有异常走这个
    except NoSuchElementException:
        print('no CancelBtn')
    #没有异常走这个
    else:
        cancelBtn.click()


def check_skipBtn():
    logging.info("start check_skipBtn....")
    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()

check_cancelBtn()
check_skipBtn()
