# Engineer: Thomas Hook
# Description: This program calculates the number of correct picks given
# .txt file containing participants answers along with an answer key
import json
from colorama import init, Fore, Style
import smtplib, ssl
from data.defaults import defaultValues

init()



def main(inFile, verbose):

    # Default the fileFormat to use Confidence vote function
    fileFormat = defaultValues.Format.CONFIDENCE_VOTE
    # Dict to hold answers read in from txt file
    # {<name> : [pick1,pick2,...,pick10]}
    answers, fileFormat = buildAnswersDict(defaultValues.weeks_path + inFile)

    # Dict to hold number of correct answers per participant
    # {<name> : (<numCorrectAnswers>, <tieBreakerScore>)}
    if fileFormat == defaultValues.Format.CONFIDENCE_VOTE:
        results = buildResultsDict(answers)
    else:
        results = buildResultsDictWithoutConfidenceVote(answers)
    
        
    displayTeamWinners(answers, fileFormat)

    # Extra logging if parameter is True. I need to add some more verbose functionality
    if verbose:
        displayParticipantsPicks(answers, fileFormat)
            
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
        with smtplib.SMTP_SSL(defaultValues.smtp_server, port, context=context) as server:
            server.login(defaultValues.sender_email, password)
            for receiver_email in emailList:
                server.sendmail(defaultValues.sender_email, receiver_email, message)

# This function builds the body of the email to be sent that contains the correct picks for the
# participants along with 1ST, 2ND and 3RD place winners
def buildResultsString(results, answers):
    resultString = ""

    # Portion of the email that contains the number of correct picks for each participant
    resultString = displayResults(results)

    # Portion of the email that contains the winners of 1ST, 2ND and 3RD place
    stringResults, finalResultsDict = calculateAndDisplayWinner(results, answers["answer"][-1])
    resultString = resultString + stringResults

    return resultString

# This function returns a list of emails from a text file
def generateEmailList():
    inFile = open(defaultValues.email_path)
    
    for line in inFile:
        line = line.strip()
        line = line.split(",")
        return line


# This function takes a dictionary (answersDict) with one of the keys being equal to "answer". It
# will print the value stored in the answersDict["answer"] slot, which is a list of the winners
# between two teams for the week.
def displayTeamWinners(answersDict, fileFormat):
    winnersString = buildPickString(answersDict["answer"], fileFormat)
    print("Winning teams this week: ", winnersString)


# This function takes a dictionary (resultsDict) and simply prints the key:value pair to display
# the results of everyones correct picks
def displayResults(resultsDict):
    resultString = ""
    # resultsDict = dict(sorted(resultsDict.items(), key=lambda item: item[1], reverse=True))
    for y in resultsDict:
        print(y, resultsDict[y][0])
        resultString = resultString + y + ": " + str(resultsDict[y]) + "\n"
    print()

    return resultString


# This function takes a dictionary (answersDict) and displays everyones picks for the week. It will
# exclude the "answer" key and will only be called if Verbose logging is on
def displayParticipantsPicks(answersDict, fileFormat):
    for x in answersDict:
        if x != "answer":
            answerStr = buildPickString(answersDict[x], fileFormat)
            print(x, ":", answerStr)


# Helper function to return a string of values seperated by a comma and space, given a list.
def buildPickString(answerList, fileFormat):
    pickStr = ""
    for x in range(len(answerList) - 1):
        if fileFormat == defaultValues.Format.CONFIDENCE_VOTE:
            if x % 2 == 0:
                pickStr = pickStr + answerList[x] + ", "
        else:
            pickStr = pickStr + answerList[x] + ", "
    
    # Take away last comma on end of string
    pickStr = pickStr[:-2]

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

        # Don't add the format to the answers dict. Just set the global format
        # variable
        if line[0] == 'format':
            format = setFormat(line[1])
        else:
            # Inserts a value into the dictionary
            # keyed by the name of the participant
            # with a value of their picks
            answers[line[0]] = line[1:]

    
    return answers, format

def setFormat(format):
    print("Setting format to: ", format)
    if format.lower() == "confidence":
        fileFormat = defaultValues.Format.CONFIDENCE_VOTE
    else:
        fileFormat = defaultValues.Format.NO_CONFIDENCE_VOTE
    return fileFormat

