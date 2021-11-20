"""
party 3 - E3
create a method to allow the user to play against alpha
"""
import chess

from alpha import gagnantAmiAlphaBeta_user


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


def matchHumanVsAlpha(b, limit):
    matchHumanVsAlpha_human(b, limit, None)
