import numpy as np
import argparse
import glob
import cv2


parser = argparse.ArgumentParser()

parser.add_argument('imgdir',help='image file path')
parser.add_argument('-ti',help = 'image file format',default = '.jpg')
parser.add_argument('-o' ,help = 'output video directory + name',default = 'out')
parser.add_argument('-f' ,help = 'output video frame rate', default = 30)
parser.add_argument('-to',help = 'output video codec', default = '.mp4')


args = parser.parse_args()
imgpath = args.imgdir
imgarr  = []

# File I/O:
images = glob.glob(imgpath+'*'+args.ti)
outname = args.o + args.to

# Codec Specification:
fourcc = {'.mp4': cv2.VideoWriter_fourcc(*'mp4v'), '.avi' : cv2.VideoWriter_fourcc(*'XVID') }

for fname in images:
	img = cv2.imread(fname)

	if len(img.shape) == 2:
		img = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)

	imgarr.append(img)
	h,w,_ = img.shape
	size = (w,h)

out = cv2.VideoWriter(outname,fourcc[args.to], args.f, size)

for i in range(len(imgarr)):
    out.write(imgarr[i])

out.release()

