'''
This code is developed from https://github.com/ageitgey/face_recognition 
so have a look on his page 
consider subcribing to my youtube channel
https://www.youtube.com/channel/UCFhPVAGq5K12pgHnKZj-EQA
''''
import face_recognition
import cv2
import numpy as np
from numpy import savetxt
from numpy import loadtxt

# This is a demo of running face recognition on live video from your webcam.
# it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)
#opening all dataset
known_face_encodings = loadtxt('face.npz', delimiter=',')
known_face_names= loadtxt('reg.npz', delimiter=',')
regname=loadtxt('name.npz',dtype=np.str, delimiter=',')
regdept=loadtxt('dept.npz',dtype=np.str, delimiter=',')
regdob=loadtxt('dob.npz',delimiter=',')
#ensure all size are same
print(len(known_face_encodings))
print(len(regname))
print(len(regdept))
print(len(regdob))
print(len(known_face_names))


# Initialize some variables
face_locations = []
face_encodings = []
faceq_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            reg = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]
            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:#getting the index of best match
                print(best_match_index)
                reg=int( known_face_names[best_match_index])#getting regno from dataset
                regnoname=regname[best_match_index]#getting name from dataset
                regnodept=regdept[best_match_index]#getting dept from dataset
                regnodob=regdob[best_match_index]#getting dob from dataset
                regnodob=int(regnodob)
                #printing in serial monitor
                print(reg)
                print(regnoname)
                print(regnodept)
                print(regnodob)

            face_names.append(reg)

    process_this_frame = not process_this_frame


    # Display the results in video frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a reg below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, str(reg), (left, bottom - 6), font, 1.0, (255, 255,255), 1)
        #display details in right side
        cv2.putText(frame, regnoname, (right +6, top), font, 1.0, (127,127,255), 1)
        cv2.putText(frame,str(regnodob), (right + 6, top+30 ), font, 1.0, (127,127,255), 1)
        cv2.putText(frame,regnodept, (right + 6, top+60 ), font, 1.0, (127,127,255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
