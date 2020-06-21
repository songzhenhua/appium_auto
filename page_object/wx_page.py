# coding=utf-8
# @Time  : 2020/6/1
# @Author: 星空物语
# @File  : wx_page.py
# @Description: 微信native页面

from page_object.base_page import BasePage
import logging
import config.config as cf

log = logging.getLogger('szh.HomePage')


# 微信native
class WXPage(BasePage):
    def __init__(self, driver):
        super(WXPage, self).__init__()

    # i=输入框, l=label、说明、显示, b=按钮, m=菜单

    # 搜索按钮
    b_search = 'id,com.tencent.mm:id/f8y'
    # 搜索输入框
    i_search_input = 'id,com.tencent.mm:id/bhn'
    # 搜索结果公众号
    l_search_result = 'id,com.tencent.mm:id/gbv'
    # 一级菜单
    m_menu_my = 'id,com.tencent.mm:id/alv'
    # 二级菜单
    m_menu_project = 'xpath,/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]'

    # 进入公众号
    def into_yidu(self):
        self.click(self.b_search)
        self.type(self.i_search_input, u"测试工程师小站")
        self.click(self.l_search_result)
        self.screenshot(u'进入公众号')

    # 点击项目
    def click_project(self):
        self.click(self.m_menu_my)
        self.sleep(1)
        self.click(self.m_menu_project)
        self.sleep(2)
        self.switch_to_context('WEBVIEW_com.tencent.mm:tools')
        cf.set_value('project_list_url', self.get_url())  # 将项目主页url保存至全局变量
