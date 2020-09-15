import cv2
#set the vedio on
img=cv2.VideoCapture(0)

#set the window name and window
cv2.namedWindow('face')

#define the face casecard
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#loop for continues capture
while(True):

    check,frame=img.read()

    gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),

    )

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(w+x,h+y),(0,0,255),3)
        if w>0 and h>0 and x>0 and y>0:
            face_separete = frame[y:(y+h), x:(x+w)]
            cv2.imshow("only_face", face_separete)
    cv2.imshow("face",frame)


    if cv2.waitKey(1)==ord('a'):
        break

img.release()
cv2.destroyAllWindows()