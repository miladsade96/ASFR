"""Inserting recognized faces to corresponding csv file."""

# import statements
from datetime import datetime
from khayyam import JalaliDate


def attendance_marker(name_of_person: str) -> None:
    """
    Opens the csv file and insert the name and arrive time to file.
    :param name_of_person: str, name of the person whom recognized
                            by the algorithm
    :return: None
    """
    with open(f"../statistics/{str(JalaliDate.today())}.csv", "r+") as file:
        my_data_list = file.readlines()
        list_of_names = []
        for line in my_data_list:
            entry = line.split(", ")
            list_of_names.append(entry[0])
        if name_of_person not in list_of_names:
            now = datetime.now()
            date_string = now.strftime("%H:%M:%S")
            file.writelines(f"\n{name_of_person}, {date_string}")
