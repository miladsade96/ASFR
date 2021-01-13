# import statements
import os
import cv2
from typing import Tuple, List


def image_loader(path: str) -> Tuple[List[str], list]:
    """
    Loading images from given directory.
    :param path: str, address of images directory
    :return: list, images class names
    """
    images = []
    class_names = []
    # Adding list of contents to a list
    list_of_contents = os.listdir(path)
    for cl in list_of_contents:
        current_image = cv2.imread(f"{path}/{cl}")
        images.append(current_image)
        # dropping the file extension
        class_names.append(os.path.splitext(cl)[0])
    return class_names, images
