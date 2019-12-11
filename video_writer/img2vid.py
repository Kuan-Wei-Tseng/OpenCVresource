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
parser.add_argument('-v' ,help = 'visualize the process with tqdm.', action ='store_true')

args = parser.parse_args()
imgpath = args.imgdir

# File I/O:
images = glob.glob(imgpath+'*'+args.ti)
outname = args.o + args.to

# Smart Progress Meter:
if args.v:
    nof = len(images)
    from tqdm import tqdm
    pbar = tqdm(total=nof)

# Codec Specification:
fourcc = {'.mp4': cv2.VideoWriter_fourcc(*'mp4v'), '.avi' : cv2.VideoWriter_fourcc(*'XVID') }

s = cv2.imread(images[0]).shape
size = (s[1],s[0])
out = cv2.VideoWriter(outname,fourcc[args.to], args.f, size)

for fname in images:
    img = cv2.imread(fname)

    if len(img.shape) == 2:
        img = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
    if args.v:
        pbar.update(1)	

    out.write(img)

out.release()

