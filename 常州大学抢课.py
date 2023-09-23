from ast import Bytes, Try
import imghdr
from operator import truediv
from pickle import TRUE
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 设置要抢课的url
url = "http://202.195.102.53/"
url2='http://202.195.102.53/web_xsxk/xfz_xsxk_fs1_zcxk.aspx'

n=input('请输入账号：')
p=input('请输入密码：')

# 设置浏览器启动选项
options = webdriver.Edge()

# 启动浏览器
driver = webdriver.Edge()

# 访问抢课页面
driver.get(url)

# 登录操作
driver.find_element('name', 'username').send_keys(n)
driver.find_element('name', 'userpasd').send_keys(p)
driver.find_element("name","btLogin").click()

driver.get(url2)

a=0

while True:             
    try:
        driver.find_elements(By.CLASS_NAME,'btn.btn-primary.btn-xs')[a].click()
        while True:
            try:
                driver.switch_to.alert.accept()
                #title = driver.switch_to.alert.text
                print('成功')
                a=a+2
            except:
                break 
                #driver.quit()     
    except:
        print('完成')
        time.sleep(2) 