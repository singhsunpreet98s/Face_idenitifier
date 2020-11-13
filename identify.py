import cv2
faceCascade = cv2.CascadeClassifier("face.xml")
img = cv2.imread("images/portrait.jpg")
while True:
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces =  faceCascade.detectMultiScale(gray_img,scaleFactor=1.2,
                                          minNeighbors=1,
                                          minSize=(50,50))

    for(x,y,w,h) in faces:
        print(x,",",y,",",w,",",h)
        cv2.rectangle(img,(x,y),(w+x,h+y),(0,255,0),1)

    cv2.imshow("identified faces",img)
    if(cv2.waitKey(1)&0xff==ord('q')):
        break
cv2.destroyAllWindows()