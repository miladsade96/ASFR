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
