import cv2
import numpy as np
path=r'C:\Users\SurabhySarath\PycharmProjects\opencv_avodha\venv\train.jpeg'
image=cv2.imread(path,1)
blur=cv2.blur(image,(5,5))
gaussian_blur=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("image",image)
cv2.imshow("blur",blur)
cv2.imshow("gaussian",gaussian_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