# This function takes a dictionary (answers) and iterates through to compare everyone's picks to the
# correct picks. This is the confidence vote version of the function so if the participant gets a pick
# correct, instead of just getting 1 point. They will get the confidence points they assigned to the game.
def buildResultsDict(answers):
    results = {}
    # Iterate through internal data structure (answers) and compare
    # the participant answer to the answer key to and store result in
    # another internal data structure (results)
    for x in answers:
        if x != "answer" and x != "numGames":
            numCorrect = 0
            for y in range(int(answers["numGames"][0]) * 2):
                if y % 2 == 0:
                    # Actual comparison to check participant x's
                    # answers against the answer key's answers
                    if (answers[x][y].lower() == answers["answer"][y].lower()) and y < (int(answers["numGames"][0]) * 2):
                        # Add the confidence vote to the total for this participant
                        numCorrect = numCorrect + int(answers[x][y + 1])

            # results format: {"<participantName>" : (<totalPoints>, <tieBreakerScore>)}
            results[x] = (numCorrect, int(answers[x][-1]))

    return results


# This function takes a dictionary (answers) and iterates through to compare everyone's picks to the
# correct picks. This is the NON-confidence vote version of the function. So if a user gets a pick correct they
# simply get 1 point added to their total
def buildResultsDictWithoutConfidenceVote(answers):
    results = {}
    # Iterate through internal data structure (answers) and compare
    # the participant answer to the answer key to and store result in
    # another internal data structure (results)
    for x in answers:
        if x != "answer" and x != "numGames" and x != "format":
            numCorrect = 0
            for y in range(int(answers["numGames"][0])):
                # Actual comparison to check participant x's
                # answers against the answer key's answers
                if (answers[x][y].lower() == answers["answer"][y].lower()) \
                        and y < (int(answers["numGames"][0])):
                    # Add the confidence vote to the total for this participant
                    numCorrect = numCorrect + 1

            # results format: {"<participantName>" : (<totalPoints>, <tieBreakerScore>)}
            results[x] = (numCorrect, int(answers[x][-1]))

    return results

