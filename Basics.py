# importing relevant libraries
import cv2
import numpy as np
import face_recognition

# loading images and converting to RGB
imgElon = face_recognition.load_image_file("imagesBasic/Elon-Musk-normal.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgElonTest = face_recognition.load_image_file("imagesBasic/Elon-Musk-Test.jpg")
imgElonTest = cv2.cvtColor(imgElonTest, cv2.COLOR_BGR2RGB)

# showing images
cv2.imshow("Elon Musk", imgElon)
cv2.imshow("Elon Musk Test", imgElonTest)
cv2.waitKey(0)
