# import statements
import cv2
import face_recognition as fr
from typing import List


def find_encodings(list_of_images: List) -> List:
    """
    find encodings for each image located in the given list
    :param list_of_images: list, all images
    :return: list of encode values
    """
    encodings_list = [] # images encodings will store here
    for img in list_of_images:
        # convert BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodings_list.append(encode)
    return encodings_list
