# import statement
import os
from khayyam import JalaliDate

# global variables
today = ""

def csv_creator():
    """
    Creates a csv file for today attendances
    :return: None
    """
    global today
    today = str(JalaliDate.today())
    if not os.path.exists(f"./statistics/{today}.csv"):
        with open(f"./statistics/{today}.csv", "w") as f:
            f.writelines(f"Name, Time")
