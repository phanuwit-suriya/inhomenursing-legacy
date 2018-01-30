import threading
import face_recognition
import cv2

import speech


class FaceRecognizer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        face_cascade = cv2.CascadeClassifier(
            'C:/Users/Effigy/Desktop/in-home-nursing/data/haarcascades/haarcascade_frontalface_default.xml')
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        print('Starting face recognizer')

        video = cv2.VideoCapture(0)

        while True:
            ret, frame = video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            faces = face_cascade.detectMultiScale(
                gray, scaleFactor=1.3, minNeighbors=5)

            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(
                frame, face_locations)
            for face_encoding in face_encodings:
                match = face_recognition.compare_faces(
                    [usesr_image_encoding], face_encoding)
                if match[0]:
                    return True
                else:
                    return False
            # if isinstance(faces, numpy.ndarray):
            #     if process_this_frame:
            #         face_locations = face_recognition.face_locations(
            #             small_frame)
            #         face_encodings = face_recognition.face_encodings(
            #             small_frame, face_locations)
            #         face_names = []
            #         for face_encoding in face_encodings:
            #             match = face_recognition.compare_faces(
            #                 [usesr_image_encoding], face_encoding)
            #             name = 'Unknown'
            #             if match[0]:
            #                 name = user_name
            #             face_names.append(name)

    def save_this_person(self):
        print('What is your name?')
        try:
            # name = speech.recognizer()
            print('Look straigth to the camera')
            return cv2.imwrite('C:/Users/Effigy/Desktop/in-home-nursing/tmp/images/{}.jpg'.format(name))
        except Exception as e:
            print(e)
