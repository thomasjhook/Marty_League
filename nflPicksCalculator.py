# Program to calculate number of correct picks on Sunday

WEEK_2_RESULTS = {"Jason":10, "Austin":6, "Sam":7, "Fritzy":9, "Brad_J":7,
                  "Tommy":9, "Rick":8, "Clark":8, "Carey":10, "Nick":8,
                  "Brownie":10, "Connor":9, "Marty":6}
WEEK_3_RESULTS = {"Jason":8, "Austin":5, "Sam":8, "Fritzy":6, "Brad_J":7,
                  "Tommy":6, "Rick":6, "Clark":6, "Carey":8, "Nick":7,
                  "Brownie":7, "Connor":6, "Marty":6}

WEEK_NAME_DICT = {"WEEK_2_RESULTS":WEEK_2_RESULTS,
                  "WEEK_3_RESULTS":WEEK_3_RESULTS}

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
            

    displayResults(results)
    

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
                if answer.lower() == answers["answer"][counter].lower():
                    numCorrect = numCorrect + 1
                
                counter = counter + 1
            results[x] = numCorrect
    return results


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
            print("All systems go!")
            break
        
        if results == WEEK_NAME_DICT["WEEK_"+str(weekNum)+"_RESULTS"]:
            print("Week ", weekNum, " test passed!")
        else:
            print("Week ", weekNum, " test failed")
            break
        weekNum = weekNum + 1
    

def initializeTestVariables(inFile):
    answers = {}
    results = {}
    try:
        answers = buildAnswersDict(inFile)
    except:
        return {},{}
        
    results = buildResultsDict(answers)
    return answers, results
