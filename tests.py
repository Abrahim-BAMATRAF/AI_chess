import time

import chess
from alpha import gagnantAmiAlphaBeta_user
from alphaWithTime import gagnantAmiAlphaBetaWithTime_user
from heuristique import *
from humanVsAlpha import matchHumanVsAlpha
from maxMin import gagnantAmi
from search import search, searchWithTime_user

""" this file contain tests of all the functions created during this project
"""
board = chess.Board()

""" party 2 - E1 (recherche exhaustive)
"""
print("testing search to calculate how many noeuds can we reach")
print("if the depth of search 1 ", search(board, 1))
print("if the depth of search 2 ", search(board, 2))
print("if the depth of search 3 ", search(board, 3))

print("testing searchWithTime to calculate how many levels can we reach in a specific time default 30s")
time_limit = 2
print("when the time limit is : ", time_limit, " , the number of levels is : ", searchWithTime_user(board, time_limit))

""" party 2 - E2 (heuristique)
"""
print("testing the function get_piece")
white_piece, black_piece = get_piece(board)
print("printing white pieces", white_piece)
print("printing black pieces", black_piece)

print("testing calculate_score")
print("the score is : ", calculate_score(white_piece))

print("testing getWhitePawns")
print("the white pawns are : ", getWhitePawns(board))

print("testing scoreWhitePawns")
print("the score of the white pawns advancement", scoreWhitePawns(getWhitePawns(board)))

print("testing scoreBlackPawns")
print("the score of the black pawns advancement", scoreBlackPawns(getBlackPawns(board)))
print("testing heuristique : ", heuristique(board))

"""party2 - E3 (MaxMin)"""
print("testing MaxMin")
print("the move suggested by MaxMin : ", gagnantAmi(board, 3))

"""party2 - E4 (match between random vs MaxMin)"""
print("testing a match between random vs MaxMin")
# matchRandomVsMaxMin(board, 3)

"""party 3 - E1 (AlphaBeta)"""
print("testing alphaBeta")
print("the move suggested by alphaBeta : ", gagnantAmiAlphaBeta_user(board, 3))

print("testing a match between alphaBeta vs MaxMin")
# matchAlphaVsMaxMin(board, 3)


"""party 3 - E2 (gagnantAmiAlphaBetaWithTime)"""
print("testing gagnantAmiAlphaBetaWithTime")
time_limit_alpha = 3
start_test = time.time()
start = time.time()
print(gagnantAmiAlphaBetaWithTime_user(board, 500000, time_limit_alpha))
end_test = time.time()
print("the time of gagnantAmiAlphaBetaWithTime : ", end_test - start_test, " must be less then : ", time_limit_alpha)

"""party3 - E3 (human vs alpha match)"""
matchHumanVsAlpha(board, 3)
