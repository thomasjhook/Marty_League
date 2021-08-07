
##############################################
# CalculateAndDisplayWinner Unit Test 1
# 3 tie for first (all same tiebreaker)
##############################################
# Inputs
caclulateAndDisplayWinnerTest1Answers = {'Tommy': (1, 5), 'Austin': (1, 5), 'Connor': (1, 5)}
caclulateAndDisplayWinnerTieBreakerScore1 = 5

# Expected Output
calclateAndDisplayWinnerTest1ExpectedOutput = {'Tommy': 1, 'Austin': 1, 'Connor': 1}

##############################################
# CalculateAndDisplayWinner Unit Test 2
# 2 tie for first (same tiebreaker), 1 third
##############################################
# Inputs
caclulateAndDisplayWinnerTest2Answers = {'Tommy': (2, 5), 'Austin': (2, 5), 'Connor': (1, 7)}
caclulateAndDisplayWinnerTieBreakerScore2 = 5

# Expected Output
calclateAndDisplayWinnerTest2ExpectedOutput = {'Tommy': 1, 'Austin': 1, 'Connor': 3}

##############################################
# CalculateAndDisplayWinner Unit Test 3
# 1 first 2 tie for second (same tiebreaker)
##############################################
# Inputs
caclulateAndDisplayWinnerTest3Answers = {'Tommy': (2, 5), 'Austin': (1, 6), 'Connor': (1, 6)}
caclulateAndDisplayWinnerTieBreakerScore3 = 5

# Expected Output
calclateAndDisplayWinnerTest3ExpectedOutput = {'Tommy': 1, 'Austin': 2, 'Connor': 2}

##############################################
# CalculateAndDisplayWinner Unit Test 4
# 1 first 3 tie for second (same tiebreaker)
##############################################
# Inputs
caclulateAndDisplayWinnerTest4Answers = {'Tommy': (2, 5), 'Austin': (1, 6), 'Connor': (1, 6), 'Adam': (1, 6)}
caclulateAndDisplayWinnerTieBreakerScore4 = 5

# Expected Output
calclateAndDisplayWinnerTest4ExpectedOutput = {'Tommy': 1, 'Austin': 2, 'Connor': 2, 'Adam': 2}

##############################################
# CalculateAndDisplayWinner Unit Test 5
# 5 tie for first (same tiebreaker)
##############################################
# Inputs
caclulateAndDisplayWinnerTest5Answers = {'Tommy': (1, 6), 'Austin': (1, 6), 'Connor': (1, 6), 'Adam': (1, 6), 'Bob': (1, 6)}
caclulateAndDisplayWinnerTieBreakerScore5 = 5

# Expected Output
calclateAndDisplayWinnerTest5ExpectedOutput = {'Tommy': 1, 'Austin': 1, 'Connor': 1, 'Adam': 1, 'Bob': 1}

##############################################
# CalculateAndDisplayWinner Unit Test 6
# First entry wins
##############################################
# Inputs
caclulateAndDisplayWinnerTest6Answers = {'Tommy': (5, 5), 'Austin': (1, 6), 'Connor': (3, 7)}
caclulateAndDisplayWinnerTieBreakerScore6 = 5

# Expected Output
calclateAndDisplayWinnerTest6ExpectedOutput = {'Tommy': 1, 'Austin': 3, 'Connor': 2}

##############################################
# CalculateAndDisplayWinner Unit Test 7
# last entry wins
##############################################
# Inputs
caclulateAndDisplayWinnerTest7Answers = {'Tommy': (5, 6), 'Austin': (6, 6), 'Connor': (7, 6), 'Adam': (8, 6), 'Bob': (9, 6)}
caclulateAndDisplayWinnerTieBreakerScore7 = 5

# Expected Output
calclateAndDisplayWinnerTest7ExpectedOutput = {'Bob': 1, 'Connor': 3, 'Adam': 2}


##############################################
# CalculateAndDisplayWinner Unit Test 8
# 2 tie for first, second participant has better tie breaker so they win outright
##############################################
# Inputs
caclulateAndDisplayWinnerTest8Answers = {'Tommy': (2, 6), 'Austin': (2, 5), 'Connor': (1, 5)}
caclulateAndDisplayWinnerTieBreakerScore8 = 5

# Expected Output
calclateAndDisplayWinnerTest8ExpectedOutput = {'Tommy': 2, 'Austin': 1, 'Connor': 3}

##############################################
# CalculateAndDisplayWinner Unit Test 9
# 2 Tie for first, first participant has better tie breaker so they win outright
##############################################
# Inputs
caclulateAndDisplayWinnerTest9Answers = {'Tommy': (2, 5), 'Austin': (2, 6), 'Connor': (1, 5)}
caclulateAndDisplayWinnerTieBreakerScore9 = 5

# Expected Output
calclateAndDisplayWinnerTest9ExpectedOutput = {'Tommy': 1, 'Austin': 2, 'Connor': 3}

##############################################
# CalculateAndDisplayWinner Unit Test 10
# 3 Tie for first, last participant has better tie breaker so they win outright
##############################################
# Inputs
caclulateAndDisplayWinnerTest10Answers = {'Tommy': (2, 7), 'Austin': (2, 6), 'Connor': (2, 5)}
caclulateAndDisplayWinnerTieBreakerScore10 = 5

