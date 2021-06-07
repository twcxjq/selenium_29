# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   selenium_29
# FileName:     se_element
# Author:      TianChangJun
# Datetime:    2021/6/7 14:45
# Description：
# -----------------------------------------------------------------------------------

from selenium import webdriver
import time

try:
    # 实例化浏览器对象:打开了浏览器
    driver = webdriver.Chrome()

    # 打开网址
    driver.get(r"https://www.baidu.com")

    # driver.get(r"http://106.13.199.209:8080/korei/login.jsp")

    # 用id定位百度搜索框，并输入三毛
    # driver.find_element_by_id("kw").send_keys("三毛")

    # 用name定位百度搜索框，并输入四毛
    # driver.find_element_by_name("wd").send_keys("四毛")

    # 用文本定位视频
    # driver.find_element_by_link_text("视频").click()

    # 用模糊文本定位视频
    # driver.find_element_by_partial_link_text("视").click()

    # 样式定位
    # 当class的值为多个单词组合时，例如：mnav.c-font-normal,c-color-t
    # 中间的空格用,或者.或者二者组合来代替，也可以只写一部分
    # ele = driver.find_elements_by_class_name("mnav.c-font-normal,c-color-t")
    # ele[4].click()

    # xpath绝对路径定位搜索框，并输入三毛
    # driver.find_element_by_xpath("html/body/div/div/div[5]/div/div/form/span/input").send_keys("三毛")

    # xpath相对路径定位搜索框，并输入四毛
    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys("四毛")
    # driver.find_element_by_xpath('//input[@id="kw"]').send_keys("五毛")
    # driver.find_element_by_xpath('//input[@id="kw" and @name="wd"]').send_keys("六毛")
    # driver.find_element_by_xpath('//input[@autocomplete="off" and @maxlength="255"]').send_keys("七毛")

    # 模糊属性值定位搜索框
    # driver.find_element_by_xpath('//*[contains(@autocomplete,"o")]').send_keys("八毛")

    # 精确文本定位
    # driver.find_element_by_xpath('//*[text()="视频"]').click()
    # driver.find_element_by_xpath('//a[text()="视频"]').click()

    # 模糊文本值定位
    # driver.find_element_by_xpath('//*[contains(text(),"视")]').click()

    # 起始属性值定位
    # driver.find_element_by_xpath('//*[starts-with(@autocomplete,"of")]').send_keys("九毛")

    # CSS选择器定位百度搜索框
    # driver.find_element_by_css_selector("#kw").send_keys("三毛")
    # driver.find_element_by_css_selector("input#kw").send_keys("四毛")
    # driver.find_element_by_css_selector(".s_ipt").send_keys("六毛")
    # driver.find_element_by_css_selector("input.s_ipt").send_keys("七毛")
    # driver.find_element_by_css_selector('input[id="kw"][name="wd"][autocomplete="off"]').send_keys("八毛")
    # 模糊查询，=前面不能有空格
    # driver.find_element_by_css_selector('input[id^="k"][name$="d"][autocomplete*="of"]').send_keys("九毛")

    # 绝对路径定位
    # driver.find_element_by_css_selector("html>body>div>div>div:nth-child(5)>div>div>form>span>input").send_keys("一块")

    # 相对路径
    # driver.find_element_by_css_selector("#head_wrapper>div>div>form>span>input").send_keys("一块一")

    # 父级定位
    # driver.find_element_by_xpath('//*[@id="form"]/span/input').send_keys("一块二")


    # 用标签定位input元素
    # ele = driver.find_elements_by_tag_name("input")
    # print(type(ele), len(ele))
    # ele[0].send_keys("admin")
    # ele[1].send_keys("123456")

finally:
    # 浏览器睡眠(秒为单位)
    time.sleep(3)
    # 关闭浏览器(单个窗口(第一个窗口))
    # driver.close()
    # 杀死进程
    driver.quit()

