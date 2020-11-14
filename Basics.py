# importing relevant libraries
import cv2
import face_recognition

# loading images and converting to RGB
imgElon = face_recognition.load_image_file("imagesBasic/Elon-Musk-normal.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgElonTest = face_recognition.load_image_file("imagesBasic/Elon-Musk-Test.jpg")
imgElonTest = cv2.cvtColor(imgElonTest, cv2.COLOR_BGR2RGB)


# finding faces in images and their encodings
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgElonTest)[0]
encodeElonTest = face_recognition.face_encodings(imgElonTest)[0]
cv2.rectangle(imgElonTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]),
              (255, 0, 255), 2)

# comparing faces
results = face_recognition.compare_faces([encodeElon], encodeElonTest)
# calculating distance
faceDis = face_recognition.face_distance([encodeElon], encodeElonTest)
cv2.putText(imgElonTest, f"{results}, {round(faceDis[0], 2)}", (50, 50),
            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

# showing images
cv2.imshow("Elon Musk", imgElon)
cv2.imshow("Elon Musk Test", imgElonTest)
cv2.waitKey(0)
