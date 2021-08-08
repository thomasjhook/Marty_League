# Deafult Values
from enum import Enum

class Format(Enum):
    NO_CONFIDENCE_VOTE = 1
    CONFIDENCE_VOTE = 2

FIRST_AMOUNT = "$220"
FIRST_AMOUNT_INT = 220
SECOND_AMOUNT = "$100"
SECOND_AMOUNT_INT = 100
THIRD_AMOUNT = "$40"
THIRD_AMOUNT_INT = 40
sender_email = "nflbettingleagueresults@gmail.com"
smtp_server = "smtp.gmail.com"
weeks_path = "./data/2021/Weeks/"
email_path = "email_list.txt"
test_file_path = "./data/Test_Pool/"
smallestDiff = 100
numberOfPayouts = 3