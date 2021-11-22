"""
party 2 - E3
creating match between MaxMin and randomMove
"""
from maxMin import gagnantAmi
from starterChess import randomMove

'''
role: plays the role of random in the match
input: b: the chess board ; limit: the limit of the depth;
        MaxMinLastMove: the move made by maxmin in the turn before the last turn
        counterMaxMin : a counter used to only memorise one move of maxmin each two turns
output: void , calls match_Ami to give the turn to maxmin
'''
def match_Enemi(b, limit, MaxMinLastMove, counterMaxMin):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    b.push(randomMove(b))
    match_Ami(b, limit, MaxMinLastMove, counterMaxMin)
    b.pop()


'''
role: plays the role of maxmin in the match
input: b: the chess board ; limit: the limit of the depth;
        MaxMinLastMove: the move made by maxmin in the turn before the last turn
        counterMaxMin : a counter used to only memorise one move of maxmin each two turns
output: void , calls match_Enemi to give the turn to maxmin
'''
def match_Ami(b, limit, MaxMinLastMove, counterMaxMin=0):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    move = gagnantAmi(b, limit)
    if move == MaxMinLastMove:
        move = randomMove(b)
    b.push(move)
    if counterMaxMin % 2 == 0:
        match_Enemi(b, limit, move, counterMaxMin + 1)
    else:
        match_Enemi(b, limit, MaxMinLastMove, counterMaxMin + 1)
    b.pop()


'''
role: starts the match by giving the turn two maxmin
input: b: the chess board ; limit: the limit of the depth;
output: void , calls match_Ami to give the turn to maxmin
'''
def matchRandomVsMaxMin(b, limit):
    match_Ami(b, limit, None)

