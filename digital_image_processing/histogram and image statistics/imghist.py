import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('imgpath',help='image file')

args = parser.parse_args()

img = cv2.imread(args.imgpath, cv2.IMREAD_GRAYSCALE)

print(img)

hist = cv2.calcHist([img], [0], None, [256], [0,256])

plt.figure()
plt.title("Histogram")
plt.xlabel("Intensity")
plt.ylabel("# of pixels")
plt.bar(hist)
plt.xlim([0, 256])
plt.grid()
plt.show()