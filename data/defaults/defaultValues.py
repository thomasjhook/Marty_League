# Deafult Values
from enum import Enum

class Format(Enum):
    NO_CONFIDENCE_VOTE = 1
    CONFIDENCE_VOTE = 2

FIRST_AMOUNT = "$250"
FIRST_AMOUNT_INT = 250
SECOND_AMOUNT = "$100"
SECOND_AMOUNT_INT = 100
THIRD_AMOUNT = "$30"
THIRD_AMOUNT_INT = 30
sender_email = "nflbettingleagueresults@gmail.com"
smtp_server = "smtp.gmail.com"
weeks_path = "../data/2022/Weeks/"
email_path = "email_list.txt"
test_file_path = "./data/Test_Pool/"
smallestDiff = 100
numberOfPayouts = 3