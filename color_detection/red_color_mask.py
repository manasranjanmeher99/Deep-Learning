import cv2
import numpy as np

cap= cv2.VideoCapture(0)

# lets load the frame and convert it to hsv color space
while True:
    _,frame=cap.read()
    # we convert the frame to hsv
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #red color detection
    low_red=np.array([161,155,84])
    high_red=np.array([179,255,255])

    red_mask=cv2.inRange(hsv_frame,low_red,high_red)
    red= cv2.bitwise_and(frame,frame,mask=red_mask)

    #lets frame on the windows
    cv2.imshow("frame",frame)
    cv2.imshow("red",red)
    # weight key event whcih is 1 aand which is 27 then break the loop
    key=cv2.waitKey(1)
    if key==27:   #esc button for exit
        break

