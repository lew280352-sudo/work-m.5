import cv2 as cv
cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
scale = 1.1
minNeighbor = 3

while True:
    ret, frame = cap.read()
    if ret:   
        gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        face_detect = face_cascade.detectMultiScale(gray_frame,scale,minNeighbor)
        if len(face_detect) > 0 :
            x,y,w,h = face_detect[0]
            
            for(x,y,w,h) in face_detect:
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            cv.imshow('face detect', frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else : 
            print("face dont detected")
    else :
        break


cap.release()
cv.destroyAllWindows()