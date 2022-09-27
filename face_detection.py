import cv2                 # Importing the opencv
import pickle
import time
import datetime
from gotoat import gtat

#import the Haar cascades for face and eye detection
def fd(day):
  recognizer = cv2.face.LBPHFaceRecognizer_create()
  recognizer.read("trainner.yml")
  
  labels = {"person_name": 1}
  with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}
  face_cascade = cv2.CascadeClassifier('Haar\haarcascade_frontalcatface.xml')
  #eye_cascade = cv2.CascadeClassifier('Haar\haarcascade_eye.xml')
  
  cap = cv2.VideoCapture(0)
  success = 0
  while True:
      ret, frame = cap.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                    # Convert the Camera to gray
  
      # ---------------------------------- FACE DETECTION ------------------------------------
  
      faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.03, minNeighbors = 5)  # Detect the faces and store the positions
     # eyes = eye_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5) 
     
      for (x, y, w, h) in faces:
          #print(x,y,w,h)                                   # Frames  LOCATION X, Y  WIDTH, HEIGHT
          roi_gray = gray[y: y+h, x: x+w]                 # The Face is isolated and cropped
          roi_color = frame[y: y+h, x: x+w]
          
          idee, conf = recognizer.predict(roi_gray)
          d=day
          n=datetime.datetime.now().time()
          print(n)
          if conf>=55:
             success = 1
             r = labels[idee]
             print(r)
             font = cv2.FONT_HERSHEY_SIMPLEX
             colour = (255, 255, 255)
             stroke = 2
            
          gtat(d,n,r)
          color = (255, 255, 255)
          eye_color = (255, 0, 0)
          stroke = 2
          end_cord_x = x+w
          end_cord_y = y+h
        #  for (ex, ey, ew, eh) in eyes:
         #  end_cord_ex = ex+ew
          # end_cord_ey = ey+eh
          cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
         # cv2.rectangle(frame, (ex, ey), (end_cord_ex, end_cord_ey), eye_color, stroke)
  
      cv2.imshow('Video', frame)         # Show the video
      if cv2.waitKey(20) & success == 1:                           # Quit if the key is Q
        time.sleep(0.8)
        break
  cap.release()
  cv2.destroyAllWindows()
