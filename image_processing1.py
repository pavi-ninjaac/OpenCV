#import the library
import cv2

######################################################################################## 1
#convert the color image to gray and gray level image to negative image
#cv2.imread(path,flag) in flag 1=colored image; 0=graysclae image ; -1=unchanged image
img_color=cv2.imread('red_car.jpg',1)
img_gray=cv2.imread('red_car.jpg',0)

cv2.imshow("the colored image",img_color)
#you can change the color image to gray using 2 methods
cv2.imshow("the gray color image",img_gray)

#or using the cvtColor method
#img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

#img_gray variable containing the each pixel values as numpy array each value from 0-255
print(img_gray)
print(f"The shape of the image{img_gray.shape}")

#converting to negative image is subracting 255 by each pixel value
img_negative=255-img_gray
cv2.imshow("the negative image",img_negative)
cv2.waitKey(0)

###################################################################################### 2

#here we are extracting each color channel of the image separatly and display them
b=img_color[:,:,0]
g=img_color[:,:,1]
r=img_color[:,:,2]
#display all the conversions
cv2.imshow("the original color image",img_color)
cv2.imshow("Blue color of the image",b)
cv2.imshow("Green channel of the image",g)
cv2.imshow("Red channel of the image",r)
cv2.imshow("Negative of the imge",img_negative)
cv2.imshow("Graysclae of the image",img_gray)
cv2.waitKey(0)
