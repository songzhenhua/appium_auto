# coding=utf-8
# @Time  : 2020/6/1
# @Author: 星空物语
# @File  : project_page.py
# @Description: H5-项目页面

from page_object.base_page import BasePage
import logging
import config.config as cf

log = logging.getLogger('szh.ProjectPage')


# H5项目列表页
class ProjectPage(BasePage):
    def __init__(self, driver):
        super(ProjectPage, self).__init__()

    # i=输入框, l=label、说明、显示, b=按钮, m=菜单

    # 查看列表 菜单
    m_view_list = u'xpath,//div[@y-log-id="查看列表"]'
    # 我的任务 菜单
    m_my_task = u'xpath,//div[@y-log-id="我的任务"]'
    # 项目进度 菜单
    m_project_progress = u'xpath,//div[@y-log-id="项目进度"]'

    # -----------------查看列表------------------
    # 添加人员 按钮
    b_add_people = u'xpath,//i[@y-log-id="新增人员"]'
    # 填空输入栏
    i_fill_blank = u'xpath,//input[@placeholder="请输入内容"]'
    # 年月日时分秒输入栏
    i_date_ymdhms = u'xpath,//input[@placeholder="选择日期时间"]'
    # 年月日时分秒此刻
    i_date_ymdhms_now = u'xpath,//span[contains(text(),"此刻")]'
    # 确认添加 按钮
    b_confirm_add = u'xpath,//span[@class="van-button__text"]'
    # 第一个人员
    l_first_people = 'xpath,//tr[2]'
    # 阶段
    l_in_group = u'xpath,//span[.="阶段"]'
    # 第2个请填写
    l_second_nowrite = u'xpath,(//div[.="请填写"])[2]'
    # 第1个已提交
    l_first_committed = u'xpath,//div[.="已提交"]'
    # 单选radio
    b_radio = 'css,.el-radio__original'
    # 多选输入框
    b_multi_choice = u'xpath,//div[.="请下拉选择，可选多个"]'
    # 多选框选项
    l_mchoice_item = 'css,.f-item'
    # 多选框确定按钮
    b_mchoice_ok = 'css,.right-btn'
    # 多行文本
    i_multi_text = 'css,.el-textarea__inner'
    # from提交按钮
    b_commit = u'xpath,//button[@y-log-id="提交"]'  # //button[.="提交"]
    # from提交-2次提交按钮
    b_commit_confirm = u'xpath,//p[.="提交"]'
    # 提交成功信息
    l_commit_success = u'xpath,//div[.="数据提交成功"]'
    # 提交from后 返回 按钮
    b_back = 'css,.van-button__text'

    # -----------------我的任务------------------
    # 我的任务第1个人员
    l_first_missionpeople = u'xpath,//div[.="阶段1-任务1"]'
    # from提交-确认按钮
    b_commit_ok = 'xpath,//button[@class="van-button van-button--default"]'

    # -----------------项目进度------------------
    # 项目进度页填写员完成总数
    l_progress_count = 'xpath,//div[@class="count"]'
    # 查看全部 按钮
    b_look_all = u'xpath,//span[@y-log-id="查看全部"]'
    # 第1个填写员
    l_write = 'css,.fullname'
    # from提交数
    l_group_count = 'xpath,(//div[@class="count"])[2]'
    # 任务from提交数
    l_mission_count = 'xpath,(//div[@class="count"])[5]'

    # 点击‘查看列表’菜单
    def click_view_list(self):
        self.click(self.m_view_list)

    # 点击‘我的任务’菜单
    def click_my_task(self):
        self.click(self.m_my_task)

    # 点击‘项目进度’菜单
    def click_project_progress(self):
        self.click(self.m_project_progress)
        self.sleep(5)

    # 添加人员
    def add_people(self):
        self.click(self.b_add_people)  # 点击添加
        self.type_all(self.i_fill_blank, 'autofill')  # 填写所有填空
        self.click(self.i_date_ymdhms)  # 点击日期
        self.click(self.i_date_ymdhms_now)  # 点击此刻
        self.double_click(self.b_confirm_add)
        self.wait_element(self.l_first_people)  # 等待人员列表展示

    # 填写from并提交
    def _fill_from(self):
        self.double_click_all(self.b_radio)  # 点击所有radio
        self.click(self.b_multi_choice)  # 点击多选框
        self.click_all(self.l_mchoice_item)  # 选择所有多选项
        self.click(self.b_mchoice_ok)  # 点击多选框确定按钮
        self.type_all(self.i_fill_blank, 'autofill')  # 填写所有填空
        self.type(self.i_multi_text, 'auto multi text')  # 填写多行文本
        self.click(self.i_date_ymdhms)  # 点击日期
        self.click(self.i_date_ymdhms_now)  # 点击此刻
        self.click(self.b_commit)  # 点击提交

    # 填写from并提交
    def commit_from(self):
        self.click(self.l_first_people)  # 点击第1个人员
        self.click(self.l_in_group)  # 点击阶段
        self.sleep(2)
        self.click(self.l_second_nowrite)  # 点击第2个请填写
        self._fill_from()
        self.click(self.b_commit_confirm)  # 点击提交确认
        self.wait_element(self.l_commit_success)

    # 打开提交的from
    def open_committed_from(self):
        self.sleep(2)
        self.double_click(self.b_back)  # 点击返回
        self.sleep(2)
        self.click(self.l_in_group)  # 点击阶段
        self.sleep(1)
        self.click(self.l_first_committed)  # 点击第1个已提交

    # 填写任务from并提交
    def commit_missionfrom(self):
        self.click(self.l_first_missionpeople)  # 点击第1个人员
        self._fill_from()
        self.click(self.b_commit_ok)  # 点击提交确认
        self.wait_element(self.l_commit_success)

    # 获取：项目进度页填写员完成总数
    def get_progress_count(self):
        self.wait_element(self.l_progress_count)
        ele = self.get_element(self.l_progress_count)
        return int(ele.text)

    # 获取：统计页填写员完成总数
    def get_statistics_count(self):
        self.click(self.b_look_all)  # 点击 查看全部
        self.sleep(5)
        self.click(self.l_write)  # 点击 第1个填写员
        ele1 = self.get_element(self.l_group_count)  # from提交数
        ele2 = self.get_element(self.l_mission_count)  # 任务from提交数
        return int(ele1.text), int(ele2.text)
