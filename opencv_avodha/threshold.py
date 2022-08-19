import cv2
path=r'C:\Users\SurabhySarath\PycharmProjects\opencv_avodha\venv\gradient.png'
image = cv2.imread(path,0)
ret,thresh=cv2.threshold(image,60,255,cv2.THRESH_BINARY)
cv2.imshow("image",image)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()