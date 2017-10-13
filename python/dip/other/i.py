import numpy as np 
import cv2 

def get_mask(input_img):
    size = [np.size(input_img,0),np.size(input_img,1)]
    if input_img.ndim == 3:
        size.append(3)
    output_img = np.array(np.zeros(size),input_img.dtype)
    for i in range(size[0]):
        for j in range(size[1]):
            if input_img[i,j].sum()/3 > 220 :
                output_img[i,j] == [0,0,0]
            else :
                output_img[i,j] = input_img[i,j]
    return output_img

def compare(img1,img2):
    size = [np.size(img1,0),np.size(img1,1)]
    if img1.ndim == 3:
        size.append(3)
    output_img = np.array(np.zeros(size),img1.dtype)
    for i in range(size[0]):
        for j in range(size[1]):
            if img1[i,j][0] == img2[i,j][0]:
                output_img[i,j] = [0,0,0]
            else :
                output_img[i,j] = [255,255,255]
                img1[i,j] = [100,100,100]
    return output_img,img1

def process(img1,img2):
    size = [np.size(img1,0),np.size(img1,1)]
    if img1.ndim == 3:
        size.append(3)
    output_img = np.array(np.zeros(size),img1.dtype)
    for i in range(size[0]):
        for j in range(size[1]):
            if img1[i,j][0] == 255:
                sum_red = 0
                sum_green = 0
                sum_blue = 0
                index = 0
                for k in range(-1,1,1):
                    for l in range(-1,1,1):
                        if img1[i+k,j+l][0] == 255:
                            pass
                        else:
                            sum_red += img2[i+k,j+l][0]
                            sum_green += img2[i+k,j+l][1]
                            sum_blue += img2[i+k,j+l][2]
                            index += 1
                output_img[i,j] = [sum_red/index,sum_green/index,sum_blue/index]
            else:
                output_img[i,j] = img2[i,j]
    return output_img

if __name__ == '__main__':
    img = cv2.imread('2.jpg',1)
    ii = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('origin.png',img)
    mask = get_mask(img)
    yy,ll = compare(img,mask)
    kk = cv2.cvtColor(yy,cv2.COLOR_BGR2GRAY)
    output = cv2.inpaint(img, kk, 10.0, cv2.INPAINT_TELEA)
    cv2.imwrite('output.png',output)
    cv2.waitKey(0)