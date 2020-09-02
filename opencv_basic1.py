#import the library
import cv2

#check what version you are having
print(cv2.__version__)

#first read and display one image using its path
img=cv2.imread('red_car.jpg')

#images are represented as a multi-dimensional NumPy array with
#shape no. rows (height) x no. columns (width) x no. channels (depth)
h,w,d=img.shape
print(f"height {h}, widht {w}, channel {d}")

#display the image
cv2.imshow("Your image", img)
cv2.waitKey(0) #wait key is used to display the image untill we close the window , other wise it will disapper in few sconds

##########################################################################################
#Accessing each pixels in an image (color or gray channel image)

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB

B,G,R=img[100,50]
print(f" Blue {B}, green {G}, Red {R}")

###########################SLICING THE ROI#################################################
# extracting the Region of Interest (ROI) using the array slicing

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=150,y=60 at ending at x=250,y=160

roi=img[60:160,150:250]
cv2.imshow("The Region of interest ",roi)
cv2.waitKey(0)
# it is in the form of image[startY:endY, startX:endX] because opencv takes the height,width format

#######################RESIGING IMAGES###########################################
# resize the image to 200x200px, ignoring aspect ratio

img_resized=cv2.resize(img,(100,100))
cv2.imshow("the resized image",img_resized)
cv2.waitKey(0)

#while doing like this the image will looking so bad , we have to maitaine the height of the image according to the selected width
#so we are coming to the concept of aspect ratio
#it will maintain the height according to the selected width

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio

r=100.0/w
dim=(100,int(h*r)) #(width,height)
img_resized_aspect=cv2.resize(img, dim)
cv2.imshow("the image resized based on the aspect ratio",img_resized_aspect)
cv2.waitKey(0)
################################################################################