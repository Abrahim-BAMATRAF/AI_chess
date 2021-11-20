import time

from heuristique import *
from starterChess import randomMove


def gagnantAmiAlphaBetaWithTime_user(b, limit, timeLimit=10):
    white, black = get_piece(b)
    whitePawns = getWhitePawns(b)
    blackPawns = getBlackPawns(b)
    if b.turn:
        alpha = (calculate_score(white) + scoreWhitePawns(whitePawns))
        beta = -1 * (calculate_score(black) + scoreBlackPawns(blackPawns))
    else:
        alpha = (calculate_score(black) + scoreBlackPawns(blackPawns))
        beta = -1 * (calculate_score(white) + scoreWhitePawns(whitePawns))
    return gagnantAmiAlphaBetaWithTime(b, limit, alpha, beta, timeLimit)


start = time.time()


def gagnantAmiAlphaBetaWithTime(b, limit, alpha, beta, timeLimit, niv=1):
    bestMove = None
    global start
    end = time.time()
    if (end - start) >= timeLimit:
        if niv == 1:
            return randomMove(b)
        else:
            return heuristique(b)
    if b.is_game_over():
        return heuristique(b)
    if limit == 1:
        return randomMove(b)
    if niv == limit:
        return heuristique(b)
    elif niv == 1:
        maxx = -239
        for move in b.generate_legal_moves():
            b.push(move)
            minn = gagnantEnnemiAlphaBetaWithTime(b, limit, alpha, beta, timeLimit, niv + 1)
            b.pop()
            if minn > maxx:
                maxx = minn
                bestMove = move
        return bestMove
    else:
        for move in b.generate_legal_moves():
            b.push(move)
            alpha = max(alpha, gagnantEnnemiAlphaBetaWithTime(b, limit, alpha, beta, timeLimit, niv + 1))
            b.pop()
            if alpha >= beta:
                return beta
        return alpha


def gagnantEnnemiAlphaBetaWithTime(b, limit, alpha, beta, timeLimit, niv=1):
    if b.is_game_over():
        return heuristique(b)
    if niv == limit:
        return heuristique(b)
    else:
        for move in b.generate_legal_moves():
            b.push(move)
            beta = min(beta, gagnantAmiAlphaBetaWithTime(b, limit, alpha, beta, timeLimit, niv + 1))
            b.pop()
            if alpha >= beta:
                return alpha
        return beta


# ------testing-----
'''

'''
