from splinter.browser import Browser
from time import sleep
import traceback
username = u"13719334988"
passwd = u"Takeabigtrain_1234"
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
date = u"2017-09-30"
start = u"%u6DF1%u5733%u5317%2CIOQ"
end = u"%u8475%u6F6D%2CKTQ"
b.cookies.add({"_jc_save_fromStation": start})
b.cookies.add({"_jc_save_toStation": end})
b.cookies.add({"_jc_save_fromDate": date})
b.reload()
sleep(1)
count = 0
while b.url == ticket_url:
    b.find_by_text(u"查询").click()
    sleep(1)
    b.find_by_text(u"预订")[0].click()
    sleep(1)
    count += 1
    print ("已经为您抢票%d次" %count)
b.find_by_text(u"曾庚涛")[1].click()
b.find_by_text(u"提交订单").click()
