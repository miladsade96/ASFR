# import statements
import numpy as np
import cv2
import face_recognition as fr
import os
import pickle
from datetime import datetime
from typing import Tuple, List
from khayyam import JalaliDate


# defining global variables
today = ""


def image_loader(path: str) -> Tuple[List[str], list]:
    """
    Loading images from given directory
    :param path: str, address of images directory
    :return: list, images class names
    """
    images = []
    class_names = []
    list_of_contents = os.listdir(path)
    for cl in list_of_contents:
        current_image = cv2.imread(f"{path}/{cl}")
        images.append(current_image)
        class_names.append(os.path.splitext(cl)[0])
    return class_names, images


# Encoding process
def find_encodings(list_of_images: list) -> list:
    """
    find encodings for each image located in the given list
    :param list_of_images: list, all images
    :return: list of encode values
    """
    encodings_list = [] # images encodings will store here
    for img in list_of_images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodings_list.append(encode)
    return encodings_list


def save_encodings(encodings: List, class_names: List):
    """
    save encodings into a file
    :param class_names: class names of images
    :param encodings: list of generated encodings
    :return: None
    """
    with open("../data/data_file", "wb") as dump:
        dump.write(pickle.dumps(encodings))

    with open("../data/names", "wb") as f:
        f.write(pickle.dumps(class_names))


def csv_creator():
    """
    Creates a csv file for today attendances
    :return: None
    """
    global today
    today = str(JalaliDate.today())
    if not os.path.exists(f"../statistics/{today}.csv"):
        with open(f"../statistics/{today}.csv", "w") as f:
            f.writelines(f"Name, Time")



def mark_attendance(name_of_person: str) -> None:
    """
    open up the csv file and insert the name and arrive time to file
    :param name_of_person: str, name of the person whom recognized
                            by the algorithm
    :return: None
    """
    with open(f"../statistics/{today}.csv", "r+") as f:
        my_data_list = f.readlines()
        list_of_names = []
        for line in my_data_list:
            entry = line.split(", ")
            list_of_names.append(entry[0])
        if name_of_person not in list_of_names:
            now = datetime.now()
            date_string = now.strftime("%H:%M:%S")
            f.writelines(f"\n{name_of_person}, {date_string}")


global user_input, images_list, known_faces_encodes, cl_names

def main():
    """
    Startup and execution function
    :return: None
    """
    global user_input, images_list, known_faces_encodes, cl_names
    while True:
        print("Attendance system using facial recognition".center(50, "-"))
        print("-" * 50)
        print("\nOptions:\n"
              "1. Loading all images in the given directory\n"
              "2. Encoding all images given in the previous section\n"
              "3. Saving generated encodings and names into files\n"
              "4. Running attendance system\n"
              "5. Exit"
              "\nChoose your option by entering numeric value.")
        # getting user input option
        while True:
            try:
                user_input = int(input("Enter your option:"))
                if 1 > user_input > 4:
                    print(f"There is no valid option to your given value -> {user_input}")
                    continue
                else:
                    break
            except ValueError:
                print(f"Your entered value is not numeric!")


def other():
    """
    The main function to run the program
    :return: None
    """
    path = "../imagesAttendance"
    # calling functions
    cl_names, images_list = image_loader(path)
    known_faces_encodes = find_encodings(images_list)
    print("Encoding finished.")

    save_encodings(known_faces_encodes, cl_names)

    source = open("../data/data_file", "rb").read()
    my_data = pickle.loads(source)
    names = open("../data/names", "rb").read()
    unpickled_names = pickle.loads(names)

    csv_creator()

    # capturing the webcam
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        img_small = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)
        faces_in_current_frame = fr.face_locations(img_small)
        encodings_in_current_frame = fr.face_encodings(img_small, faces_in_current_frame)

        for encodeFaces, faceLoc in zip(encodings_in_current_frame, faces_in_current_frame):
            matches = fr.compare_faces(my_data, encodeFaces)
            faceDistance = fr.face_distance(my_data, encodeFaces)
            matchIndex = np.argmin(faceDistance)

            if matches[matchIndex]:
                name = unpickled_names[int(matchIndex)].upper()
                y_1, x_2, y_2, x_1 = faceLoc
                y_1, x_2, y_2, x_1 = y_1 * 4, x_2 * 4, y_2 * 4, x_1 * 4
                cv2.rectangle(img, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)
                cv2.putText(img, name, (x_1 + 6, y_2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                mark_attendance(name)
        cv2.imshow("Webcam", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
