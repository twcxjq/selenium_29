# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   selenium_29
# FileName:     homework_tcj_20210607
# Author:      TianChangJun
# Datetime:    2021/6/7 18:50
# Description：
# -----------------------------------------------------------------------------------

"""
以面向对象的方式：完成科睿的登录，登录之后点击学员管理中的所有学生，最后退出（退出按钮）科睿系统
"""

from selenium import webdriver
import time


class LoginExitSystem:

    def __init__(self, url):
        # 实例化浏览器对象
        self.driver = webdriver.Chrome()
        # 打开科睿系统
        self.driver.get(url)

    def loginSystem(self, user_name, password):
        # 标签定位
        input_element = self.driver.find_elements_by_tag_name("input")
        input_element[0].send_keys(user_name)
        input_element[1].send_keys(password)
        input_element[2].click()

        # self.driver.find_element_by_xpath("html/body/form/div/div/div/div[1]/input").send_keys("admin")
        # self.driver.find_element_by_xpath("html/body/form/div/div/div/div[2]/input").send_keys("1")
        # self.driver.find_element_by_xpath("html/body/form/div/div/div/div[3]/div/input").click()

        self.driver.find_element_by_css_selector("#form-login>div>div>div>a").click()

        time.sleep(3)

        self.driver.find_element_by_id("leftTree_4_span").click()
        # self.driver.find_element_by_css_selector("#leftTree_4_a>span:nth-child(2)").click()

        self.driver.find_element_by_id("leftTree_5_span").click()

    def exitSystem(self):
        self.driver.find_element_by_link_text("退出").click()

    def __del__(self):
        # 浏览器睡眠(秒为单位)
        time.sleep(3)
        self.driver.close()
        # 杀死进程
        # self.driver.quit()     # ImportError: sys.meta_path is None, Python is likely shutting down


if __name__ == '__main__':
    loginExitSystem = LoginExitSystem(r"http://106.13.199.209:8080/korei/login.jsp")
    loginExitSystem.loginSystem("admin", "1")
    loginExitSystem.exitSystem()
