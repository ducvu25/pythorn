import cv2
#đọc
img = cv2.imread("D:/Nam 1 - He/python/opencv/1.png", 0)
#1: ảnh màu, 0 đen trắng, -1 có độ trong suốt
#kích thước
# img = cv2.resize(img, (200, 300))
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
#xuất
cv2.imshow("cửa sổ: ", img)
k = cv2.waitKey() #getch
if k == ord("s"):
    #Xoay ảnh 
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite("D:/Nam 1 - He/python/opencv/hello.PNG", img)
