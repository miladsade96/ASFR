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
