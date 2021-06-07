# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   selenium_29
# FileName:     se_one
# Author:      TianChangJun
# Datetime:    2021/6/7 11:57
# Description：
# -----------------------------------------------------------------------------------

from selenium import webdriver

# 实例化浏览器对象: 打开了浏览器
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# 输入网址
driver.get(r"https://www.baidu.com")
