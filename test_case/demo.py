# coding=utf-8

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from page_object.base_page import BasePage

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '63fa4de5'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
desired_caps['noReset'] = 'True'
# 设置原因：appium识别webview的时候, 把com.tencent.mm:tools的webview识别成com.tencent.mm的webview. 从而导致context切换失败
desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}

'''
# 以下为可能用到的desired_caps配置
'automationName': 'Uiautomator2',
'unicodeKeyboard': True,#  使用appium的输入法，支持中文并隐藏键盘
'resetKeyboard': True,#  重置键盘输入法   即自动化后，会还原成原来的输入法
 'app': r'd:\apktoutiao.apk',   #   如果设备上未安装apk，可直接填写所测apk的包名路径
 'newCommandTimeout': 6000    #   设置driver超时时间   appium server(服务端)监听客户端，认为没有连接通信了，就会超时断掉
"recreateChromeDriverSessions", true  # 必须加这句，否则webView和native来回切换会有问题
'''

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

'''
# 以下为使用原始函数，未使用自己封闭函数
wait=WebDriverWait(driver, 1000)
# 打开微信需要一定时间，这里我们用显示等待，等搜索元素出现后再获取，后面代码大家自行根据需要添加
el1 = wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/f4u')))
el1.click()  # 点击搜索
driver.find_element_by_id("com.tencent.mm:id/bfl").send_keys("wxid_o")  # 输入名称
driver.find_element_by_id("com.tencent.mm:id/g8b").click()  # 点击公众号
driver.find_element_by_id("com.tencent.mm:id/akr").click()  # 点击一级菜单
# 点击二级菜单
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]")
el2.click()
'''

bg = BasePage()
bg.click('id,com.tencent.mm:id/f4u')  # 点击搜索
bg.type('id,com.tencent.mm:id/bfl', 'wxid_o')  # 输入wxid_o
bg.click('id,com.tencent.mm:id/g8b')  # 点击公众号
bg.click('id,com.tencent.mm:id/akr')  # 点击菜单
bg.click('xpath,//android.widget.ListView/android.widget.TextView[1]')  # 点击我的项目
time.sleep(5)
print(driver.contexts)
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
bg.click('xpath,//div[@y-log-id="查看列表"]')  # 点击查看列表
time.sleep(6)
