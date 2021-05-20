from time import sleep
from find__element.capability_swipe import driver

#获取屏幕尺寸
def get_size():
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y

#显示屏幕尺寸（width,height）
l=get_size()
print(l)#(1080, 2076)
print(type(l))#<class 'tuple'>

#向左滑动
def swipeLeft():
    l=get_size()
    x1=int(l[0]*0.9)
    y1=int(l[1]*0.5)
    x2=int(l[0]*0.1)
    driver.swipe(x1,y1,x2,y1,1000)#driver调用swipe方法，传参进去

#向左滑动2次
for i in range(2):
    swipeLeft()
    sleep(0.5)

#点击立即体验
driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()