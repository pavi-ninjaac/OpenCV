#import the library
import cv2
import numpy as np
from skimage.util import random_noise

#adding nosie to the image
img=cv2.imread('red_car.jpg')
# random_noise() method will convert image in [0, 255] to [0, 1.0],
# inherently it use np.random.normal() to create normal distribution
# and adds the generated noised back to image
img_gaussian= random_noise(img, mode='gaussian', var=0.05**2)
img_gaussian= (255*img_gaussian)

#adding salt and peper noise
img_s_and_p=random_noise(img,mode='s&p')


cv2.imshow("The image with noise of gaussian ",img_gaussian)
cv2.imshow("The image with nice of salt and peper",img_s_and_p)

cv2.waitKey(0)

