import cv2 as cv
import numpy as np
# pic = np.zeros((512,512,3),np.uint8)                        #create black array 512*512 3 layer 8bit
pic2 = np.full((1024,1024,3),(225,178,102),np.uint8)         #create BGR array 1024*1024 3 layer 8bit
center = (pic2.shape[1]//2,pic2.shape[0]//2)                  #x,y
#cv.line(image,startpoint,endpoint,color,thickness)
#cv.arrowedLine(image,startpoint,endpoint,color,thickness)
#cv.rectangle(image,startpoint,endpoint,color,thickness) thickness -1 = fill
#cv.circle(image,center,radius,color,thickness) thickness -1 = fill
#cv.ellipse(img,center,axis,angle,startAngle,endAngle,color,thickness) thickness -1 = fill
#cv.fillPoly(img,np.array[point1-intfinity],color)
#cv.putText(img,text,startpoint,FONT,scale,color,thickness)

for _ in range(1000):
    x = np.random.randint(-200, 1200)
    y = np.random.randint(-100, 1024)
    radius = np.random.randint(15, 50)

    gray = np.random.randint(60, 181) 
    color = (gray, gray, gray) 
    
    cv.circle(pic2, (x, y), radius, color, -1)

cv.ellipse(pic2,(512,1000),(500,800),0,180,360,(96,96,96),-1)
cv.rectangle(pic2,(410,300),(600,800),(255,153,51),-1)
cv.circle(pic2,(505,295),95,(255,153,51),-1)
cv.ellipse(pic2,(0,1000),(300,600),0,180,360,(51,102,0),-1)
cv.ellipse(pic2,(1023,1000),(300,600),0,180,360,(51,102,0),-1)
cv.ellipse(pic2,(512,1023),(600,300),0,180,360,(76,153,0),-1)
cv.rectangle(pic2,(350,750),(660,900),(255,51,255),-1)
cv.fillPoly(pic2, [np.array([[512, 600], [350, 750], [660, 750]], dtype=np.int32)], (204, 0, 102))
cv.circle(pic2,(512,700),35,(252,193,100),-1)
cv.rectangle(pic2,(395,785),(455,830),(252,193,100),-1)
cv.rectangle(pic2,(555,785),(615,830),(252,193,100),-1)
cv.rectangle(pic2,(482,850),(512,900),(0,51,102),-1)
cv.rectangle(pic2,(520,850),(550,900),(0,51,102),-1)
np.random.seed()

for _ in range(1500):

    x = np.random.randint(-200, 1200)

    y = np.random.randint(-100, 1024)

    length = np.random.randint(15, 50)

    cv.line(pic2, (x, y), (x - int(length * 0.4), y + length), (180, 180, 180), 1)


cv.imshow("picture",pic2)
cv.waitKey(0)
cv.destroyAllWindows()
#----------------------------------2-----------------------------------------------#
# import cv2
# import datetime

# # 1. เปิดกล้องเว็บแคม (0 คือกล้องหลักของเครื่อง)
# cap = cv2.VideoCapture(0)

# while True:
#     # อ่านเฟรมจากกล้อง
#     ret, frame = cap.read()

#     # ดึงขนาดของวิดีโอ (ความสูง, ความกว้าง)
#     height, width, _ = frame.shape

#     # หาจุดกึ่งกลางของภาพ
#     center_x = width // 2
#     center_y = height // 2

#     # 2. วาดวงกลมสีเขียวที่ตำแหน่งกึ่งกลาง รัศมี 50 pixels (ความหนาเส้น = 3)
#     # สีเขียวใน BGR คือ (0, 255, 0)
#     cv2.circle(frame, (center_x, center_y), 50, (0, 255, 0), 3)

#     # 3. วาดสี่เหลี่ยมผืนผ้าสีฟ้ารอบขอบภาพ ขนาดขอบ 20 pixels
#     # สีฟ้า/น้ำเงินอ่อนใน BGR เช่น (255, 255, 0) คือสีฟ้า Cyan
#     cv2.rectangle(frame, (0, 0), (width, height), (255, 255, 0), 20)

#     # 4. วาดเส้นทแยงมุมสีแดงจากมุมบนซ้ายไปยังมุมล่างขวา (ความหนาเส้น = 3)
#     # สีแดงใน BGR คือ (0, 0, 255)
#     cv2.line(frame, (0, 0), (width, height), (0, 0, 255), 3)

#     # ดึงเวลาปัจจุบันในรูปแบบ ชั่วโมง:นาที:วินาที
#     current_time = datetime.datetime.now().strftime("%H:%M:%S")
#     text = f"Live Video : {current_time}"

#     # 5. ใส่ข้อความที่มุมบนซ้ายของวิดีโอ (ขยับพิกัดลงมาเล็กน้อยเพื่อไม่ให้ทับขอบ 20px)
#     # ใช้สีขาว (255, 255, 255) เพื่อให้เห็นชัดเจน
#     cv2.putText(frame, text, (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#     # แสดงผลวิดีโอในหน้าต่างชื่อ "Webcam Object Drawing"
#     cv2.imshow('Webcam Object Drawing', frame)

#     # กดปุ่ม 'q' บนคีย์บอร์ดเพื่อออกจากโปรแกรม
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # คืนค่าทรัพยากรให้กับระบบเมื่อเลิกใช้งาน
# cap.release()
# cv2.destroyAllWindows()