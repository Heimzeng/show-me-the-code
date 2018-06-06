import requests
from PIL import Image
from io import BytesIO
import random
from time import sleep
import os
import cv2

dataPath = './data/'
imgPath = './data/img/'

def getInitI(dirpath):
    return len([name for name in os.listdir(dirpath)])

def getImgs():
    i = getInitI(imgPath)
    while(True):
        if i >= 10000:
            break
        sleep(1)
        filename = imgPath + str(i) + '.png'
        rand = str(random.random())
        img_src = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&' + rand
        response = requests.get(img_src)
        image = Image.open(BytesIO(response.content))
        try:
            image.save(filename)
        except Exception as e:
            print(e)
            continue
        print(i)
        i += 1
def log(number, label):
    with open('./data/log.txt', 'a+') as logFile:
        logFile.write(str(number) + label)

if __name__ == '__main__':
    getImgs()
    for i, filename in zip(range(getInitI(imgPath)), os.listdir(imgPath)):
        img = cv2.imread(imgPath + filename, 1)
        label_block = img[0:30, 0:230]