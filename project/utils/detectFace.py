from __future__ import print_function, unicode_literals 
from facepplib import FacePP, exceptions 
import cv2
import tempfile
import os

def detectFace(imageFilename):
    image = cv2.imread(imageFilename)

    face_roi = 0
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = image[y:y + h, x:x + w]
        temp_filename = tempfile.mktemp(suffix='.jpg')
        cv2.imwrite(temp_filename, face_roi)
        print(temp_filename)
        return temp_filename    

def faceComparing(Image1, Image2): 
    
    try:
        api_key ='xQLsTmMyqp1L2MIt7M3l0h-cQiy0Dwhl'
        api_secret ='TyBSGw8NBEP9Tbhv_JbQM18mIlorY6-D'

        # call api 
        app = FacePP(api_key = api_key,  
                        api_secret = api_secret)      

        print() 
        print('-'*30) 
        print('Comparing Photographs......') 
        print('-'*30) 
  
   
        cmp_ = app.compare.get(image_file1 = Image1, 
                               image_file2 = Image2) 
        
        os.remove(Image1)
        os.remove(Image2)
   
        # Comparing Photos 
        if cmp_.confidence > 70: 
            print('Both photographs are of same person......') 
        else: 
            print('Both photographs are of two different persons......')
            
   
    except exceptions.BaseFacePPError as e: 
        print('Error:', e) 


