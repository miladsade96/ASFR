# import statement
import os
from khayyam import JalaliDate


def csv_creator():
    """
    Creates a csv file for today attendances
    :return: None
    """
    if not os.path.exists(f"./statistics/{str(JalaliDate.today())}.csv"):
        with open(f"./statistics/{str(JalaliDate.today())}.csv", "w") as f:
            f.writelines(f"Name, Time")
