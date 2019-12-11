# OpenCV Webcam Foundamentals
# OpenCV網路攝影機基礎
import numpy as np
import cv2

# 選擇網路攝影機的位置，對於筆電來說，0是螢幕鏡頭，
# 但是對於Raspberry Pi來說，0代表接上去的第一台相機
cap = cv2.VideoCapture(1)

while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read() # ret回傳的是讀取成功與否

  # 顯示圖片，第一個參數是視窗名稱，第二個參數是影像矩陣
  cv2.imshow('frame', frame)

  # 若按下 q 鍵則離開迴圈，waitKey(1)表示等待1毫秒
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()