def calculateAndDisplayWinner(resultsDict, tieBreakerScore):
    # print("Results dict: ", resultsDict)
    # print("tiebrealer scpre: ", tieBreakerScore)
    localCount = 0
    resultString = ""
    sameTieBreakerScore = False
    prefix = "1st Place: "
    amount = defaultValues.FIRST_AMOUNT
    # This is only used for unit test purposes
    finalResultsDict = {}
    
    # localCount refers to the number of participants that will be paid out. This
    # number needs to be adjusted as that changes. Ex: if 1st and 2nd get paid, 
    # it needs to be "while localCount < 2". 
    while localCount < 3:
        print(Style.RESET_ALL)

        # Set variables used for output string
        if localCount == 1:
            prefix = "2nd Place: "
            amount = defaultValues.SECOND_AMOUNT
        elif localCount == 2:
            prefix = "3rd Place: "
            amount = defaultValues.THIRD_AMOUNT

        # Set default values for the current loop
        winnersList = []
        tieBreakerList = []
        smallestDiff = defaultValues.smallestDiff
        finalWinner = ""
        finalWinnerTB = ""


        # Get the highest value from the results dictionary
        highestCorrectPicks = max(resultsDict.items(), key=lambda x: x[1])
        highestCorrectPicks = highestCorrectPicks[1][0]
        
        # Iterate through the participants to see who has the highest score. Keep
        # in mind there can be ties
        for participant in resultsDict:
            if resultsDict[participant][0] == highestCorrectPicks:
                # Add participant name to winnersList
                winnersList.append(participant)
        
        # This means there are at least 2 people tied for the current position
        # being calculated (Ex: 1st, 2nd or 3rd)
        if len(winnersList) > 1:
            print("There is a tie with ", str(highestCorrectPicks)," correct picks. Result will be determined based on tie breaker score")

            # Store string in variable to be used for email later
            resultString = resultString + "There is a tie with " + str(highestCorrectPicks) + " correct picks. Result will be determined based on tie breaker score" + "\n"

            print("Tiebreaker score: " + str(tieBreakerScore))

            # Store string in variable to be used for email later
            resultString = resultString + "Tiebreaker score: " + str(tieBreakerScore) + "\n"

            # Iterate through the participants who have tied
            for winner in winnersList:
                # Get the participants tie breaker score
                participantTieBreaker = resultsDict[winner][1]
                # print(winnerKey + "'s tie breaker score: " + str(participantTieBreaker))

                # Calculate the difference between the participants tie breaker score (participantTieBreaker)
                # and the real tie breaker score (tieBreakerScore)
                participantDiff = abs(int(participantTieBreaker) - int(tieBreakerScore))

                # Check if that difference is smaller than the smallest difference we have 
                # calculated so far. If so, then this participant will be in the lead.
                if participantDiff <= smallestDiff:

                    # If we have two participants the same distance away from the tie breaker score
                    # Then we have to do do some special logic to determine the payouts. Also if this is the 
                    # first tie breaker play we are comparing we automatically need to add them to the tieBreakerList
                    # Then we have a check to only call determineTieBreakerPayout if that list is larger than 1
                    if participantDiff == smallestDiff or smallestDiff == defaultValues.smallestDiff:
                        # print(Fore.YELLOW + "We have a problem. Both tiebreaker scores were the same value away from actual tiebreaker")
                        print(Style.RESET_ALL)
                        # Add the participant to the list of tie breakers to be passed to determineTieBreakerPayout
                        tieBreakerList.append(winner)
                        finalWinner = winner
                        finalWinnerTB = str(participantTieBreaker)
                        if (len(tieBreakerList) > 1):
                            sameTieBreakerScore = True

                    # One of the participants had a tiebreaker score that was a smaller distance away
                    # from the real tiebreaker score than the other participants. Clear the 
                    # tieBreakerList, add the current participant and continue processing    
                    else:
                        tieBreakerList.clear()
                        tieBreakerList.append(winner)

                        finalWinner = winner

                        finalWinnerTB = str(participantTieBreaker)
                        sameTieBreakerScore = False
                    smallestDiff = participantDiff

            # This value is set if we have more than 1 participant in the tieBreakerList list.
            # This means we need to determine the payout for the players who have tied and decide
            # if we need to continue processing or not
            if sameTieBreakerScore:
                shouldTerminate, localCount, resultString, namesToRemove, finalResultsDict  = determineTieBreakerPayout(tieBreakerList, localCount, resultString, finalResultsDict)

                # We had at least as many players tie as there are payouts
                # (Ex: 3 players tied for 1st and only 3 are payed out)
                if shouldTerminate:
                    return resultString, finalResultsDict
                
                # If we are to continue processing. Remove the names who tied and have had their 
                # payouts determined and start the loop over with the remaining resultsDict
                else:
                    for name in namesToRemove:
                        resultsDict.pop(name)

            # We were able to determine a clear winner based off the tie breaker score.
            else:
                print(Fore.GREEN + prefix + finalWinner + " wins " + amount + " with a tiebreaker score of " + finalWinnerTB)
                resultString = resultString + prefix + finalWinner + " wins " + amount + " with a tiebreaker score of " + finalWinnerTB + "\n"
                finalResultsDict[finalWinner] = localCount + 1
                resultsDict.pop(finalWinner)
                localCount = localCount + 1

        # We had no ties for this cycle in the loop. Display the winner
        elif len(winnersList) == 1:
            print(Fore.GREEN + prefix + winnersList[0] + " wins " + amount + " with " + str(highestCorrectPicks) + " correct picks!")
            resultString = resultString + prefix + winnersList[0] + " wins " + amount + " with " + str(highestCorrectPicks) + " correct picks!" + "\n"
            finalResultsDict[winnersList[0]] = localCount + 1
            resultsDict.pop(winnersList[0])
            localCount = localCount + 1

        else:
            print("Error occurred populating winners list")

    #finalResultsDict is only used for unit test purposes
    return resultString, finalResultsDict
    
