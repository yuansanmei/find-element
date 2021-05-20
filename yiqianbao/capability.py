from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName']='Android'
#三星测试机真机
desired_caps['platformVersion']='9'
desired_caps['deviceName']='SM-G9508'
desired_caps['udid']='988954324349574d45'

desired_caps['app']=r'/Users/yuansanmei/Desktop/yiqianbao/com.paic.zhifu.wallet.activity_7.6.1_761.apk'
desired_caps['appPackage']='com.paic.zhifu.wallet.activity'
desired_caps['appActivity']='com.paic.zhifu.wallet.activity.myapp.LoadingActivity'

desired_caps['noReset']='True'
#desired_caps['noReset']='False'
desired_caps['unicodeKeyboard']="True"
desired_caps['resetKeyboard']="True"

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(2)

