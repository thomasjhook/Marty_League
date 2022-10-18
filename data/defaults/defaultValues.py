# Deafult Values
from enum import Enum

class Format(Enum):
    NO_CONFIDENCE_VOTE = 1
    CONFIDENCE_VOTE = 2

FIRST_AMOUNT = "$200"
FIRST_AMOUNT_INT = 200
SECOND_AMOUNT = "$80"
SECOND_AMOUNT_INT = 80
THIRD_AMOUNT = "$20"
THIRD_AMOUNT_INT = 20
sender_email = "nflbettingleagueresults@gmail.com"
smtp_server = "smtp.gmail.com"
weeks_path = "../data/2022/Weeks/"
email_path = "email_list.txt"
test_file_path = "./data/Test_Pool/"
smallestDiff = 100
numberOfPayouts = 3