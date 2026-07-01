import cv2 as cv

# img =cv.imread('kurumi.png',1)# imread = analyze image /1 = rgb / 0 = gray-scale /-1 = unchange 

# print(img.shape) # .shape = show data image (high width layer)

# cv.imwrite('coppy.jpg',img) #save image

# cv.imshow('Image',img) # show image in desktop

# cv.waitKey(0) 

# cv.destroyAllWindows 
kurumi = cv.imread('kurumi.png',1)

for i in range(kurumi.shape[0]):
    for j in range(kurumi.shape[1]):
        b=kurumi[i,j,0]
        g =kurumi[i,j,1]
        r = kurumi[i,j,2]
        gray=(b*0.114+0.587*g+0.299*r)
        if gray>=128:
            kurumi[i,j] = [255,255,255]
        else:
            kurumi[i,j] = [0,0,0]
cv.imshow("",kurumi)
cv.waitKey(0)
cv.destroyAllWindows()


