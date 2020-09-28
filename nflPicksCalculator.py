# Program to calculate number of correct picks on Sunday

from colorama import init, Fore, Style
init()

WEEK_2_RESULTS = {"Jason":10, "Austin":6, "Sam":7, "Fritzy":9, "Brad_J":7,
                  "Tommy":9, "Rick":8, "Clark":8, "Carey":10, "Nick":8,
                  "Brownie":10, "Connor":9, "Marty":6}
WEEK_3_RESULTS = {"Jason":3, "Austin":2, "Sam":3, "Fritzy":2, "Brad_J":3,
                  "Tommy":3, "Rick":3, "Clark":2, "Carey":3, "Nick":3,
                  "Brownie":3, "Connor":2, "Marty":3}

WEEK_NAME_DICT = {"WEEK_2_RESULTS":WEEK_2_RESULTS}

def main(inFile, verbose):
    
    systemOperational = runTestPool()

    if systemOperational:
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
                

        displayResults(results)

        print("###########################")
        print("RESULTS")
        print("###########################\n")

        calculateAndDisplayWinner(results, answers)

    else:
        print("Error in test pool. Terminating execution")
    

# This function takes a dictionary (answersDict) with one of the keys being equal to "answer". It
# will print the value stored in the answersDict["answer"] slot, which is a list of the winners
# between two teams for the week.
def displayWinners(answersDict):
    winnersString = buildPickString(answersDict["answer"])
    print("Winning teams this week: ", winnersString)


# This function takes a dictionary (resultsDict) and simply prints the key:value pair to display
# the results of everyones correct picks
def displayResults(resultsDict):
    for y in resultsDict:
        print(y, resultsDict[y])
    print()


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
        if x != "answer":
            for answer in answers[x]:
                # Actual comparison to check participant x's
                # answers against the answer key's answers
                if (answer.lower() == answers["answer"][counter].lower()) and counter < 10:
                    numCorrect = numCorrect + 1
                
                counter = counter + 1
            results[x] = numCorrect
    return results

def calculateAndDisplayWinner(resultsDict, answersDict):
    localCount = 0
    prefix = "1st Place: "
    amount = "$200"
    tieBreakerScore = answersDict["answer"][10]
    while localCount < 2:
        print(Style.RESET_ALL)
        if localCount == 1:
            prefix = "2nd Place: "
            amount = "$60"
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
            print("Tiebreaker score: " + str(tieBreakerScore))
            for winner in winnersList:
                for winnerKey in winner:
                    participantTieBreaker = answersDict[winnerKey][10]
                    print(winnerKey + "'s tie breaker score: " + str(participantTieBreaker))
                    participantDiff = abs(int(participantTieBreaker) - int(tieBreakerScore))
                    if participantDiff <= smallestDiff:
                        if participantDiff == smallestDiff:
                            print("We have a problem. Both tiebreaker scores were the same value away from actual tiebreaker")
                        else:
                            smallestDiff = participantDiff
                            finalWinner = winnerKey
                            finalWinnerTB = str(participantTieBreaker)
            print(Fore.GREEN + prefix + finalWinner + " wins ", amount, " with a tiebreaker score of " + finalWinnerTB)
            resultsDict.pop(finalWinner)
            localCount = localCount + 1
        elif len(winnersList) == 1:
            for winner in winnersList:
                for winnerKey in winner:
                    print(Fore.GREEN + prefix + winnerKey + " wins ", amount, " with " + str(winner[winnerKey]) + " correct picks!")
                    resultsDict.pop(winnerKey)
                    localCount = localCount + 1
        else:
            print("Error occured populating winners list")
    
        






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
            print("All systems go!\n")
            print("###########################")
            print("TEST POOL COMPELTED")
            print("###########################\n")
            return True
        try:
            if results == WEEK_NAME_DICT["WEEK_"+str(weekNum)+"_RESULTS"]:
                print("Week ", weekNum, " test passed!")
            else:
                print("Week ", weekNum, " test failed")
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

# Run through test pool
# runTestPool()

# Call the main() function
main("week_2.txt", False)