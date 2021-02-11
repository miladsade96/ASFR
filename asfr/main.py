# import statements

import os
import cv2
import _csv
import pickle
import numpy as np
from pathlib import Path
from datetime import datetime
import face_recognition as fr
from khayyam import JalaliDate
from typing import Tuple, List
from alive_progress import alive_bar
from concurrent.futures import ProcessPoolExecutor


# defining global variables
user_input = int
images_list = []
known_faces_encodes = []
cl_names = []


def csv_creator():
    """
    Creates a csv file for today attendances.
    :return: None
    """
    Path("../statistics").mkdir(parents=True, exist_ok=True)
    if not os.path.exists(f"../statistics/{str(JalaliDate.today())}.csv"):
        with open(f"../statistics/{str(JalaliDate.today())}.csv", "w") as file:
            file.writelines("Name,Time")
            file.flush()


def csv_reader():
    with open(f"../statistics/{str(JalaliDate.today())}.csv", "r") as file:
        read = _csv.reader(file)
        for row in read:
            print(",".join(row))


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


def image_loader(path="../train_images") -> Tuple[List[str], list]:
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


def attendance_marker(name_of_person: str) -> None:
    """
    Opens the csv file and insert the name and arrive time to file.
    :param name_of_person: str, name of the person whom recognized
                            by the algorithm
    :return: None
    """
    fmt = "%H:%M:%S"    # time format
    with open(f"../statistics/{str(JalaliDate.today())}.csv", "r+") as file:
        my_data_list = file.readlines()
        # declaring two empty lists to store previous records
        names = []
        times = []
        for line in my_data_list[1:]:   # skipping first row(Name,Time)
            line = line.strip()     # skipping new line character
            entry = line.split(",")
            names.append(entry[0])
            times.append(entry[1])
        if name_of_person not in names:
            now = datetime.now()
            date_string = now.strftime(fmt)
            file.writelines(f"\n{name_of_person},{date_string}")
            file.flush()
        else:
            # When name of person previously stored in csv file
            now = datetime.now()
            now_str = datetime.strftime(now, fmt)
            now_time = datetime.strptime(now_str, fmt)
            for name, time in zip(list(reversed(names)), list(reversed(times))):
                if name == name_of_person:
                    latest_time_str = time.strip()
                    latest_time = datetime.strptime(latest_time_str, fmt)
                    delta = (now_time - latest_time).total_seconds()
                    break   # breaks for loop when first wanted record is found
            if delta > 30.0:    # if 30 seconds have elapsed since the last arrival
                file.writelines(f"\n{name_of_person},{now_str}")
                file.flush()


def save_encodings(encodings: List, class_names: List):
    """
    Save encodings into a file.
    :param class_names: class names of images
    :param encodings: list of generated encodings
    :return: None
    """
    # opening data_file and names and pickling to them
    with open("../data/data_file", "wb") as dump:
        dump.write(pickle.dumps(encodings))
        dump.flush()
    with open("../data/names", "wb") as file:
        file.write(pickle.dumps(class_names))
        file.flush()


# ----------------------------------------------------------------------------------


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
                break
            except ValueError:
                print(f"Your entered value is not numeric!")

        if user_input == 1:
            cl_names, images_list = image_loader()
            print("Loading images completed!")
        elif user_input == 2:
            with alive_bar(len(images_list)) as bar, ProcessPoolExecutor() as executor:
                known_faces_encodes = []
                for enc in executor.map(encoder, images_list):
                    bar()
                    known_faces_encodes.append(enc)
            print("Encoding process completed!")
        elif user_input == 3:
            save_encodings(known_faces_encodes, cl_names)
            print("Saving process completed!")
        elif user_input == 4:
            with open("../data/data_file", "rb") as file_1:
                my_data = pickle.loads(file_1.read())
            with open("../data/names", "rb") as file_2:
                unpickled_names = pickle.loads(file_2.read())

            csv_creator()

            # capturing the webcam
            cap = cv2.VideoCapture(0)
            while True:
                _, img = cap.read()   # _: True if the frame is read correctly, otherwise False
                # making small - quarter
                small_image = cv2.resize(img, (0, 0), None, 0.25, 0.25)
                # converting BGR to RGB
                small_image = cv2.cvtColor(small_image, cv2.COLOR_BGR2RGB)
                # finding face locations in the current frame
                faces_in_current_frame = fr.face_locations(small_image)
                # encoding faces that are located in the current frame
                encodings_in_current_frame = fr.face_encodings(small_image, faces_in_current_frame)

                for encode_face, face_location in zip(encodings_in_current_frame, faces_in_current_frame):
                    # comparing faces
                    matches = fr.compare_faces(my_data, encode_face)
                    # calculating the distance
                    face_distance = fr.face_distance(my_data, encode_face)
                    # finding the index of minimum value (correct encoding)
                    index_of_match = np.argmin(face_distance)

                    if matches[index_of_match]:
                        # capitalizing the name of person
                        name = unpickled_names[int(index_of_match)].upper()
                        y_1, x_2, y_2, x_1 = face_location
                        # undoing making small image - Quadruple
                        y_1, x_2, y_2, x_1 = y_1 * 4, x_2 * 4, y_2 * 4, x_1 * 4
                        # image itself, start_point, end_point, color, thickness
                        cv2.rectangle(img, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)
                        # image itself, text string, coordinate of text, font type, font scale, color, thickness
                        cv2.putText(img, name, (x_1 + 6, y_2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (255, 255, 255), 2)
                        # inserting the name and the time to csv file
                        attendance_marker(name)
                    else:
                        # unpacking face location
                        y_1, x_2, y_2, x_1 = face_location
                        # undoing making small image - Quadruple
                        y_1, x_2, y_2, x_1 = y_1 * 4, x_2 * 4, y_2 * 4, x_1 * 4
                        cv2.rectangle(img, (x_1, y_1), (x_2, y_2), (0, 0, 255), 2)
                        cv2.putText(img, "Unknown Face!", (x_1 + 6, y_2 - 6),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                # name of the window, image itself
                cv2.imshow("Webcam", img)
                # display a frame for 1 ms
                cv2.waitKey(1)

        elif user_input == 5:
            print("\n" + "GoodBye!".center(50, "-") + "\n")
            break


if __name__ == '__main__':
    main()
