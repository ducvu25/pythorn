from email import header
import cv2

cap = cv2.VideoCapture("D:/Nam 1 - He/python/opencv/file.mp4")
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #Vẽ đường
    #cv2.line(<biến>, (Tọa độ trên), (Tọa độ dưới), (r, g, b), size)
    img = cv2.line(frame, (0, 0), (width, height), (0, 0, 0), 25)
    img = cv2.line(frame, (0, height), (width, 0), (0, 0, 255), 25)
    
    #vẽ HCN
    # cv2.rectangle
    # nếu size = -1 => tô full
    cv2.rectangle(frame, (0, 0), (100, 200), (0, 0, 0), 20)
    
    #vẽ hình tròn
    cv2.circle(frame, (200, 200), 50, (150, 0, 0), -1)
    
    # chèn chữ
    font = cv2.FONT_HERSHEY_TRIPLEX
    img = cv2.putText(frame, "Hello", (100, 200), font, 4, 5)
    cv2.imshow("cua so", frame)
    if cv2.waitKey(1) == ord("s"):
        break
cap.replease()
cv2.destroyAllWindows()