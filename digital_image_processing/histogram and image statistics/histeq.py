import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('imgpath',help='image file')
parser.add_argument('-method',help = 'Method for histogram eqaulization. You can try: \
normal (default) or CLAHE (contrast limited histogram equalization)',default = 'normal')

args = parser.parse_args()

img = cv2.imread(args.imgpath, cv2.IMREAD_GRAYSCALE)

if args.method is 'normal':
	equ = cv2.equalizeHist(img)
else:
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	equ = clahe.apply(img)

cop = np.hstack((img,equ))
cv2.imshow('histogram equalization', cop)
cv2.waitKey(0)