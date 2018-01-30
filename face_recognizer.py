import cv2
import face_recognition
import time

video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
user_image = face_recognition.load_image_file(
    'C:/Users/Effigy/Desktop/in-home-nursing/samples/users1.jpg')
user_image_encoding = face_recognition.face_encodings(user_image)[0]
user_name = 'EFF'

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
name = None

while True:
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Only process every other frame of video to save time
    if process_this_frame:
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(
            small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces(
                [user_image_encoding], face_encoding)
            name = 'Unknown'
            if match[0]:
                name = user_name
            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
