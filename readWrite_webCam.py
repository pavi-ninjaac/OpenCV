import cv2
#####################Basic program
"""
###set the vediocapture
img=cv2.VideoCapture(0)

#read the image that captured by the web cam
check,frame=img.read()

#check gives it is working fine or not
print(check)

#show the image
cv2.imshow("the",frame)
cv2.waitKey()
print(frame.shape)

#relese the image that will turn off the web camera
img.release()
cv2.destroyAllWindows()
print(check)
"""
#############more advanced capturing the vedio and write it in divice
img=cv2.VideoCapture(0)
fourcc_code=cv2.VideoWriter_fourcc(*"XVID")
vedio=cv2.VideoWriter("my_vedio.mp4",fourcc_code,30,(640,480))
count=0
#loop for continues capture
while(True):
    count+=1
    check,frame=img.read()

    print(frame.shape)
    cv2.imshow("thefirtvedio",frame)

    cv2.imwrite("img"+str(count)+".jpg",frame)
    vedio.write(frame)
    if cv2.waitKey(1)==ord('a'):
        break

vedio.release()
cv2.destroyAllWindows()