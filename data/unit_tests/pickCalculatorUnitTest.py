import unittest
from src import nflPicksCalculator
import testCaseValues

class MyTestCase(unittest.TestCase):

    ##############################################
    # CalculateAndDisplayWinner Unit Test 1
    # 3 tie for first
    ##############################################
    def test_calculateAndDisplayWinnerTest1(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest1Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore1)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest1ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 2
    # 2 tie for first, 1 gets 3rd
    ##############################################
    def test_calculateAndDisplayWinnerTest2(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest2Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore2)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest2ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 3
    # 1 first 2 tie for second
    ##############################################
    def test_calculateAndDisplayWinnerTest3(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest3Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore3)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest3ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 4
    # 1 first 3 tie for second
    ##############################################
    def test_calculateAndDisplayWinnerTest4(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest4Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore4)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest4ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 5
    # 5 tie for first
    ##############################################
    def test_calculateAndDisplayWinnerTest5(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest5Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore5)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest5ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 6
    # first entry wins
    ##############################################
    def test_calculateAndDisplayWinnerTest6(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest6Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore6)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest6ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 7
    # last entry wins
    ##############################################
    def test_calculateAndDisplayWinnerTest7(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest7Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore7)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest7ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 8
    # Tie for first, second participant has better tie breaker so they win outright
    ##############################################
    def test_calculateAndDisplayWinnerTest8(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest8Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore8)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest8ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 9
    # Tie for first, first participant has better tie breaker so they win outright
    ##############################################
    def test_calculateAndDisplayWinnerTest9(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest9Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore9)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest9ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 10
    # 3 Tie for first, last participant has better tie breaker so they win outright
    ##############################################
    def test_calculateAndDisplayWinnerTest10(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest10Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore10)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest10ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 11
    # 3 Tie for first, middle participant has better tie breaker so they win outright
    ##############################################
    def test_calculateAndDisplayWinnerTest11(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest11Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore11)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest11ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 12
    # 3 Tie for first, first participant has better tie breaker so they win outright
    ##############################################
    def test_calculateAndDisplayWinnerTest12(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest12Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore12)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest12ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 13
    # 2 tie for first (same tiebreaker), 3 tie for third (same tiebreaker)
    ##############################################
    def test_calculateAndDisplayWinnerTest13(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest13Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore13)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest13ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 14
    # 2 tie for first (different tiebreaker), 3 tie for third (different tiebreaker)
    ##############################################
    def test_calculateAndDisplayWinnerTest14(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest14Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore14)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest14ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 15
    # 2 tie for second (different tiebreaker)
    ##############################################
    def test_calculateAndDisplayWinnerTest15(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest15Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore15)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest15ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 16
    # 3 tie for third (different tiebreaker)
    ##############################################
    def test_calculateAndDisplayWinnerTest16(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest16Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore16)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest16ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 17
    # No ties first winner
    ##############################################
    def test_calculateAndDisplayWinnerTest17(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest17Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore17)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest17ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 18
    # No ties middle winner
    ##############################################
    def test_calculateAndDisplayWinnerTest18(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest18Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore18)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest18ExpectedOutput)

    ##############################################
    # CalculateAndDisplayWinner Unit Test 19
    # No ties end winner
    ##############################################
    def test_calculateAndDisplayWinnerTest19(self):
        resultString, finalResultsDict = nflPicksCalculator.calculateAndDisplayWinner(
            testCaseValues.caclulateAndDisplayWinnerTest19Answers,
            testCaseValues.caclulateAndDisplayWinnerTieBreakerScore19)
        self.assertEqual(finalResultsDict, testCaseValues.calclateAndDisplayWinnerTest19ExpectedOutput)





if __name__ == '__main__':
    unittest.main()
