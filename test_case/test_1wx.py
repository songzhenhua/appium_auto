# coding=utf-8
# @Time  : 2020/6/1
# @Author: 星空物语
# @File  : test_1wx.py
# @Description: 微信native测试用例

from page_object.wx_page import WXPage
from page_object.project_page import ProjectPage
import pytest
import config.config as cf
import logging


log = logging.getLogger('szh.TestNative')


class TestWX():
    """
    pytest:
    测试文件以test_开头
    测试类以Test开头，并且不能带有__init__方法
    测试函数以test_开头
    断言使用assert
    """

    driver = cf.get_value('driver')  # 从全局变量取driver
    native_page = WXPage(driver)
    project_page = ProjectPage(driver)

    def test_in_project_list(self):
        """进入项目列表页"""
        try:
            self.native_page.into_yidu()
            self.native_page.click_project()
            assert self.project_page.wait_element(self.project_page.m_view_list)  # 有‘查看列表’element
            log.info(u'断言有‘查看列表’元素 成功')
            self.native_page.screenshot(u'进入H5项目列表页')
        except Exception, e:
            self.native_page.screenshot(u'进入H5项目列表页失败')
            raise e


if __name__ == '__main__':
    # pytest.main(['-v', '-s', 'test_1wx.py::TestHome::test_input_keyword'])
    pytest.main(['-v', '-s'])
