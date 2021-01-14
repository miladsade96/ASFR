# import statements
import pickle

import cv2
import numpy as np
import face_recognition as fr

from frp.csv import csv_creator
from frp.saver import save_encodings
from frp.loader import image_loader
from frp.encoder import encoder
from frp.marker import attendance_marker


# defining global variables
user_input = int
images_list = []
known_faces_encodes = []
cl_names = []


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
            path = input("Enter path to directory:")
            cl_names, images_list = image_loader(path)
            print("Loading images completed!")
        elif user_input == 2:
            known_faces_encodes = encoder(images_list)
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
                # name of the window, image itself
                cv2.imshow("Webcam", img)
                # display a frame for 1 ms
                cv2.waitKey(1)

        elif user_input == 5:
            print("\n" + "GoodBye!".center(50, "-") + "\n")
            break


if __name__ == '__main__':
    main()
