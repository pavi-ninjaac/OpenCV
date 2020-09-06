import numpy as np
import pywt
import cv2

#read the image
img=cv2.imread('red_car.jpg',0)

#find the size of the image
img_size=img.size
print(img_size)

#First Level Decomposition of 2D-DWT
coeffs = pywt.dwt2(img, 'bior1.3')
cA, (cH, cV, cD) = coeffs

#Second Level Decomposition of 2D-DWT
coeffs2= pywt.dwt2(cA,'bior1.3')
cA2, (cH2,cV2,cD2) =coeffs2
print(cA2)

# Inverse of 2D-DWT Using 2nd Level
idw2=pywt.idwt2(coeffs2, 'bior1.3')
print(idw2.shape)

import matplotlib.pyplot as plt

fig=plt.figure(figsize=(12,4))
for i,a in enumerate([cA,cH,cV,cD]):
    ax=fig.add_subplot(2,2,i+1)
    ax.imshow(a,interpolation='nearest',cmap=plt.cm.gray)
    ax.set_xticks([])
    ax.set_yticks([])
fig.tight_layout()
plt.show()

fig=plt.figure(figsize=(12,4))
for i,a in enumerate([cA2,cH2,cV2,cD2]):
    ax=fig.add_subplot(2,2,i+1)
    ax.imshow(a,interpolation='nearest',cmap=plt.cm.gray)
    ax.set_xticks([])
    ax.set_yticks([])
fig.tight_layout()
plt.show()