# Determines a payout for 1ST, 2ND or 3RD if any of them have a tie in number of correct picks
# AND the same tie breaker score. Also will tell us if we need to continue calculating winners
# based on how many we have calculated so far (localCount) and how many are tied
def determineTieBreakerPayout(tieBreakerList, localCount, resultString, finalResultsDict):

    winnerNameString = ""
    # Case 1: 3 or more people with same tiebreaker tied for 1ST
    if localCount == 0 and len(tieBreakerList) > 2:
        print(Fore.GREEN + "3 or more people tied for first place!")
        resultString = resultString + "3 or more people tied for first place!" + "\n"
        for participant in tieBreakerList:
            finalResultsDict[participant] = localCount + 1
            winnerNameString = winnerNameString + participant + ", "
        winnerNameString = winnerNameString[:-2]
        amountWon = (
                                defaultValues.FIRST_AMOUNT_INT + defaultValues.SECOND_AMOUNT_INT + defaultValues.THIRD_AMOUNT_INT) / len(tieBreakerList)
        print(winnerNameString + " each win $" + str(amountWon))
        resultString = resultString + winnerNameString + " each win $" + str(amountWon) + "\n"
        print(Style.RESET_ALL)
        winnerNameString = ""
        return (True, 0, resultString, [], finalResultsDict)
    
    # Case 2: 2 people with same tiebreaker tied for 1ST
    elif localCount == 0 and len(tieBreakerList) == 2:
        shouldTerminate = False
        if localCount > 0:
            shouldTerminate = True
        namesToRemove = []
        print(Fore.GREEN + "2 people tied for first place!")
        resultString = resultString + "2 people tied for first place!" + "\n"
        for participant in tieBreakerList:
            finalResultsDict[participant] = localCount + 1
            winnerNameString = winnerNameString + participant + ", "
            namesToRemove.append(participant)
        winnerNameString = winnerNameString[:-2]
        amountWon = (defaultValues.FIRST_AMOUNT_INT + defaultValues.SECOND_AMOUNT_INT) / len(tieBreakerList)
        print(winnerNameString + " each win $" + str(amountWon))
        resultString = resultString + winnerNameString + " each win $" + str(amountWon) + "\n"
        print(Style.RESET_ALL)
        winnerNameString = ""
        return (shouldTerminate, 2, resultString, namesToRemove, finalResultsDict)
    
    # Case 3: 2 or more people with same tiebreaker tied for 2ND
    elif localCount == 1 and len(tieBreakerList) >= 2:
        print(Fore.GREEN + "2 or more people tied for second place!")
        resultString = resultString + "2 or more people tied for second place!" + "\n"
        for participant in tieBreakerList:
            finalResultsDict[participant] = localCount + 1
            winnerNameString = winnerNameString + participant + ", "
        winnerNameString = winnerNameString[:-2]
        amountWon = (defaultValues.SECOND_AMOUNT_INT + defaultValues.THIRD_AMOUNT_INT) / len(tieBreakerList)
        print(winnerNameString + " each win $" + str(amountWon))
        resultString = resultString + winnerNameString + " each win $" + str(amountWon) + "\n"
        print(Style.RESET_ALL)
        winnerNameString = ""
        return (True, 0, resultString, [], finalResultsDict)
    
    # Case 4: 2 or more people with same tiebreaker tied for 3RD
    elif localCount == 2 and len(tieBreakerList) >= 2:
        print(Fore.GREEN + "2 or more people tied for third place!")
        resultString = resultString + "2 or more people tied for third place!" + "\n"
        for participant in tieBreakerList:
            finalResultsDict[participant] = localCount + 1
            winnerNameString = winnerNameString + participant + ", "
        winnerNameString = winnerNameString[:-2]
        amountWon = defaultValues.THIRD_AMOUNT_INT / len(tieBreakerList)
        print(winnerNameString + " each win $" + str(amountWon))
        resultString = resultString + winnerNameString + " each win $" + str(amountWon) + "\n"
        print(Style.RESET_ALL)
        winnerNameString = ""
        return (True, 0, resultString, [], finalResultsDict)






##############################################
## This is the beginning of the test pool code
##############################################


# Test pool launch pad. Call this function to initiate the test pool to run through
# all available previous weeks data and compare it to the recorded results that
# are stored in testPool.json. Each week, Tom will need to add an entry to 
# testPool.json for that weeks answers. If a week fails the test, the test pool 
# will print an error message and will terminate execution

