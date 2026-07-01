import cv2 as cv
import numpy as nm
image = cv.imread('kurumi.png',1)
img=cv.resize(image,(607,500))
high , width = img.shape[:2]
center = (width//2,high//2)
# vdo = cv.VideoCapture(0) # VideoCapture = capture video ,0 = webcam, 1 = file

# while(vdo.isOpened()):
#     ret,frame = vdo.read() # read = read video
#     if ret == True:
#         framed = cv.resize(frame,(640,480))
#         frame = cv.resize(frame,fx=0.5,fy=0.5,dsize=(0,0),interpolation=cv.INTER_AREA) #fx = scale x , fy = scale y 
#         cv.imshow("Video",frame)
#         cv.imshow("Video2q",framed)
#         key=cv.waitKey(1)
#         if key == ord('q'): #ord = order
#             break
#     else:
#         break
# vdo.release()
# cv.destroyAllWindows()


# kurumi = cv.imread('kurumi.png',1)
# img_crop = kurumi[150:700,1300:1800] #y_start:y_end,x_start:x_end
# img_rotate = cv.rotate(img_crop,cv.ROTATE_90_COUNTERCLOCKWISE) #ROTATE_180 ,ROTATE_90_CLOCKWISE, ROTATE_90_COUNTERCLOCKWISE
# cv.imshow("og",kurumi)
# cv.imshow("img_crop",img_crop)
# cv.imshow("img_rotate",img_rotate)
# cv.waitKey(0)
# cv.destroyAllWindows()

#---------------------1--------------------------
# Mtx = nm.float32([[1,0,-90],
#                   [0,1,100]])
# result = cv.warpAffine(img,Mtx,(width,high))
# cv.imshow("1",result)
# cv.waitKey(0)
# cv.destroyAllWindows()

#--------------------2--------------------------
# rotate_M=cv.getRotationMatrix2D(center,27,1)
# result = cv.warpAffine(img,rotate_M,(width,high))
# cv.imshow("2",result)
# cv.waitKey(0)
# cv.destroyAllWindows()

#-------------------3---------------------------
# Mtx = nm.float32([[2,0,0],
#                   [0,0.5,0]])
# result = cv.warpAffine(img,Mtx,(width,high))
# cv.imshow("3",result)
# cv.waitKey(0)
# cv.destroyAllWindows()

#------------------4-------------------------
rotate_M = cv.getRotationMatrix2D(center,92,1)

rotated = cv.warpAffine(
    img,
    rotate_M,
    (width,high)
)

Mtx = nm.float32([
    [2,0,100],
    [0,1,0]
])

result = cv.warpAffine(
    rotated,
    Mtx,
    (width,high)
)
cv.imshow("4",result)
cv.waitKey(0)
cv.destroyAllWindows()