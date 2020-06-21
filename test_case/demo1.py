# coding=utf-8

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

'''
以下为微信自身H5 demo，测试公众号：测试工程师小站
用例步骤为：打开微信->右上搜索公众号->进入公众号->点击一级菜单->点击二级菜单进入历史文章H5->点击第一个历史消息->点击在看
你应该不能直接运行，因为每个微信版本的元素id是变化的，contexts、handle也有可能变化
'''

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '63fa4de5'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
desired_caps['noReset'] = 'True'
desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:toolsmp'}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
wait=WebDriverWait(driver, 10)
# 打开微信需要一定时间，这里我们用显示等待，等搜索元素出现后再获取，后面代码大家自行根据需要添加
el1 = wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/f8y')))
el1.click()  # 点击搜索公众号
time.sleep(1)
driver.find_element_by_id("com.tencent.mm:id/bhn").send_keys(u"测试")  # 输入名称
driver.find_element_by_id("com.tencent.mm:id/gbv").click()  # 点击公众号
driver.find_element_by_id("com.tencent.mm:id/alv").click()  # 点击一级菜单
# 点击二级菜单
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]")
el2.click()
time.sleep(3)
print(driver.contexts)
driver.switch_to.context('WEBVIEW_com.tencent.mm:toolsmp')

hs = driver.window_handles
print hs
# 每个handle相当于浏览器上的一个Tab标签页
for handle in hs:
    driver.switch_to.window(handle)
    url = driver.current_url
    print url
    # 此时有多个handle，其中那个有以下文字的就是我们想要的
    if u'界面通用测试用例' in driver.page_source:
        break

driver.find_element_by_xpath('//span[@class="weui_media_hd js_media"]').click()  # 点击第一个历史消息

time.sleep(3)
hs = driver.window_handles
print hs
for handle in hs:
    driver.switch_to.window(handle)
    url = driver.current_url
    print url
    # 此时有多个handle，其中那个有以下文字的就是我们想要的
    if u'历史文章推荐阅读' in driver.page_source:
        break

driver.find_element_by_xpath('//button[@id="js_like_btn"]').click()  # 点击在看
