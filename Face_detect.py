import cv2 as cv

scale = 1.1
minNeighbor = 5

cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

def create_dataset(frame,id,frame_id):
    cv.imwrite("data/pic.%s.%s.jpg"%(id,frame_id),frame)

def draw_boundary(frame,text):
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face_detect = face_cascade.detectMultiScale(gray_frame,scale,minNeighbor)
    xywh = []
    for(x,y,w,h) in face_detect:
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv.putText(frame,text,(x-10,y-10),cv.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)
        xywh = [x,y,w,h]
    return frame ,xywh


def detect(frame,frame_id):
    frame,xywh = draw_boundary(frame,"face")
    id = 1 
    if len(xywh)==4 :
        result = frame[xywh[1]:xywh[1]+xywh[3],xywh[0]:xywh[0]+xywh[2]]
        create_dataset(result,id,frame_id)
    return frame    

frame_id=1


while True:
    check,frame = cap.read()
    frame = detect(frame,frame_id)
    frame_id +=1
    cv.imshow("output",frame)
    if cv.waitKey(1) & 0xFF == ord('q') :
        break
    if frame_id ==100:
        break
cap.release()
cv.destroyAllWindows
