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
                    break
            if delta > 30.0:
                file.writelines(f"\n{name_of_person},{now_str}")
                file.flush()
