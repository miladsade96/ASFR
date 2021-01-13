"""
Generating encode values(vectors) for each image located in imagesAttendance directory
"""

# import statements
from typing import List
import cv2
import face_recognition as fr


def encoder(list_of_images: List) -> List:
    """
    Find encodings for each image located in the given list.
    :param list_of_images: list, all images
    :return: list of encode values
    """
    encodings_list = []     # images encodings will store here
    for img in list_of_images:
        # convert BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodings_list.append(encode)
    return encodings_list
