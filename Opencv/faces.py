import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognize = cv2.face.LBPHFaceRecognizer_create()
recognize.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    org_label = pickle.load(f)
    print(org_label)
    labels = {v:k for k,v in org_label.items()}
    print(labels)

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
        roi_color = frame[y:y+h, x:x+w]
        
        #reconize ? deep learning model predict keras tensorflow pytourch scikit learn
        id_, conf = recognize.predict(roi_gray)
        if conf>=45:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255,255,255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
        # Using to create image training deep learning
        img_item = "hung_13.png"
        cv2.imwrite(img_item, frame)
        
        color = (255, 0, 0) #BGR
        stroke = 2
        end_cord_x = x+w
        end_cord_y = y+h
        cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)
        
    cv2.imshow('frame', frame)
    #cv2.imshow('gray', gray)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break

# When every thing done, release the capture
cap.release()
cv2.destroyAllWindows()