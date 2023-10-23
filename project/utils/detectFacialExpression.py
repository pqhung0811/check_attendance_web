import sys
import argparse
import re
import cv2
import numpy as np
from keras.models import load_model

def detect_classify_display(frame, model, face_cascade):
    emotions = ['angry', 'disgust', 'fear',
                'happy', 'sad', 'surprise', 'neutral']
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        frame_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    for (x, y, w, h) in faces:
        face = frame_gray[y:y+h, x:x+w]
        face = cv2.resize(face, (48, 48)) / 255
        face = np.expand_dims(face, axis=0)
        face = np.expand_dims(face, axis=-1)
        predictions = model.predict(face)
        pred = np.argmax(predictions)

    return emotions[pred]

def detectMain(filename):
    face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    
    saved_models_path = "project/resource/"
    model_name = "fer2013_simple_CNN_1-e50-a0.64.hdf5"
        
    model = load_model(saved_models_path + model_name)
    
    frame = cv2.imread(filename)
    
    if frame is None:
        print('No captured frame -- Break!')
        return
        
    result = detect_classify_display(frame, model ,face_cascade)
    print(result)
