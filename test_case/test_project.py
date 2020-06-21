# coding=utf-8
# @Time  : 2020/6/1
# @Author: 星空物语
# @File  : test_project.py
# @Description: 项目测试用例

from page_object.wx_page import WXPage
from page_object.project_page import ProjectPage
import pytest
import config.config as cf
import logging

log = logging.getLogger('szh.TestProject')


class TestProject():
    """
    pytest:
    测试文件以test_开头
    测试类以Test开头，并且不能带有__init__方法
    测试函数以test_开头
    断言使用assert
    """

    driver = cf.get_value('driver')  # 从全局变量取driver
    project_page = ProjectPage(driver)

    # -----------------查看列表------------------
    def test_in_project(self):
        """进入项目"""
        try:
            self.project_page.click_view_list()  # 点击 查看列表
            assert self.project_page.wait_element(self.project_page.b_add_people)  # 有‘添加人员’
            log.info(u'断言有‘添加人员’按钮 成功')
            self.project_page.screenshot(u'进入项目')
        except Exception, e:
            self.project_page.screenshot(u'进入项目失败')
            raise e

    def test_add_people(self):
        """添加人员"""
        try:
            self.project_page.add_people()
            assert self.project_page.wait_text('autofill')
            log.info(u'断言页面有‘autofill’人名 成功')
        except Exception, e:
            self.project_page.screenshot(u'添加人员失败')
            raise e

    def test_commit_from(self):
        """提交小组问卷"""
        try:
            self.project_page.commit_from()
            assert self.project_page.wait_text(u'数据提交成功')
        except Exception, e:
            self.project_page.screenshot(u'from提交失败')
            raise e

    def test_open_committed(self):
        """打开提交的问卷"""
        try:
            self.project_page.open_committed_from()
            assert self.project_page.wait_text(u'已提交问卷')
        except Exception, e:
            self.project_page.screenshot(u'打开提交的问卷失败')
            raise e

    # -----------------我的任务------------------
    def test_commit_fromfrom(self):
        """提交问卷"""
        try:
            self.project_page.open(cf.get_value('project_list_url'))  # 跳到项目列表url
            self.project_page.click_my_task()  # 打开我的任务
            self.project_page.commit_from()
            assert self.project_page.wait_text(u'数据提交成功')
        except Exception, e:
            self.project_page.screenshot(u'from提交失败')
            raise e

    # -----------------项目进度------------------
    def test_open_progress(self):
        """打开项目进度"""
        try:
            self.project_page.open(cf.get_value('project_list_url'))  # 跳到项目列表url
            self.project_page.click_project_progress()
            assert self.project_page.get_progress_count() > 0  # 断言填写员完成数>0
            self.project_page.screenshot(u'项目进度统计图')
        except Exception, e:
            self.project_page.screenshot(u'项目进度完成数错误')
            raise e

    def test_people_count(self):
        """填写员提交统计"""
        try:
            n1, n2 = self.project_page.get_statistics_count()
            assert n1 > 0  # 断言小组提交>0
            assert n2 > 0  # 断言提交>0
            self.project_page.screenshot(u'填写员统计')
        except Exception, e:
            self.project_page.screenshot(u'填写员统计数错误')
            raise e


if __name__ == '__main__':
    # pytest.main(['-v', '-s', 'test_1wx.py::TestHome::test_input_keyword'])
    pytest.main(['-v', '-s'])
