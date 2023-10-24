"""
This script runs the project application using a development server.
"""

from os import environ
from project import app, db
from flask_migrate import Migrate
from project.service.employeeService import EmployeeService
from project.utils.detectFace import faceComparing
from project.utils.detectFace import detectFace
from project.utils.detectFacialExpression import detectMain

migrate = Migrate(app, db)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)

 

    # image1 = detectFace("D:/CV/CV/anh/iu1.jpg")
    # image2 = detectFace("D:/CV/CV/anh/iu2.jpg")

    # faceComparing(image1, image2)

    # import cv2

    # image = cv2.imread('D:/CV/CV/anh/iu1.jpg')

    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # for (x, y, w, h) in faces:
    #     face_roi = image[y:y + h, x:x + w]

    #     cv2.imwrite('D:/CV/CV/anh/face_image.jpg', face_roi)

    # cv2.imshow('Face Detection', image)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
