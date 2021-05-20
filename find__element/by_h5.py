from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

desired_caps={}
#使用xpath定位元素，报错：selenium.common.exceptions.InvalidArgumentException: Message: invalid argument: invalid locator。
#解决办法：需要在创建driver时增加2个参数。https://blog.csdn.net/m0_38039283/article/details/113430598
#驱动H5自动化关键之一  desired_caps['chromeOptions'] = {'androidProcess': 'com.nuomi'}
desired_caps['chromeOptions'] = {'w3c':'False'}
desired_caps['showChromedriverLog']=True




#谷歌驱动位置，操作H5  "C:\\Program Files (x86)\\Appium\\resources\\app\\node_modules\\appium\\node_modules\\appium-chromedriver\\chromedriver\win\\chromedriver.exe"
desired_caps['chromedriverExecutable']=r'/usr/local/bin/chromedriver'
desired_caps['platformName']='Android'
desired_caps['platformVersion']='9'
desired_caps['deviceName']='988954324349574d45'

desired_caps['app']=r'/Users/yuansanmei/Desktop/dr.fone3.2.0.apk'
desired_caps['appPackage']='com.wondershare.drfone'
#如何获取：aapt dump badging app包地址 |findstr "launchable-activity"
desired_caps['appActivity']='com.wondershare.drfone.ui.activity.WelcomeActivity'




#desired_caps['noReset']='True'
desired_caps['noReset']='False'

#设置手机上的输入法键盘 设置后再修改回去 否则导致调不起本地的输入法
desired_caps['unicodeKeyboard']="True"
desired_caps['resetKeyboard']="True"

#Appium 1.6.3开始支持识别Toast内容，主要是基于UiAutomator2，因此需要在Capablity配置如下参数
desired_caps['automationName']='uiautomator2'







driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)

print('click BackupBtn')
driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

#添加显式等待时间 后面是next按钮的定位ID
#这里需要等待next按钮的出现 等待一会儿，所以加个显示等待
WebDriverWait(driver,30).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
print('click NextBtn')
#然后点击next按钮
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

#整个页面的webview定位classname是android.webkit.WebView
#等待webview的出现，等待30s；然后打印出来contexts #获取目前整个页面的环境
WebDriverWait(driver,30).until(lambda x:x.find_element_by_class_name('android.webkit.WebView'))
contexts=driver.contexts
print(contexts)
#打印结果
#['NATIVE_APP', 'WEBVIEW_com.android.launcher', 'WEBVIEW_com.wondershare.drfone', 'WEBVIEW_com.psiphon3']
##['NATIVE_APP', 'WEBVIEW_com.tencent.mobileqq:mini', 'WEBVIEW_com.wondershare.drfone']


#需android4.4及以上版本的系统中才会输出更多的webview
#开始从原生app切换到WEBVIEW_com.wondershare.drfone这个webview
print('start switch conetext')
driver.switch_to.context('WEBVIEW_com.wondershare.drfone')

#填写邮箱信息 用的是selenium定位那一套
#虽然定位的名字find_element_by_id（定位的是网页的元素）和appium一样（定位的是安卓里面的元素）
#定位的是网页的元素
print('edit email')
driver.find_element_by_id('email').send_keys('sanmei@wondershare.cn')


#开始点击提交按钮
#定位的是网页元素
print('click sendBtn')
driver.find_element_by_class_name('btn_send').click()



#因为要定位要原生的backup返回按钮
#那么一定要先从context切换到原生app  然后点击返回按钮
driver.switch_to.context('NATIVE_APP')
#点击backup前面的返回按钮
driver.find_element_by_class_name('android.widget.ImageButton').click()