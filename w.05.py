import cv2 as cv
import numpy as np

# pic = np.full((512,512,3),(255,255,255),np.uint8) 
# pic2 =np.full((512,512,3),(255,255,255),np.uint8) 
# center = (pic.shape[1]//2,pic.shape[0]//2)   
# cv.circle(pic,center,512//2,(255,0,0),-1)
# cv.rectangle(pic2,(12,12),(500,500),(255,0,0),-1)

# bitwise_and=cv.bitwise_and(pic,pic2)
# cv.imshow("and",bitwise_and)

# bitwise_or=cv.bitwise_or(pic,pic2)
# cv.imshow("or",bitwise_or)

# bitwise_not=cv.bitwise_not(pic)
# cv.imshow("not",bitwise_not)

# bitwise_xor=cv.bitwise_xor(pic,pic2)
# cv.imshow("xor",bitwise_xor)

# cv.imshow("rectangle",pic2)
# cv.imshow("circle",pic)
# cv.waitKey(0)
# cv.destroyAllWindows()

#=====================================================#

# img =cv.imread("test0.1.jpg",1)
# upper_green = np.array([132,255,106])
# lower_green = np.array([0,50,0]) 
# mask = cv.inRange(img,lower_green,upper_green)
# result = cv.bitwise_and(img,img,mask=mask)


# cv.imshow("origin",img)
# cv.imshow("detect color mask",mask)
# cv.imshow("result detect color",result)
# cv.waitKey(0)
# cv.destroyAllWindows()
#======================================================#

lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

lower_yellow = np.array([15, 100, 100])
upper_yellow = np.array([35, 255, 255])

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    green_mask = cv.inRange(frame_hsv, lower_green, upper_green)
    yellow_mask = cv.inRange(frame_hsv, lower_yellow, upper_yellow)
    blue_mask = cv.inRange(frame_hsv, lower_blue, upper_blue)

    result_mask = green_mask | yellow_mask | blue_mask
    result = cv.bitwise_and(frame, frame, mask=result_mask)
       
    cv.imshow("Result", result)         
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()