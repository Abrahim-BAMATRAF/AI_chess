'''
party 2 - E3
creating match between MaxMin and randomMove
'''
import chess
from maxMin import gagnantAmi
from starterChess import randomMove

def match_Enemi(b, limit, MaxMinLastMove, counterMaxMin):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    b.push(randomMove(b))
    match_Ami(b, limit,MaxMinLastMove,counterMaxMin)
    b.pop()

def match_Ami(b,limit,MaxMinLastMove, counterMaxMin=0):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    move = gagnantAmi(b,limit)
    if move == MaxMinLastMove:
        move = randomMove(b)
    b.push(move)
    if counterMaxMin%2 == 0:
        match_Enemi(b, limit,move,counterMaxMin+1)
    else:
        match_Enemi(b, limit, MaxMinLastMove, counterMaxMin+1)
    b.pop()


def matchRandomVsMaxMin(b, limit):
    match_Ami(b,limit,None)

board = chess.Board()
print(matchRandomVsMaxMin(board,3))