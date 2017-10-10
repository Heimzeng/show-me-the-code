#-*- coding: UTF-8 -*- 
from splinter.browser import Browser
from time import sleep
import traceback
import os
f = open('data.txt')
username = f.readline()
passwd = f.readline()
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
b = Browser("chrome")
b.visit(login_url)
b.fill("loginUserDTO.user_name", username)
sleep(2)
b.fill("userDTO.password", passwd)
sleep(2)
print (u"等待验证码，自行输入...")
while True:
    if b.url != initmy_url:
        sleep(1)
    else:
        break
b.visit(ticket_url)
date = u'2017-10-08'
start = u'%u6DF1%u5733%u5317%2CIOQ'
end = u'%u8475%u6F6D%2CKTQ'
temp = start
start = end
end = temp
b.cookies.add({"_jc_save_fromStation": start})
b.cookies.add({"_jc_save_toStation": end})
b.cookies.add({"_jc_save_fromDate": date})
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