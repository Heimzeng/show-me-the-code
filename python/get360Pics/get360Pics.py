import wget
import os
l = ['r', 'l', 'f', 'b', 'd', 'u']
urlbase = 'https://f.expoon.com/sub4/user/Panorama/63/25563/pimgs/183661/1501231673/'
urlexample = 'https://f.expoon.com/sub4/user/Panorama/63/25563/pimgs/183659/1501231176/u/n3/6/u_6_6.jpg'

i = 0
j = 1

while(True):
    url = urlbase + 'f' + '/n3/' + str(i+1) + '/f_' + str(i+1) + '_1.jpg'
    try:
        wget.download(url)
    except:
        print('404 at row ' + str(i+1))
        break
    else:
        i += 1

while(True):
    url = urlbase + 'f' + '/n3/' + '1' + '/f_' + '1' + '_' + str(j+1) + '.jpg'
    try:
        wget.download(url)
    except:
        print('404 at col ' + str(j+1))
        break
    else:
        j += 1


ROW_PIC_NUM = i
COL_PIC_NUM = j

def checkFileExist(file_path):
    return os.path.isfile(file_path)

for i in range(6):
    for r in range(ROW_PIC_NUM):
        for c in range(COL_PIC_NUM):
            filename = l[i] + '_' + str(r+1) + '_' + str(c+1) + '.jpg'
            print('getting ' + filename)
            if not checkFileExist(filename):
                url = urlbase + l[i] + '/n3/' + str(r+1) + '/' + filename
                wget.download(url)
                print('\n')

import cv2
import numpy as np


for i in range(6):
    width = 0
    height = 0
    for r in range(ROW_PIC_NUM):
        filename = l[i] + '_' + str(r+1) + '_' + '1' + '.jpg'
        img = cv2.imread(filename)
        height += np.size(img, 0)
    for c in range(COL_PIC_NUM):
        filename = l[i] + '_' + '1' + '_' + str(c+1) + '.jpg'
        img = cv2.imread(filename)
        width += np.size(img, 1)
    img_mix = np.array(np.zeros([height, width, 3]),img.dtype)
    offsetW = 0
    offsetH = 0
    for r in range(ROW_PIC_NUM):
        offsetH = r * 512
        offsetW = 0
        for c in range(COL_PIC_NUM):
            filename = l[i] + '_' + str(r+1) + '_' + str(c+1) + '.jpg'
            img = cv2.imread(filename)
            size = [np.size(img, 0), np.size(img, 1)]
            for row in range(size[0]):
                for col in range(size[1]):
                    img_mix[offsetH+row][offsetW+col] = img[row][col]
            offsetW += size[1]
    out_file_name = l[i] + '.bmp'
    cv2.imwrite(out_file_name, img_mix)
    print(l[i] + 'finished')