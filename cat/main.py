import cv2

image=cv2.imread("session28\cat\input\cats.jpg")
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
faces=face_detector.detectMultiScale(image_gray)
for face in faces:
    x,y,w,h=face
    cv2.rectangle(image,[x,y],[x+w,y+h],0,4)
   
cv2.imshow("cats",image)
cv2.imwrite("result.jpg",image)
cv2.waitKey()