# -*- coding: utf-8 -*-
# @Time     :2019/8/26 上午 10:45
# @Author   :yutq.test
# @Email    :646642124@qq.com
# @File     :class_baidu.com.py
from selenium import webdriver
import time
driver=webdriver.Chrome('C:\chromedriver.exe')
driver.get("https://www.baidu.com")
driver.find_element_by_id('kw').send_keys('华通银行')
time.sleep(3)
driver.find_element_by_id('su').click()
time.sleep(3)
driver.find_element_by_css_selector("[id='1'] a").click()

title=driver.title
if  title== '华通银行_百度搜索':
    print('title=',title)
    time.sleep(4)
    print('成功')
else:
    print('失败')
time.sleep(5)
driver.find_element_by_css_selector(".myheader>p>ul>li:nth-child(5)").click()
driver.quit()
