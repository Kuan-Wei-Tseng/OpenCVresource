# OpenCV Face/Eye Detection
# 基本上從 https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html來
# 包含「臉」以及眼睛的偵測
# 執行方式：打開終端機，輸入 python3 face 然後按Tab再按Enter就會自動跑出來

import numpy as np
import cv2

# 讀取已經訓練好的資料檔，也可以依照他的教程自己訓練分類器
# 這個檔案在opencv的data中，避免路徑上困擾，我單獨把他拉出來放
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# 從檔案讀取影像
img = cv2.imread('people.jpg')
# 將影像由彩色轉成灰階
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gimg, 1.3, 5)

for (x,y,w,h) in faces:
	# 在指定的座標畫長方形
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gimg[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # 眼睛的偵測是在每個臉裡頭去找
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# 顯示影像
cv2.imshow('img',img)
# waitKey一定要寫，0表示按任意鍵繼續，其他數字表示展示出來的時間(毫秒)
cv2.waitKey(0)
cv2.destroyAllWindows()