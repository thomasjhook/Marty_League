# Program to calculate number of correct picks on Sunday

import json
from colorama import init, Fore, Style
import smtplib, ssl
init()

FIRST_AMOUNT = "$220"
FIRST_AMOUNT_INT = 220
SECOND_AMOUNT = "$100"
SECOND_AMOUNT_INT = 100
THIRD_AMOUNT = "$40"
THIRD_AMOUNT_INT = 40
sender_email = "nflbettingleagueresults@gmail.com"
smtp_server = "smtp.gmail.com"

def main(inFile, verbose):

    # Dict to hold answers read in from txt file
    # {<name> : [pick1,pick2,...,pick10]}
    answers = buildAnswersDict(inFile)

    # Dict to hold number of correct answers per participant
    # {<name> : <numCorrectAnswers>}
    results = buildResultsDict(answers)
    
        
    displayWinners(answers)

    # Extra logging if parameter is True. I need to add some more verbose functionality
    if verbose:
        displayParticipantsPicks(answers)
            
    # Output results of the week which includes all the participants correct picks along
    # with the winners of 1ST, 2ND and 3RD place. This function also builds the body of the email to be sent
    # which contains the same information
    resultString = buildResultsString(results, answers)

    print("###########################")
    print("RESULTS")
    print("###########################\n")

    # Obtain user input to decide if results should be emailed or not
    print(Style.RESET_ALL)
    emailResults = input("Would you like to email the results? (y/n)")
    while emailResults != "y" and emailResults != "Y" and emailResults != "n" and emailResults != "N":
        print("Come on Tom, enter a valid response (y/n)")
        emailResults = input("Would you like to email the results? (y/n)")

    # Email the results
    if emailResults == "y" or emailResults == "Y":
        emailList = generateEmailList()
        subjectLine = inFile
        port = 465  # For SSL
        password = input("Type your password and press enter: ")
        message = f"""\
        Subject: {subjectLine}

        This message is sent from Python.
        
        {resultString}"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            for receiver_email in emailList:
                server.sendmail(sender_email, receiver_email, message)

# This function builds the body of the email to be sent that contains the correct picks for the
# participants along with 1ST, 2ND and 3RD place winners
def buildResultsString(results, answers):
    resultString = ""

    # Portion of the email that contains the number of correct picks for each participant
    resultString = displayResults(results)

    # Portion of the email that contains the winners of 1ST, 2ND and 3RD place
    resultString = resultString + calculateAndDisplayWinner(results, answers)

    return resultString

# This function returns a list of emails from a text file
def generateEmailList():
    inFile = open("email_list.txt")
    
    
    for line in inFile:
        line = line.strip()
        line = line.split(",")
        return line


# This function takes a dictionary (answersDict) with one of the keys being equal to "answer". It
# will print the value stored in the answersDict["answer"] slot, which is a list of the winners
# between two teams for the week.
def displayWinners(answersDict):
    winnersString = buildPickString(answersDict["answer"])
    print("Winning teams this week: ", winnersString)


# This function takes a dictionary (resultsDict) and simply prints the key:value pair to display
# the results of everyones correct picks
def displayResults(resultsDict):
    resultString = ""
    for y in resultsDict:
        print(y, resultsDict[y])
        resultString = resultString + y + ": " + str(resultsDict[y]) + "\n"
    print()

    return resultString


# This function takes a dictionary (answersDict) and displays everyones picks for the week. It will
# exclude the "answer" key and will only be called if Verbose logging is on
def displayParticipantsPicks(answersDict):
    for x in answersDict:
        if x != "answer":
            answerStr = buildPickString(answersDict[x])
            print(x, ":", answerStr)


# Helper function to return a string of values seperated by a comma and space, given a list.
def buildPickString(answerList):
    pickStr = ""
    for x in answerList:
        pickStr = pickStr + x + ", "

    return pickStr


# This function builds up and returns a dictionary representing everyone's picks for the weeks.
# It basically takes what is on the text file and transfers it to an internal data member so it
# can be used by the rest of the program
def buildAnswersDict(inFile):
    answers = {}
    inFile = open(inFile)
    
    # Build up internal data structure based on file
    for line in inFile:
        line = line.strip()
        line = line.split(",")
        
        # Inserts a value into the dictionary
        # keyed by the name of the participant
        # with a value of their picks 
        answers[line[0]] = line[1:]
    
    return answers


# This function takes a dictionary (answers) and iterates through to compare everyone's picks to the
# correct picks. This is the real meat of the program
def buildResultsDict(answers):
    results = {}
    
    # Iterate through internal data structure (answers) and compare
    # the participant answer to the answer key to and store result in
    # another internal data structure (results)
    for x in answers:
        numCorrect = 0
        counter = 0
        if x != "answer" and x != "numGames":
            for answer in answers[x]:
                # Actual comparison to check participant x's
                # answers against the answer key's answers
                if (answer.lower() == answers["answer"][counter].lower()) and counter < int(answers["numGames"][0]):
                    numCorrect = numCorrect + 1
                
                counter = counter + 1
            results[x] = numCorrect
    return results

def calculateAndDisplayWinner(resultsDict, answersDict):
    localCount = 0
    resultString = ""
    sameTieBreakerScore = False
    sameScoreTieBreakerValue = 1000
    prefix = "1st Place: "
    amount = FIRST_AMOUNT
    tieBreakerScore = answersDict["answer"][int(answersDict["numGames"][0])]
    while localCount < 3:
        print(Style.RESET_ALL)
        if localCount == 1:
            prefix = "2nd Place: "
            amount = SECOND_AMOUNT
        elif localCount == 2:
            prefix = "3rd Place: "
            amount = THIRD_AMOUNT
        winnersList = []
        smallestDiff = 100
        finalWinner = ""
        finalWinnerTB = ""
        highestCorrectPicks = max(resultsDict.items(), key=lambda x: x[1])
        for participant in resultsDict:
            if resultsDict[participant] == highestCorrectPicks[1]:
                winnersList.append({participant : resultsDict[participant]})
        
        if len(winnersList) > 1:
            print("There is a tie with ", str(highestCorrectPicks[1])," correct picks. Result will be determined based on tie breaker score")
            resultString = resultString + "There is a tie with " + str(highestCorrectPicks[1]) + " correct picks. Result will be determined based on tie breaker score" + "\n"
            print("Tiebreaker score: " + str(tieBreakerScore))
            resultString = resultString + "Tiebreaker score: " + str(tieBreakerScore) + "\n"
            print()
            for winner in winnersList:
                for winnerKey in winner:
                    participantTieBreaker = answersDict[winnerKey][int(answersDict["numGames"][0])]
                    # print(winnerKey + "'s tie breaker score: " + str(participantTieBreaker))
                    participantDiff = abs(int(participantTieBreaker) - int(tieBreakerScore))
                    if participantDiff <= smallestDiff:
                        if participantDiff == smallestDiff:
                            # print(Fore.YELLOW + "We have a problem. Both tiebreaker scores were the same value away from actual tiebreaker")
                            print(Style.RESET_ALL)
                            sameTieBreakerScore = True
                            sameScoreTieBreakerValue = participantDiff
                        else:
                            smallestDiff = participantDiff
                            finalWinner = winnerKey
                            finalWinnerTB = str(participantTieBreaker)
            if sameTieBreakerScore:
                shouldTerminate, localCount, resultString, namesToRemove = determineTieBreakerWinner(winnersList, answersDict, localCount, resultString, tieBreakerScore, sameScoreTieBreakerValue)
                if shouldTerminate:
                    return resultString
                else:
                    for name in namesToRemove:
                        resultsDict.pop(name)
            else:
                print(Fore.GREEN + prefix + finalWinner + " wins " + amount + " with a tiebreaker score of " + finalWinnerTB)
                resultString = resultString + prefix + finalWinner + " wins " + amount + " with a tiebreaker score of " + finalWinnerTB + "\n"
                resultsDict.pop(finalWinner)
                localCount = localCount + 1
        elif len(winnersList) == 1:
            for winner in winnersList:
                for winnerKey in winner:
                    print(Fore.GREEN + prefix + winnerKey + " wins " + amount + " with " + str(winner[winnerKey]) + " correct picks!")
                    resultString = resultString + prefix + winnerKey + " wins " + amount + " with " + str(winner[winnerKey]) + " correct picks!" + "\n"
                    resultsDict.pop(winnerKey)
                    localCount = localCount + 1
        else:
            print("Error occured populating winners list")

    return resultString
    
# Determines a winner for 1ST, 2ND or 3RD if any of them have a tie in number of correct picks
# AND the same tie breaker score
def determineTieBreakerWinner(winnersList, answersDict, localCount, resultString, tieBreakerScore, sameScoreTieBreakerValue):
    tieBreakerList = []
    for winner in winnersList:
        for winnerKey in winner:
            participantTieBreaker2 = answersDict[winnerKey][int(answersDict["numGames"][0])]
            participantDiff2 = abs(int(participantTieBreaker2) - int(tieBreakerScore))
            if participantDiff2 == sameScoreTieBreakerValue:
                tieBreakerList.append(winnerKey)
    
    winnerNameString = ""
    # Case 1: 3 or more people with same tiebreaker tied for 1ST
    if localCount == 0 and len(tieBreakerList) > 2:
        print(Fore.GREEN + "3 or more people tied for first place!")
        resultString = resultString + "3 or more people tied for first place!" + "\n"
        for participant in tieBreakerList:
            winnerNameString = winnerNameString + participant + ", "
        winnerNameString = winnerNameString[:-2]
        amountWon = (FIRST_AMOUNT_INT + SECOND_AMOUNT_INT + THIRD_AMOUNT_INT) / len(tieBreakerList)
        print(winnerNameString + " each win $" + str(amountWon))
        resultString = resultString + winnerNameString + " each win $" + str(amountWon) + "\n"
        print(Style.RESET_ALL)
        winnerNameString = ""
        return (True, 0, resultString, [])
    
    # Case 2: 2 people with same tiebreaker tied for 1ST
    elif localCount == 0 and len(tieBreakerList) == 2:
        namesToRemove = []
        print(Fore.GREEN + "2 people tied for first place!")
        resultString = resultString + "2 people tied for first place!" + "\n"
        for participant in tieBreakerList:
            winnerNameString = winnerNameString + participant + ", "
            namesToRemove.append(participant)
        winnerNameString = winnerNameString[:-2]
        amountWon = (FIRST_AMOUNT_INT + SECOND_AMOUNT_INT) / len(tieBreakerList)
        print(winnerNameString + " each win $" + str(amountWon))
        resultString = resultString + winnerNameString + " each win $" + str(amountWon) + "\n"
        print(Style.RESET_ALL)
        winnerNameString = ""
        return (False, 2, resultString, namesToRemove)
    
    # Case 3: 2 or more people with same tiebreaker tied for 2ND
    elif localCount == 1 and len(tieBreakerList) == 2:
        print(Fore.GREEN + "2 or more people tied for second place!")
        resultString = resultString + "2 or more people tied for second place!" + "\n"
        for participant in tieBreakerList:
            winnerNameString = winnerNameString + participant + ", "
        winnerNameString = winnerNameString[:-2]
        amountWon = (SECOND_AMOUNT_INT + THIRD_AMOUNT_INT) / len(tieBreakerList)
        print(winnerNameString + " each win $" + str(amountWon))
        resultString = resultString + winnerNameString + " each win $" + str(amountWon) + "\n"
        print(Style.RESET_ALL)
        winnerNameString = ""
        return (True, 0, resultString, [])
    
    # Case 4: 2 or more people with same tiebreaker tied for 3RD
    elif localCount == 2 and len(tieBreakerList) == 2:
        print(Fore.GREEN + "2 or more people tied for third place!")
        resultString = resultString + "2 or more people tied for third place!" + "\n"
        for participant in tieBreakerList:
            winnerNameString = winnerNameString + participant + ", "
        winnerNameString = winnerNameString[:-2]
        amountWon = THIRD_AMOUNT_INT / len(tieBreakerList)
        print(winnerNameString + " each win $" + str(amountWon))
        resultString = resultString + winnerNameString + " each win $" + str(amountWon) + "\n"
        print(Style.RESET_ALL)
        winnerNameString = ""
        return (True, 0, resultString, [])






##############################################
## This is the beginning of the test pool code
##############################################


# Test pool launch pad. Call this function to initiate the test pool to run through
# all available previous weeks data and compare it to the recorded results that
# are currently being stored in global variables. Each week, Tom will need to add
# a new global variable for that weeks answers and add the variable name to the
# WEEK_NAME_DICT dictionary. If a week fails the test, the test pool will print an error
# message and will terminate execution

def runTestPool():
    print("###########################")
    print("STARTING TEST POOL")
    print("###########################\n")

    
    # Variable to keep track of what week we are testing. Start at 2 because I never
    # got data for week 1
    weekNum = 2
    while weekNum != 0:

        # Build the file name
        fileName = "week_" + str(weekNum) + ".txt"

        # Call the functions to be tested to get the values to compare to global variables
        answers,results = initializeTestVariables(fileName)

        # initializeTestVariables() will catch an exception if it can't find the file
        # we are looking for and return empty dictionaries for "answers" and "results".
        # This should only ever happen if we are trying to open a week that does not have data yet.
        # So if we make it to this point without breaking out of the loop then that means we have
        # passed every week of data we have to test.
        if answers == {} and results == {}:
            print(Fore.GREEN + "All systems go!\n")
            print(Style.RESET_ALL)
            print("###########################")
            print("TEST POOL COMPELTED")
            print("###########################\n")
            return True
        

        # Make sure I didn't make any typos entering the data
        print("Running input validator for " + fileName + " ...")
        spellingResults = runInputValidator(fileName)
        if spellingResults:
            print("Input validator completed. No mistakes were found. Continuing execution.")
        else:
            return

        # Get the dictionary from the test pool that contains the right answers to test 
        # buildAnswersDict() and buildResultsDict() against
        compareDict = getDictFromTestPool(weekNum)
        
        try:
            if results == compareDict:
                print(Fore.GREEN + "Week ", weekNum, " test passed!")
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "Week ", weekNum, " test failed\n")
                print(Style.RESET_ALL)
                print("###########################")
                print("TEST POOL COMPELTED")
                print("###########################\n")
                
                return False
            weekNum = weekNum + 1
        except:
            print("Could not find internal data structure for week " + str(weekNum) + ". Continuing...\n")
            print("###########################")
            print("TEST POOL COMPELTED")
            print("###########################\n")
            return True
    

def initializeTestVariables(inFile):
    answers = {}
    results = {}
    try:
        answers = buildAnswersDict(inFile)
    except:
        return {},{}
        
    results = buildResultsDict(answers)
    return answers, results

def getDictFromTestPool(weekNum):
    offset = 2
    testDict = {}
    with open("testPool.json") as testFile:
        data = json.load(testFile)
        testDict = data['TEST_POOL'][weekNum-offset]
    return testDict

def runInputValidator(fileName):
    teamNames = ["cardinals","falcons","panthers","bears","cowboys","lions","pack","rams","vikings",
                 "saints","giants","eagles","49ers","seahawks","bucs","wash","ravens","bills",
                 "bengals","browns","broncos","texans","colts","jags","chiefs","raiders","chargers",
                 "dolphins","pats","jets","steelers","titans"]
    participantNames = ["jason","austin","sam","fritzy","brad_j","tommy","rick","clark","carey",
                        "nick","brownie","connor","marty","answer","numgames","empty","jake_h","cal_griff",
                        "charlie","chubbs","skeeter"]
    inFile = open(fileName)
    for line in inFile:
        line = line.strip()
        line = line.split(",")
        for entry in line:
            if entry.lower() not in participantNames and entry.lower() not in teamNames and entry != line[-1]:
                print(Fore.RED + "You made a typo when entering " + entry + " for " + line[0] + " in " + fileName)
                print(Style.RESET_ALL)
                return False

    return True



# # Run through test pool
# runTestPool()

# # Validate inputs
# runInputValidator("week_8.txt")

# Call the main() function
main("week_8.txt", False)
