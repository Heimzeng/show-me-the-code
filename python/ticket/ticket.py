#-*- coding: UTF-8 -*- 
from splinter.browser import Browser
from time import sleep
import traceback
import os
from PIL import Image
import cv2
from aip import AipImageClassify
from aip import AipOcr
import json
from selenium.webdriver.common.action_chains import ActionChains
import random

def wait(driver):
    while True:
        documentState = driver.execute_script('return document.readyState')
        jQueryState = driver.execute_script('return jQuery.active')
        if documentState == 'complete' and jQueryState == 0:
            sleep(1)
            break
def get9pics(img):

    imgs = []
    imgs.append(img[0:30, 0:230])
    picD = [67, 67]
    start = [41, 5]
    distance = [5, 5]
    for row in range(2):
        for col in range(4):
            beginRow = start[0] + row * picD[0] + row * distance[0]
            endRow = beginRow + picD[0]
            beginCol = start[1] + col * picD[1] + col * distance[1]
            endCol = beginCol + picD[1]
            imgs.append(img[beginRow:endRow, beginCol:endCol])
    return imgs

def clickpics(driver, positions):
    action = ActionChains(driver)
    element = driver.find_element_by_class_name('touclick-image')
    picD = [67, 67]
    start = [41, 5]
    distance = [5, 5]
    for row in range(2):
        for col in range(4):
            if positions[row*4+col]:
                randX = random.randint(1, 67)
                randY = random.randint(1, 67)
                beginRow = start[0] + row * picD[0] + row * distance[0]
                endRow = beginRow + randY
                beginCol = start[1] + col * picD[1] + col * distance[1]
                endCol = beginCol + randX
                action.move_to_element_with_offset(element, endRow, endCol)
                action.click()
                action.perform()

if __name__ == '__main__':
    with open('user.txt', 'r') as userFile:
        username = userFile.readline().strip()
        password = userFile.readline().strip()
    ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
    login_url = "https://kyfw.12306.cn/otn/login/init"
    initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"
    isHeadless = True
    b = Browser("firefox", headless = isHeadless)
    b.visit(login_url)
    b.fill("loginUserDTO.user_name", username)
    b.fill("userDTO.password", password)
    imgElement = b.driver.find_element_by_class_name('touclick-image')
    wait(b.driver)
    sleep(3)
    imgElement.screenshot('./main.png')
    img = cv2.imread('./main.png', 1)
    imgs = get9pics(img)
    for i in range(9):
        cv2.imwrite(str(i)+'.png', imgs[i])
    APP_ID = '11252201'
    API_KEY = 'fyg8xolXs4GibfbbfapGH8b2'
    SECRET_KEY = 'awvwNXxRb78ZrbSs721KbmsosTKMO8hy'
    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
    clientOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    keywords = []
    for i, img in zip(range(9), imgs):
        if i == 0:
            cv2.imwrite('./temp.png', img)
            resultJson = clientOcr.basicAccurate(get_file_content('./temp.png'));
            words = resultJson['words_result'][0]['words']
            words = words.split('的')[1]
            print(words)
        else:
            cv2.imwrite('./temp.png', img)
            resultJson = client.advancedGeneral(get_file_content('./temp.png'));
            result = resultJson['result']
            kn = []
            for d in result:
                kn.append(d['keyword'])
            keywords.append(kn)
    for i in range(8):
        print(str(i)+':', keywords[i])
    res = [False for i in range(8)]
    for i, keyword in zip(range(len(keywords)), keywords):
        keywordall = ''
        for kwi in keyword:
            keywordall = keywordall + kwi
        for c1 in keywordall:
            for c2 in words:
                if c1 == c2:
                    res[i] = True
                    break
    print(res)
    imgElement = b.driver.find_element_by_class_name('touclick-image')
    imgElement.screenshot('./clicked.png')
    clickpics(b.driver, res)
    # b.quit()
    '''
    print (u"等待验证码，自行输入...")
    while True:
        if b.url != initmy_url:
            sleep(1)
        else:
            break
    b.visit(ticket_url)
    date = u'2018-06-22'
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
            #b.find_by_text(u"预订")[32].click()
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