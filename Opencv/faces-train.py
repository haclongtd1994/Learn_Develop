import cv2  # Lib opencv2
import os   # Lib to process with path of file 
import numpy as np # Lib to process with array and matrix
from PIL import Image # Lib to convert to gray scale
import pickle # Lib to write to file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

current_id=0
label_ids={}

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognize = cv2.face.LBPHFaceRecognizer_create()

y_labels = [] # To store some information label of image_dir
x_train = [] # To store some numpy array to training deep leaning

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("jpg") or file.endswith("png"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            #print(label, path)
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            print(label_ids)
            # y_labels.append("label") # Store labels
            # x_train.append("path") #Store path of image
            pil_image = Image.open(path).convert("L")   # Convert to gray scale
            size = (550, 550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, "uint8")
            #print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
                #print(x_train)
                #print(y_labels)
                
with open("labels.pickle", "wb") as f:
    pickle.dump(label_ids, f)

recognize.train(x_train, np.array(y_labels))
recognize.save("trainner.yml")