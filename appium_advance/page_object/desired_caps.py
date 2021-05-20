'''这个模块是用来封装appium启动app的'''


from appium import webdriver
import yaml
import logging
import logging.config
import os

# logging.basicConfig(level=logging.INFO,filename='runlog.log',format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
'''定义一个常量，启用log/log.conf的配置文件信息'''
CON_LOG='../log/log.conf'
logging.config.fileConfig(CON_LOG)
'''定义一个采集器'''
logging=logging.getLogger()



'''然后开始把登录封装成一个方法'''
def appium_desired():
    file = open('../yaml/desired_caps.yaml', 'r')
    data = yaml.load(file, Loader=yaml.FullLoader)

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = data['udid']
    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    # desired_caps['noReset']='True'
    desired_caps['noReset'] = data['noReset']
    # 设置手机上的输入法键盘 设置后再修改回去 否则导致调不起本地的输入法
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    # Appium 1.6.3开始支持识别Toast内容，主要是基于UiAutomator2，因此需要在Capablity配置如下参数
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['ip'] = data['ip']
    desired_caps['port'] = data['port']

    logging.info('start app....')
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    # appium_desired()
    '''获取当前模块所在的路径'''
    current_dir = os.path.dirname(__file__)
    print(current_dir)
    '''获取当前目录的父级目录'''
    base_dir = os.path.dirname(os.path.dirname(__file__))
    print(base_dir)
