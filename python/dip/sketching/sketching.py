import numpy as np 
import cv2 
#http://blog.csdn.net/yangtrees/article/details/9115321
#inverse 
def inverse(input_img):
    size = [np.size(input_img,0),np.size(input_img,1)]
    if input_img.ndim == 3:
        size.append(3)
    output_img = np.array(np.zeros(size),input_img.dtype)
    for i in range(size[0]):
        for j in range(size[1]):
            output_img[i,j] = 255 - input_img[i,j]
    return output_img

def added(input_img,img2):
    size = [np.size(input_img,0),np.size(input_img,1)]
    if input_img.ndim == 3:
        size.append(3)
    output_img = np.array(np.zeros(size),input_img.dtype)
    for i in range(size[0]):
        for j in range(size[1]):
            A = int(input_img[i,j])
            B = int(img2[i,j])
            x = A + ((A * B) / (255 - B))
            if x > 255:
                x = 255
            output_img[i,j] = x
    return output_img

def sketching(input_img):
    size = [np.size(input_img,0),np.size(input_img,1)]
    if input_img.ndim == 3:
        size.append(3)
    output_img = cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
    inverse_img = inverse(output_img)
    #http://lib.csdn.net/article/opencv/26910
    blur = cv2.GaussianBlur(inverse_img,(11,11),0)
    b = added(output_img,blur)
    return b

if __name__ == '__main__':
    img = cv2.imread('9.jpg',1)
    #cv2.imshow('origin.png',img)
    output = sketching(img)
    cv2.imshow('output.png',output)
    cv2.imwrite('sketching.png',output)
    cv2.waitKey(0)