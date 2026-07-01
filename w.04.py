import cv2 as cv
import numpy as np
img = cv.imread('kurumi.png', 1)
# def click_position(event, x, y, flags, parameter):
#     if event == cv.EVENT_LBUTTONDOWN:
#         blue = img[y, x, 0]
#         green = img[y, x, 1]
#         red = img[y, x, 2]
#         text = f"R:G:B={red},{green},{blue}"
#         cv.putText(img, text, (x, y), cv.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
#         pic2 = np.full((256, 256, 3), (blue, green, red), dtype=np.uint8)
#         cv.imshow("img2", pic2)
#         cv.imshow("img", img)


# cv.imshow("img", img)
# cv.setMouseCallback("img", click_position)
# cv.waitKey(0)
# cv.destroyAllWindows()
#-----------------------------------------------------------------------------------#
# img2 = np.zeros((512,512,3),np.uint8)  
# position = [] 

# def click_position(event, x, y, flags, parameter):
#     if event == cv.EVENT_LBUTTONDOWN:
#         position.append((x,y))
#         cv.circle(img2,(x,y),5,(0,0,255),-1)
#         if len(position) >= 2:
#             
#             cv.line(img2, position[-1], position[-2], (255,0,0), 2) 
#         cv.imshow("pic", img2)

# cv.imshow("pic", img2)


# cv.setMouseCallback("pic", click_position)

# cv.waitKey(0)
# cv.destroyAllWindows()
#-----------------------------------------------------------------------------------# 

drawing = False
start_point = None
end_point = None

def draw_ellipse_callback(event, x, y, flags, param):
    global drawing, start_point, end_point, canvas, temp
 
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        end_point = (x, y)
 
    elif event == cv.EVENT_MOUSEMOVE and drawing:
        end_point = (x, y)
        
      
        temp = canvas.copy()
        
    
        cx = (start_point[0] + end_point[0]) // 2
        cy = (start_point[1] + end_point[1]) // 2
        axes_x = abs(end_point[0] - start_point[0]) // 2
        axes_y = abs(end_point[1] - start_point[1]) // 2
        
     
        if axes_x > 1 or axes_y > 1:
            cv.ellipse(temp, (cx, cy), (axes_x, axes_y), 0, 0, 360, (255, 255, 255), 2)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        if start_point and end_point:
            cx = (start_point[0] + end_point[0]) // 2
            cy = (start_point[1] + end_point[1]) // 2
            center = (cx, cy)
 
            axes_x = abs(end_point[0] - start_point[0]) // 2
            axes_y = abs(end_point[1] - start_point[1]) // 2
 
            if axes_x > 1 or axes_y > 1:
              
                color = tuple(np.random.randint(0, 256, 3).tolist())
                thickness = 6
                cv.ellipse(canvas, center, (axes_x, axes_y), 0, 0, 360, color, thickness)

canvas = np.zeros((512, 512, 3), np.uint8) 
temp = canvas.copy() 

cv.namedWindow("pic")
cv.setMouseCallback("pic", draw_ellipse_callback)

while True:
   
    if drawing:
        cv.imshow("pic", temp)   
    else:
        cv.imshow("pic", canvas) 
    
    key = cv.waitKey(1) & 0xFF
    if key == ord('q') or key == 27: 
        break

cv.destroyAllWindows()