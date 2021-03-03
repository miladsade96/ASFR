# import statements
import eel
from asfr.classes import ASFR

# initializing eel
eel.init("../web")

# creating asfr object
asfr = ASFR()


@eel.expose
def load() -> None:
    """
    Loading images that we are going to encode
    Decorated function (Callable from javascript side)
    :return: None
    """
    # calling image_loader method
    asfr.image_loader()


@eel.expose
def encode() -> None:
    """
    Encoding images
    Decorated function (Callable from javascript side)
    :return: None
    """
    # calling encoder method
    asfr.encoder()


@eel.expose
def save() -> None:
    """
    Saving generated encodes
    Decorated function (Callable from javascript side)
    :return: None
    """
    # calling save method
    asfr.save()


@eel.expose
def recognizer() -> None:
    """
    Opens default camera and starts recognition process
    :return: None
    """
    cap = cv2.VideoCapture(0)

    with open("../data/data_file", "rb") as file_1:
        my_data = pickle.loads(file_1.read())
    with open("../data/names", "rb") as file_2:
        unpickled_names = pickle.loads(file_2.read())

    # creating a csv file
    csv_creator()

    while True:
        _, img = cap.read()  # _: True if the frame is read correctly, otherwise False
        # making small - quarter
        small_image = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        # converting BGR to RGB
        small_image = cv2.cvtColor(small_image, cv2.COLOR_BGR2RGB)
        # finding face locations in the current frame
        faces_in_current_frame = fr.face_locations(small_image)
        # encoding faces that are located in the current frame
        encodings_in_current_frame = fr.face_encodings(
            small_image, faces_in_current_frame)

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

        _, jpeg = cv2.imencode(".jpg", img)
        blob = base64.b64encode(jpeg.tobytes())
        blob = blob.decode("utf-8")
        eel.updateImageSrc(blob)()


@eel.expose
def stop() -> None:
    """
    Stops capturing video
    :return: None
    """
    cv2.destroyAllWindows()


if __name__ == '__main__':
    eel.start("index.html")
