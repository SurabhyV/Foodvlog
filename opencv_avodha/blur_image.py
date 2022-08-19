import cv2
import numpy as np
path=r'C:\Users\SurabhySarath\PycharmProjects\opencv_avodha\venv\train.jpeg'
image=cv2.imread(path,1)
matrix=np.ones((5,5),np.float32)/25
new_image=cv2.filter2D(image,-1,matrix)
cv2.imshow("image",image)
cv2.imshow("newimage",new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()