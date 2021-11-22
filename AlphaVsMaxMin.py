from alpha import gagnantAmiAlphaBeta_user
from maxMin import gagnantAmi
from starterChess import randomMove

'''
role: plays one move using maxmin (gagnantAmi) to decide this move
input: b: the chess board ; limit: the limit of the depth;
        MaxMinLastMove: the move made by maxmin in the turn before the last turn
        AlphaLastMove: the move made by alpha in the turn before the last turn
        (these two parametre used to avoid loops in the movement chosen by maxmin and alpha)
        counterMaxMin : a counter used to only memorise one move of maxmin each two turns
        counterAlpha : a counter used to only memorise one move of alpha each two turns
output: void , calls matchAlpha to give the turn to alpha
'''
def matchMaxMin(b, limit,MaxMinLastMove, AlphaLastMove, counterMaxMin=0, counterAlpha=0):
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
        matchAlpha(b, limit, move, AlphaLastMove, counterMaxMin+1,counterAlpha)
    else:
        matchAlpha(b, limit, MaxMinLastMove, AlphaLastMove, counterMaxMin+1,counterAlpha)
    b.pop()

'''
role: plays one move using alpha (gagnantAmiAlphaBeta_user) to decide this move
input: b: the chess board ; limit: the limit of the depth;
        MaxMinLastMove: the move made by maxmin in the turn before the last turn
        AlphaLastMove: the move made by alpha in the turn before the last turn
        (these two parametre used to avoid loops in the movement chosen by maxmin and alpha)
        counterMaxMin : a counter used to only memorise one move of maxmin each two turns
        counterAlpha : a counter used to only memorise one move of alpha each two turns
output: void , calls matchMaxMin to give the turn to alpha
'''
def matchAlpha(b,limit,MaxMinLastMove, AlphaLastMove, counterMaxMin=0, counterAlpha=0):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    move = gagnantAmiAlphaBeta_user(b,limit)
    if move == AlphaLastMove:
        move = randomMove(b)
    b.push(move)
    if counterAlpha%2 == 0:
        matchMaxMin(b, limit,MaxMinLastMove,move,counterMaxMin,counterAlpha+1)
    else:
        matchMaxMin(b, limit, MaxMinLastMove, AlphaLastMove, counterMaxMin,counterAlpha+1)
    b.pop()


'''
role: starts the match by giving the turn two matchAlpha
input: b: the chess board ; limit: the limit of the depth;
output: void , calls matchAlpha to give the turn to alpha
'''
def matchAlphaVsMaxMin(b, limit):
    matchAlpha(b,limit, None, None)