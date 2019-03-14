#-*- coding: UTF-8 -*- 
from splinter.browser import Browser
from time import sleep
import traceback
import os
f = open('data.txt')
username = f.readline()
passwd = f.readline()
f.close()
ticket_url =  "https://uems.sysu.edu.cn/elect/s/courses?xkjdszid=2017231005001&fromSearch=false&sid=8eb8baa6-fb6b-45c7-be92-6cfbdbe046bc"
login_url = "https://cas.sysu.edu.cn/cas/login?service=http%3A%2F%2Fuems.sysu.edu.cn%2Fjwxt%2Fapi%2Fsso%2Fcas%2Flogin%3Fpattern%3Dstudent-login"
initmy_url = "https://uems.sysu.edu.cn/jwxt/#!/student/index"
b = Browser("chrome")
b.visit(login_url)

print (u"等待验证码，自行输入...")

while True:
    if b.url != initmy_url:
        sleep(1)
    else:
        break

b.find_by_text(u"选课系统（非体育课）").click()

b.find_by_text(u"专选").click()
'''
b.reload()
sleep(1)
count = 0
while b.url == ticket_url:

    if b.find_by_text(u"查询"):
    	b.find_by_text(u"查询").click()
    else:
    	reload()
    	continue
    sleep(3)
    if b.find_by_text(u"预订"):
        b.find_by_text(u"预订")[32].click()
        sleep(5)
        count += 1
        print ("已经为您抢票%d次" %count)
    else:
        b.reload()
        sleep(1)
b.find_by_id(u"normalPassenger_0").click()
b.find_by_id(u"normalPassenger_1").click()
b.find_by_text(u"提交订单").click()
sleep(10)
b.execute_script('$("#qr_submit_id").click()')
#b.find_by_id(u"qr_submit_id").first.click()
'''