"""Generating encode values(vectors) for each image located in imagesAttendance directory."""

# import statements
import cv2
import face_recognition as fr


def encoder(image):
    """
    Find encodings for each image located in the given list.
    :param image: loaded image
    :return: encode value
    """
    # convert BGR to RGB
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encode = fr.face_encodings(img)[0]
    return encode
