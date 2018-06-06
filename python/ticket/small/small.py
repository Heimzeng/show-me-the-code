import cv2 
import numpy as np
import os
if __name__ == '__main__':
    path = './'
    filenames = os.listdir(path)
    for filename in filenames:
        portion = os.path.splitext(filename)
        if portion[1] == '.jpg' or '.png':
            input_img_rgb = cv2.imread(filename, 1)
            input_img = cv2.cvtColor(input_img_rgb, cv2.COLOR_BGR2GRAY)
            binary_img = cv2.adaptiveThreshold(input_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)
            kernel = np.ones((2,2),np.uint8) 
            #cv2.imshow('dilation', dilation)
            erosion = cv2.erode(binary_img,kernel,iterations = 1)
            dilation = cv2.dilate(binary_img,kernel,iterations = 1)
            opening = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)
            cv2.imwrite(filename, dilation)