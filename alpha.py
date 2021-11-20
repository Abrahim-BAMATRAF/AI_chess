'''
party 3 - E1
implementing alpha beta method 
'''

from heuristique import *
from starterChess import randomMove


# role: calculate alpha and beta then calls gagnantAmiAlphaBeta
def gagnantAmiAlphaBeta_user(b, limit):
    white, black = get_piece(b)
    whitePawns = getWhitePawns(b)
    blackPawns = getBlackPawns(b)
    if b.turn:
        alpha = (calculate_score(white) + scoreWhitePawns(whitePawns))
        beta = -1 * (calculate_score(black) + scoreBlackPawns(blackPawns))
    else:
        alpha = (calculate_score(black) + scoreBlackPawns(blackPawns))
        beta = -1 * (calculate_score(white) + scoreWhitePawns(whitePawns))
    return gagnantAmiAlphaBeta(b, limit, alpha, beta)


def gagnantAmiAlphaBeta(b, limit, alpha, beta, niv=1):
    bestMove = None
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
            minn = gagnantEnnemiAlphaBeta(b, limit, alpha, beta, niv + 1)
            b.pop()
            if minn > maxx:
                maxx = minn
                bestMove = move
        return bestMove
    else:
        for move in b.generate_legal_moves():
            b.push(move)
            alpha = max(alpha, gagnantEnnemiAlphaBeta(b, limit, alpha, beta, niv + 1))
            b.pop()
            if alpha >= beta:
                return beta
        return alpha


def gagnantEnnemiAlphaBeta(b, limit, alpha, beta, niv=1):
    if b.is_game_over():
        return heuristique(b)
    if niv == limit:
        return heuristique(b)
    else:
        for move in b.generate_legal_moves():
            b.push(move)
            beta = min(beta, gagnantAmiAlphaBeta(b, limit, alpha, beta, niv + 1))
            b.pop()
            if alpha >= beta:
                return alpha
        return beta
