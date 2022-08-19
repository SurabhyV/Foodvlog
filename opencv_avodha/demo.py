import cv2
path=r'C:\Users\SurabhySarath\PycharmProjects\opencv_avodha\venv\lena.jpg'
image=cv2.imread(path,1)
cv2.imshow('image',image)
cv2.waitKey(10000)
cv2.imwrite('lena.png',image)
cv2.destroyAllWindows()