import cv2
face_cascade = cv2.CascadeClassifier()
face_cascade.load('/home/webhead/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')

img = cv2.imread("Me'.jpeg", 1)

cv2.imshow('image', img) 
cv2.waitKey(0)

gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

count = 0

face = face_cascade.detectMultiScale(gr, scaleFactor = 1.05, minNeighbors = 5)
for (x,y,w,h) in face: 
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)   
    cv2.imshow('img',img) 
    cv2.waitKey(1)
    count += 1
cv2.waitKey(1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'No of Faces = {}'.format(count), (0,20), font, 1,(0,0,0),2)
cv2.imshow('img', img)
cv2.waitKey(0)

cv2.destroyAllWindows() 
