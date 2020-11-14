# import statements
import numpy as np
import cv2
import face_recognition as fr
import os

# loading images that has located in imageAttendance directory
path = "imagesAttendance"
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    # current image
    curImg = cv2.imread(f"{path}/{cl}")
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

# Encoding process
def find_encodings(list_of_images):
    encode_list = []
    for img in list_of_images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list

encode_list_known = find_encodings(images)
print("Encoding completed!")


# capturing the webcam
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)
    faces_in_current_frame = fr.face_locations(img_small)
    encodings_in_current_frame = fr.face_encodings(img_small, faces_in_current_frame)

    for encodeFaces, faceLoc in zip(encodings_in_current_frame, faces_in_current_frame):
        matches = fr.compare_faces(encode_list_known, encodeFaces)
        faceDistance = fr.face_distance(encode_list_known, encodeFaces)
        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            name = classNames[int(matchIndex)].upper()
            y_1, x_2, y_2, x_1 = faceLoc
            y_1, x_2, y_2, x_1 = y_1 * 4, x_2 * 4, y_2 * 4, x_1 * 4
            cv2.rectangle(img, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)
            cv2.putText(img, name, (x_1 + 6, y_2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
