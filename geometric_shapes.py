import cv2
import numpy as np

###create a simple black photo
img_black=np.zeros((512,512,3),np.uint8)

#image
img=cv2.imread("red_car.jpg")
img=cv2.resize(img,(512,512))
#draaw line one image
cv2.line(img_black,(10,10),(400,400),(0,255,255),10)
cv2.line(img,(10,10),(400,400),(0,255,255),10)

cv2.rectangle(img_black,(20,40),(200,200),(0,0,255),-1)

cv2.circle(img_black,(200,200),50,(0,255,0),4)

cv2.putText(img_black,"hi",(300,350),cv2.FONT_HERSHEY_COMPLEX,4,(255,0,0),2)
#show the image
cv2.imshow("image_shape",img)
cv2.imshow("black image",img_black)

#waitkey
cv2.waitKey()
cv2.destroyAllWindows()