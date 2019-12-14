import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()

# Future Work: Graphical User Interface(too many input arguments)

parser.add_argument('-o',help = 'output image directory + name',default = '~/Desktop/pattern')
parser.add_argument('-p',help = 'output pattern size. (Ex:A4)',default = 'A4')
parser.add_argument('-pw',help = 'specify output pattern width(mm)',default = -1)
parser.add_argument('-ph',help = 'specify output pattern height(mm)',default = -1)
parser.add_argument('--h' ,help = 'Draw horizontal ruled line.', action ='store_true')
parser.add_argument('--v' ,help = 'Draw vertical ruled line.', action ='store_true')
parser.add_argument('-rs',help = 'specify distance between each horizontal lines(mm)',default = 5)
parser.add_argument('-cs',help = 'specify distance between each vertical lines(mm)',default = 5)

args = parser.parse_args()

# Future Work: User can specify color.
gray = (200, 200, 200, 255)

# Future Work: Create dictionary from csv file.
dic_siz = {'A4':(297,210),'B5':(250,176)}

if (args.pw is not -1) and (args.ph is not -1):
    M = int(args.sM*10)
    N = int(args.sN*10)
else:
    paper = args.p
    (M,N) = dic_siz[paper]
    M,N = 10*M,10*N

img = np.zeros((M, N, 4))

if args.h:
    s = int(args.rs*10)
    for i in range(0,M,s):
        cv2.line(img,(0,i),(N-1,i),gray,1)

if args.v:
    s = int(args.cs*10)
    for j in range(0,N,s):
        cv2.line(img,(j,0),(j,M-1),gray,1)

cv2.imwrite(args.o+'.png',img)