# Expected Output
calclateAndDisplayWinnerTest10ExpectedOutput = {'Tommy': 3, 'Austin': 2, 'Connor': 1}

##############################################
# CalculateAndDisplayWinner Unit Test 11
# 3 Tie for first, middle participant has better tie breaker so they win outright
##############################################
# Inputs
caclulateAndDisplayWinnerTest11Answers = {'Tommy': (2, 6), 'Austin': (2, 5), 'Connor': (2, 7)}
caclulateAndDisplayWinnerTieBreakerScore11 = 5

# Expected Output
calclateAndDisplayWinnerTest11ExpectedOutput = {'Tommy': 2, 'Austin': 1, 'Connor': 3}

##############################################
# CalculateAndDisplayWinner Unit Test 12
# 3 Tie for first, fist participant has better tie breaker so they win outright
##############################################
# Inputs
caclulateAndDisplayWinnerTest12Answers = {'Tommy': (2, 5), 'Austin': (2, 6), 'Connor': (2, 7)}
caclulateAndDisplayWinnerTieBreakerScore12 = 5

# Expected Output
calclateAndDisplayWinnerTest12ExpectedOutput = {'Tommy': 1, 'Austin': 2, 'Connor': 3}


##############################################
# CalculateAndDisplayWinner Unit Test 13
# 2 tie for first (same tiebreaker), 3 tie for third (same tiebreaker)
##############################################
# Inputs
caclulateAndDisplayWinnerTest13Answers = {'Tommy': (2, 5), 'Austin': (2, 5), 'Connor': (1, 7), 'Bob': (1, 7), 'Rick': (1, 7)}
caclulateAndDisplayWinnerTieBreakerScore13 = 5

# Expected Output
calclateAndDisplayWinnerTest13ExpectedOutput = {'Tommy': 1, 'Austin': 1, 'Connor': 3, 'Bob': 3, 'Rick': 3}

##############################################
# CalculateAndDisplayWinner Unit Test 14
# 2 tie for first (different tiebreaker), 3 tie for third (different tiebreaker)
##############################################
# Inputs
caclulateAndDisplayWinnerTest14Answers = {'Tommy': (2, 6), 'Austin': (2, 5), 'Connor': (1, 7), 'Bob': (1, 8), 'Rick': (1, 5)}
caclulateAndDisplayWinnerTieBreakerScore14 = 5

# Expected Output
calclateAndDisplayWinnerTest14ExpectedOutput = {'Tommy': 2, 'Austin': 1, 'Rick': 3}

##############################################
# CalculateAndDisplayWinner Unit Test 15
# 2 tie for second (different tiebreaker)
# Inputs
caclulateAndDisplayWinnerTest15Answers = {'Tommy': (12, 6), 'Austin': (2, 5), 'Connor': (2, 7), 'Bob': (1, 8), 'Rick': (1, 5)}
caclulateAndDisplayWinnerTieBreakerScore15 = 5

# Expected Output
calclateAndDisplayWinnerTest15ExpectedOutput = {'Tommy': 1, 'Austin': 2, 'Connor': 3}

##############################################
# CalculateAndDisplayWinner Unit Test 16
# 3 tie for third (different tiebreaker)
##############################################
# Inputs
caclulateAndDisplayWinnerTest16Answers = {'Tommy': (2, 6), 'Austin': (13, 5), 'Connor': (1, 7), 'Bob': (1, 8), 'Rick': (1, 5)}
caclulateAndDisplayWinnerTieBreakerScore16 = 5

# Expected Output
calclateAndDisplayWinnerTest16ExpectedOutput = {'Tommy': 2, 'Austin': 1, 'Rick': 3}

##############################################
# CalculateAndDisplayWinner Unit Test 17
# No ties fist winner
##############################################
# Inputs
caclulateAndDisplayWinnerTest17Answers = {'Tommy': (2, 6), 'Austin': (13, 5), 'Connor': (1, 7), 'Bob': (8, 8), 'Rick': (7, 5)}
caclulateAndDisplayWinnerTieBreakerScore17 = 5

# Expected Output
calclateAndDisplayWinnerTest17ExpectedOutput = {'Bob': 2, 'Austin': 1, 'Rick': 3}

##############################################
# CalculateAndDisplayWinner Unit Test 18
# No ties middle winner
##############################################
# Inputs
caclulateAndDisplayWinnerTest18Answers = {'Tommy': (10, 6), 'Austin': (13, 5), 'Connor': (1, 7), 'Bob': (8, 8), 'Rick': (7, 5)}
caclulateAndDisplayWinnerTieBreakerScore18 = 5

# Expected Output
calclateAndDisplayWinnerTest18ExpectedOutput = {'Bob': 3, 'Austin': 1, 'Tommy': 2}

##############################################
# CalculateAndDisplayWinner Unit Test 18
# No ties end winner
##############################################
# Inputs
caclulateAndDisplayWinnerTest19Answers = {'Tommy': (10, 6), 'Austin': (13, 5), 'Connor': (1, 7), 'Bob': (15, 8), 'Rick': (7, 5)}
caclulateAndDisplayWinnerTieBreakerScore19 = 5

# Expected Output
calclateAndDisplayWinnerTest19ExpectedOutput = {'Bob': 1, 'Austin': 2, 'Tommy': 3}