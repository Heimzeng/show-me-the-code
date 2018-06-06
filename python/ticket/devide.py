import cv2 
import numpy as np
import random
import os
from skimage.morphology import skeletonize
from skimage.filters import threshold_mean
import matplotlib.pyplot as plt
from skimage.util import invert

def makeDirIfItsNotExist(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def checkFileExist(file_path):
    return os.path.isfile(file_path)

if __name__ == '__main__':
    ri = random.randint(0, 9999)
    input_img_rgb = cv2.imread('./data/img/' + str(ri) + '.png', 1)
    makeDirIfItsNotExist('./word/' + str(ri))
    cv2.imwrite('./word/'+ str(ri) + '/' + str(ri) + '.png', input_img_rgb)
    input_img_rgb = input_img_rgb[0:30, 119:230]
    input_img_rgb = cv2.resize(input_img_rgb, (1000, 300))
    cv2.imwrite('./word/' + str(ri) + '/input_img_x4.png', input_img_rgb)
    input_img = cv2.cvtColor(input_img_rgb, cv2.COLOR_BGR2GRAY)

    cv2.imshow('COLOR_BGR2GRAY', input_img)
    cv2.imwrite('./word/' + str(ri) + '/input_img_gray.png', input_img)
    # 1000 x 300 : 33, 7
    binary_img = cv2.adaptiveThreshold(input_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 77, 11)
    #_, binary_img = cv2.threshold(input_img, 200, 255, cv2.THRESH_BINARY)
    cv2.imshow('binary_img', binary_img)
    cv2.imwrite('./word/' + str(ri) + '/binary_img.png', binary_img)
    kernel = np.ones((7,7),np.uint8) 
    kernel0 = np.ones((3,3),np.uint8) 
    kernel0[0][0] = 0
    kernel0[0][2] = 0
    kernel0[2][0] = 0
    kernel0[2][2] = 0
    kernel1 = np.ones((3,3),np.uint8) 
    kernel1[1][0] = 0
    kernel1[1][2] = 0
    kernel1[2][0] = 0
    kernel1[2][1] = 0
    kernel1[2][2] = 0
    kernel2 = np.ones((3,3),np.uint8) 
    kernel2[1][0] = 0
    kernel2[1][2] = 0
    kernel2[2][0] = 0
    kernel2[2][1] = 0
    kernel2[2][2] = 0


    
    erosion = cv2.erode(binary_img,kernel1,iterations = 5)
    cv2.imwrite('./word/' + str(ri) + '/erosion.png', erosion)
    cv2.imshow('erosion', erosion)
    
    image = invert(erosion)
    thresh = threshold_mean(image)
    binary = image > thresh
    skeleton = skeletonize(binary)
    fig, axes = plt.subplots(ncols=2, figsize=(8, 3))
    ax = axes.ravel()
    ax[0].imshow(skeleton, cmap=plt.cm.gray)
    ax[1].imshow(binary, cmap=plt.cm.gray)
    plt.show()

    dilation = cv2.dilate(binary_img,kernel0,iterations = 1)

    cv2.imshow('dilation', dilation)
    cv2.imwrite('dilation.png', dilation)
    
    #closing = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, closekernel)
    #kernel = np.ones((35,35),np.uint8) 
    #opening = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, closekernel)
    #cv2.imshow('open', opening)
    #cv2.imshow('close', closing)
    binary_img = dilation
    _ ,contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
    #_ ,contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
    print (np.size(contours))
    result = input_img_rgb
    count = 0
    for contour in contours:
        rect = cv2.boundingRect(contour)
        if rect[2] * rect[3] > 10:
        #if True:
            x1 = rect[0]
            y1 = rect[1]
            x2 = x1 + rect[2]
            y2 = y1 + rect[3]
            #cv2.line(result, (x1,y1), (x1,y2), (0,255,0), 2)
            #cv2.line(result, (x1,y1), (x2,y1), (0,255,0), 2)
            #cv2.line(result, (x1,y2), (x2,y2), (0,255,0), 2)
            #cv2.line(result, (x2,y1), (x2,y2), (0,255,0), 2)
            rows = rect[3]
            lines = rect[2]
            img = np.zeros((rows, lines), dilation.dtype)
            for i in range(rows):
                for j in range(lines):
                    img[i][j] = dilation[y1+i][x1+j]
            count += 1
            name = './word/' + str(ri) + '/item' + str(count) + '.png'
            cv2.imwrite(name, img)
        count += 1
    cv2.imwrite('./word/' + str(ri) + '/draw.png', result)
    cv2.waitKey()