def runTestPool():
    print("###########################")
    print("STARTING TEST POOL")
    print("###########################\n")

    
    # Variable to keep track of what week we are testing. Start at 2 because I never
    # got data for week 1
    weekNum = 2
    while weekNum != 0:

        # Build the file name
        fileName = "cWeek_" + str(weekNum) + ".txt"

        # Call the functions to be tested to get the values to compare to global variables
        answers,results = initializeTestVariables(fileName)

        ## Debug in case testing ever fails and you need to compare
        # print("RESULTS: " + results)

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
            print("Input validator completed. No mistakes were found. Continuing execution...")
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
        answers = buildAnswersDict(defaultValues.weeks_path + inFile)
    except:
        return {},{}
        
    results = buildResultsDict(answers)
    return answers, results

def getDictFromTestPool(weekNum):
    offset = 2
    testDict = {}
    with open(defaultValues.test_file_path + "testPool.json") as testFile:
        data = json.load(testFile)
        testDict = data['TEST_POOL'][weekNum-offset]
        ## Debug in case testing ever fails and you need to compare
        # print(data)
    return testDict

def runInputValidator(fileName):
    teamNames = ["cardinals","falcons","panthers","bears","cowboys","lions","pack","rams","vikings",
                 "saints","giants","eagles","49ers","seahawks","bucs","wash","ravens","bills",
                 "bengals","browns","broncos","texans","colts","jags","chiefs","raiders","chargers",
                 "dolphins","pats","jets","steelers","titans","commanders","michigan","washington","texas","arkansas",
                 "iowa","isu","utah","byu","buffalo","nebraska","alabama","minnesota","colorado","northwestern","duke",
                 "cincinnati","indiana","michigan_st","miami","oklahoma_st","texas","purdue","florida","kansas_st","purdue",
                 "penn_st","oklahoma","notre_dame","wisconsin","minnesota","georgia","va_tech","texas_am","north_western",
                 "kentucky","mich_st","iowa_st","rutgers","texas_tech","nc_st","tcu","wv","ohio_st","baylor","illinois","rutgers",
                 "auburn","az_st","usc","miss","unlv","wake_forest","hawaii","oregon","clemson","ucla", "florida_st",
                 "tennessee", "pitt", "houston", "kentucky", "stanford", "citadel", "etsu", "ole_miss", "ndsu","wku", "arizona",
                 "georgia_tech", "osu", "kansas", "lsu", "wmu", "emu", "miss_st","louisville", "syracuse", "maryland", "wvu", "vanderbilt", "ucf",
                 "toledo", "fresno", "tulane", "ohio", "boise"]
    participantNames = ["jason","austin","sam","fritzy","brad_j","tommy","rick","clark","carey",
                        "nick","brownie","connor","marty","answer","numgames","empty","jake_h","cal_griff",
                        "charlie","chubbs","skeeter", "format", "confidence", "no_confidence", "ron","brownie", "aj", "chris_q",
                        "lucas","tim","todd","tyler","mike_b","adam"]
    inFile = open(defaultValues.weeks_path + fileName)
    for line in inFile:
        line = line.strip()
        line = line.split(",")
        for entry in line:
            if entry.lower() == "numgames":
                numGames = line[-1]
            if entry.lower() not in participantNames and entry.lower() not in teamNames and entry != line[-1]:
                print(Fore.RED + "You made a typo when entering " + entry + " for " + line[0] + " in " + fileName)
                print(Style.RESET_ALL)
                return False

    inFile = open(defaultValues.weeks_path + fileName)
    for line in inFile:
        line = line.strip()
        line = line.split(",")
        if line[0].lower() == "numgames" or line[0].lower() == "format":
            continue
        if len(line) != int(numGames) + 2:
            print(Fore.RED + "Participant: " + line[0] + " does not contain enough entries")
            return False
    print(Fore.GREEN + "Inputs are valid")

    return True



# # Run through test pool
# runTestPool()

# Validate inputs
runInputValidator("week_16.txt")

# Call the main() function
# # This needs to be commented out for unit tests to run properly
main("week_16.txt", False)

