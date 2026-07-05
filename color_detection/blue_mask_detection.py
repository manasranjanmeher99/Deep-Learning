# blue color detection
import cv2
import numpy as np

cap= cv2.VideoCapture(0)

# lets load the frame and convert it to hsv color space
while True:
    _,frame=cap.read()
    # we convert the frame to hsv
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #blue color detection
    low_blue=np.array([100,150,0])
    high_blue=np.array([140,255,255])

    blue_mask=cv2.inRange(hsv_frame,low_blue,high_blue)
    blue= cv2.bitwise_and(frame,frame,mask=blue_mask)

    #lets frame on the windows
    cv2.imshow("frame",frame)
    cv2.imshow("blue",blue)
    # weight key event whcih is 1 aand which is 27 then break the loop
    key=cv2.waitKey(1)
    if key==27:   #esc button for exit
        break

