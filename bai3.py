import numpy as np # thay tên
import cv2

cap = cv2.VideoCapture("D:/Nam 1 - He/python/opencv/file.mp4")
num = 0
while True:
    ret, frame = cap.read() # chụp ảnh liên tiếp
    #ret: true/false

    # set up khung hinh
    width = int(cap.get(3))
    height = int(cap.get(4))
    small_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)


    image = np.zeros(frame.shape, np.uint8)
    image[:height//2, :width//2] = small_frame
    # image[height//2:, :width//2] = cv2.rotate(small_frame, cv2.ROTATE_180)
    image[:height//2, width//2:] = cv2.rotate(small_frame, cv2.ROTATE_180)
    # image[height//2:, width//2:] = small_frame
    cv2.imshow("cua so cam", image)
    # cv2.imwrite(f"D:/Nam 1 - He/python/anh/{num}.PNG", frame)
    num += 1
    if cv2.waitKey(1) == ord("s"):
        break
cap.release()
cv2.destroyAllWindows() # dóng các cửa sổ