# coding=utf-8
# @Time  : 2020/6/1
# @Author: 星空物语
# @File  : run.py
# @Description: 初始化，运行测试，测试收尾

import pytest
import config.config as cf
from util.log import Logger
import argparse
from appium import webdriver
from util.mail import send_mail


def get_args():
    """命令行参数解析"""
    parser = argparse.ArgumentParser(description=u'可选择参数：')
    parser.add_argument('-e', '--environment', choices=['preview', 'product'], default='preview', help=u'测试环境preview，线上环境product')
    args = parser.parse_args()
    if args.environment in ('pre', 'preview'):
        cf.set_value('environment', 'preview')
        cf.set_value('site', 'http://www.baidu.com/')
    elif args.environment in ('pro', 'product'):
        cf.set_value('environment', 'product')
        cf.set_value('site', 'https://www.baidu.com/')
    else:
        print u"请输入preview/product"
        exit()


def set_driver():
    """设置Appium driver"""
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = '63fa4de5'
    desired_caps['appPackage'] = 'com.tencent.mm'
    desired_caps['appActivity'] = '.ui.LauncherUI'
    desired_caps['noReset'] = 'True'  # 不重置app
    # 设置原因：appium识别webview的时候, 把com.tencent.mm:tools的webview识别成com.tencent.mm的webview. 从而导致context切换失败
    desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}
    desired_caps['recreateChromeDriverSessions'] = 'True'
    desired_caps['newCommandTimeout'] = 600
    driver = webdriver.Remote(r'http://localhost:4723/wd/hub', desired_caps)
    # 将driver存入全局变量
    cf.set_value('driver', driver)


def main():
    """运行pytest命令启动测试"""
    pytest.main(['-v', '-s', 'test_case/', '--html=report/report.html', '--self-contained-html'])


if __name__ == '__main__':
    cf.init()  # 初始化全局变量
    # get_args()  # 本测试无需使用命令行参数解析
    log = Logger('szh')  # 初始化log配置
    set_driver()  # 初始化driver
    main()  # 运行pytest测试集
    cf.get_value('driver').quit()  # 关闭appium driver

    # 先将util.mail文件send_mail()中的用户名、密码填写正确，再启用发送邮件功能！！！
    # send_mail(['22459496@qq.com'])  # 将报告发送至邮箱
