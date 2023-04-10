import cv2


def lips_detection(image):
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    lips=lip_detector.detectMultiScale(frame_gray,1.3,20)
    sticker=cv2.imread("session28\webcam\input\lips.png")

    for lip in lips:
        x,y,w,h=lip
        sticker=cv2.resize(sticker,[w,h])
        for i in range(h):
            for j in range(w):
                if sticker[i][j][0]==0 and sticker[i][j][1]==0 and sticker[i][j][2]==0:
                    sticker[i][j]=frame[y+i,x+j]
        frame[y:y+h , x:x+w]=sticker
    
    return image   


def eyes_detection(image):
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eyes=eye_detector.detectMultiScale(frame_gray,1.2,10)    
    for (x, y, w, h) in eyes:
        center_coordinates = x + w // 2, y + h // 2
        radius = w // 2 
        cv2.circle(image, center_coordinates, radius, (0, 0, 100), 3)
      
    
    return image 


def chess_face(image):
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_detector.detectMultiScale(frame_gray,1.3)
    for face in faces:
        x,y,w,h=face
        image_face=image[y:y+w,x:x+h]
        image_face_small=cv2.resize(image_face,[20,20])
        image_face_big=cv2.resize(image_face_small,[w,h],interpolation=cv2.INTER_NEAREST)
        image[y:y+w,x:x+h]=image_face_big

    return image

def sticker_on_face(image):
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces_stick=face_stick_detector.detectMultiScale(frame_gray,1.3)
    sticker=cv2.imread("session28\webcam\input\star.png")
    for (x,y,w,h) in faces_stick:
        sticker=cv2.resize(sticker,[w,h])
        for i in range(h):
            for j in range(w):
                if sticker[i][j][0] == 0 and sticker[i][j][1] == 0 and sticker[i][j][2] == 0:
                    sticker[i][j] = image[y+i,x+j]
        frame[y:y+h, x:x+w] = sticker
    

    return image  



def mirror_filter(image):
    col = image.shape[1]
    flipVertical = cv2.flip(image[:,:col//2], 1)
    image[:,col//2:] = flipVertical

    return image

cap=cv2.VideoCapture(0)
face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
lip_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
eye_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
face_stick_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")


while 1==1:
    _,frame=cap.read()
    if cv2.waitKey(25) & 0xFF==ord('1'):
        image=chess_face(frame)
    if cv2.waitKey(25) & 0xFF==ord('2'):
        image=lips_detection(frame)
        image=eyes_detection(frame)
    if cv2.waitKey(25) & 0xFF==ord('3'):
        image=sticker_on_face(frame)
    if cv2.waitKey(25) & 0xFF==ord('4'):
        image=mirror_filter(frame)


    cv2.imshow("result",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
            break
            