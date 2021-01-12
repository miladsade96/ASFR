# import statements
from datetime import datetime


def attendance_marker(name_of_person: str) -> None:
    """
    opens the csv file and insert the name and arrive time to file
    :param name_of_person: str, name of the person whom recognized
                            by the algorithm
    :return: None
    """
    with open(f"./statistics/{today}.csv", "r+") as f:
        my_data_list = f.readlines()
        list_of_names = []
        for line in my_data_list:
            entry = line.split(", ")
            list_of_names.append(entry[0])
        if name_of_person not in list_of_names:
            now = datetime.now()
            date_string = now.strftime("%H:%M:%S")
            f.writelines(f"\n{name_of_person}, {date_string}")

