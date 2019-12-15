import numpy as np
import argparse
import cv2
import os

parser = argparse.ArgumentParser()

parser.add_argument('viddir',help='video file path')
parser.add_argument('-to',help = 'output image format (.jpg or .bmp)',default = '.jpg')
parser.add_argument('-o' ,help = 'output image directory + prefix',default = 'img/img')
parser.add_argument('-v' ,help = 'visualize the process with tqdm.', action ='store_true')

args = parser.parse_args()
vid = cv2.VideoCapture(args.viddir)
cnt = 1

if args.v:
	nof = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
	from tqdm import tqdm
	pbar = tqdm(total=nof)

while(True):
    ret, img = vid.read()
    if ret:
        cv2.imwrite(os.path.join(args.o,str(cnt),args.to,img))
        cnt = cnt + 1
        if args.v:
        	pbar.update(1)
    else:
        break

vid.release()

if args.v:
	pbar.close()

