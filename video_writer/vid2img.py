import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()

parser.add_argument('viddir',help='video file path')
parser.add_argument('-to',help = 'output image format (.jpg or .bmp)',default = '.jpg')
parser.add_argument('-o' ,help = 'output image directory + prefix',default = 'img/img')

args = parser.parse_args()
vid = cv2.VideoCapture(args.viddir)
cnt = 1

while(True):
    ret, img = vid.read()
    if ret:
        cv2.imwrite(args.o + str(cnt) + args.to,img)
        cnt = cnt + 1
    else:
        break
        
vid.release()