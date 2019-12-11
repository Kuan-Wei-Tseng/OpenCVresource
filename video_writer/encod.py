import numpy as np
import cv2
import random

dur = 100;
dat = [1,0,1,0,1,0,1,0,1,0,1,0];

counter = 0;

fourcc = cv2.VideoWriter_fourcc(*'XVID')


img_array = []

for i in range(0,dur):
	if i < 6:
		x = 0
		m = cv2.imread('1600/'+str(x)+'.bmp',cv2.IMREAD_GRAYSCALE)		
		curimg = m
	elif (i-6)%6 < 4:
		if dat[counter] is 0: 
			x = 0
			z = cv2.imread('800/'+str(x)+'.bmp',cv2.IMREAD_GRAYSCALE)
			curimg = z
		else:
			#x = random.randint(0,160)
			x = 0
			h = cv2.imread('3200/'+str(x)+'.bmp',cv2.IMREAD_GRAYSCALE)
			curimg = h
	else:
		#x = random.randint(0,160)
		x = 0
		m = cv2.imread('1600/'+str(x)+'.bmp',cv2.IMREAD_GRAYSCALE)		
		curimg = m

	if i >=6 and (i-6)%6 == 5:
		counter = counter + 1

	#cv2.imshow('window',curimg)
	#cv2.waitKey(1)

	cv2.imwrite('VLC/'+str(i)+'.jpg',curimg)

	www = cv2.cvtColor(curimg,cv2.COLOR_GRAY2RGB)

	img_array.append(www)

	h,w = curimg.shape
	size = (w,h)
	if counter > len(dat)-1:
		break;

'''
out = cv2.VideoWriter('VLC.avi',cv2.VideoWriter_fourcc(*'XVID'), 30, size)
for i in range(len(img_array)):
    out.write(img_array[i])

out.release()
'''


