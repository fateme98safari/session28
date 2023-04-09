import cv2
import numpy as np


footbal_pitch = np.zeros((250, 350), dtype="uint8")
footbal_pitch = cv2.cvtColor(footbal_pitch, cv2.COLOR_BGR2RGB)
footbal_pitch[0:250,0:350]=(1,91,7)
for c in range(0,350,100):
    footbal_pitch[0:250 , c:c+50]=(1,117,8)

cv2.rectangle(footbal_pitch,(10,10),(340,240),(255,255,255),2)
cv2.rectangle(footbal_pitch,(10,64),(70,190),(255,255,255),2)
cv2.rectangle(footbal_pitch,(275,64),(340,190),(255,255,255),2)
cv2.rectangle(footbal_pitch,(10,95),(45,161),(255,255,255),2)
cv2.rectangle(footbal_pitch,(305,95),(340,161),(255,255,255),2)

cv2.line(footbal_pitch,(174,10),(175,240),(255,255,255),2)

cv2.circle(footbal_pitch,(175,125),50,(255,255,255),2)
cv2.circle(footbal_pitch,(175,125),5,(255,255,255),thickness=-1)

cv2.imshow("FootbalPitch", footbal_pitch)
cv2.imwrite("result.jpg",footbal_pitch)
cv2.waitKey()