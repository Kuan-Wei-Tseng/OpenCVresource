import numpy as np
import argparse
import cv2

parser = argparse.ArgumentParser()

parser.add_argument('viddir',help='video file path')
parser.add_argument('-to',help = 'output image format (.jpg or .bmp)',default = '.jpg')
parser.add_argument('-o' ,help = 'output image directory + prefix',default = 'img')