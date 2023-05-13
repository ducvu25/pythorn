import random
import cv2
img = cv2.imread("D:/Nam 1 - He/python/opencv/1.png", 1)
print(TYPE(img))
img = cv2.resize(img, (0, 0), fx = 0.3, fy = 0.3)
#kich thuoc .shape
print(img.shape)
# for i in range(0, 324):
#     for j in range(0, 576):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

#copy vùng chọn
vungchon = img[0 : 100, 100 : 300] 
img[200:300, 200:400] = vungchon
cv2.imshow("man hinh: ", img)
k = cv2.waitKey()
