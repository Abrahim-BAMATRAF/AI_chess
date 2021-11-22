"""
party 3 - E3
create a method to allow the user to play against alpha
"""
import chess
from alpha import gagnantAmiAlphaBeta_user


'''
role : reads a move given by the user
input: b: the board
output : the move
'''
def getMove(b):
    print("choose on of the legal moves")
    print("legal moves")
    print([m for m in b.generate_legal_moves()])
    move = input('Enter your move: ')
    move = chess.Move.from_uci(move)
    while not (b.is_legal(move)):
        move = input('Enter your move: ')
        move = chess.Move.from_uci(move)
    return move


# ---------human vs Alpha------------------
'''
role: plays the turn of the human
input: b: the chess board ; limit: the limit of the depth;
        AlphaLastMove: the move made by alpha in the turn before the last turn
        counterAlpha : a counter used to only memorise one move of alpha each two turns
output: void , calls matchHumanVsAlpha_alpha to give the turn to alpha
'''
def matchHumanVsAlpha_human(b, limit, AlphaLastMove, counterAlpha=0):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    move = getMove(b)
    b.push(move)
    matchHumanVsAlpha_alpha(b, limit, AlphaLastMove, counterAlpha)
    b.pop()


'''
role: plays the turn of the AI using alpha
input: b: the chess board ; limit: the limit of the depth;
        AlphaLastMove: the move made by alpha in the turn before the last turn
        counterAlpha : a counter used to only memorise one move of alpha each two turns
output: void , calls matchHumanVsAlpha_human to give the turn to alpha
'''
def matchHumanVsAlpha_alpha(b, limit, AlphaLastMove, counterAlpha=0):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    move = gagnantAmiAlphaBeta_user(b, limit)
    b.push(move)
    if counterAlpha % 2 == 0:
        matchHumanVsAlpha_human(b, limit, move, counterAlpha + 1)
    else:
        matchHumanVsAlpha_human(b, limit, AlphaLastMove, counterAlpha + 1)
    b.pop()


'''
role: starts the match by calling matchHumanVsAlpha_human
input: b: the chess board ; limit: the limit of the depth;
output: void , calls matchHumanVsAlpha_human to give the turn to alpha
'''
def matchHumanVsAlpha(b, limit):
    matchHumanVsAlpha_human(b, limit, None)
