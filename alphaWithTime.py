import time
from heuristique import *
from starterChess import randomMove

'''
role: calculate alpha and beta then calls gagnantAmiAlphaBeta
input: b: the chess board ; limit: the limit of the depth;
        timeLimit: the limit of time the algo should not exceed
output: returns the move calculated by gagnantAmiAlphaBetaWithTime
precond: the global variable start must be initialized (start = time.time())
'''
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


'''
role: implements alpha beta algorithme (ami turn)
input: b: the chess board ; limit: the limit of the depth; 
        alpha : the best possible score; beta: the worst possible score
        timeLimit: the limit of time the algo should not exceed
        niv: the current depth reached by default 1 (for the first call)
output: the best possible move
precond: the global variable start must be initialized (start = time.time())
'''
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

'''
role: implements alpha beta algorithme (enemi turn)
input: b: the chess board ; limit: the limit of the depth; 
        alpha : the best possible score; beta: the worst possible score
        timeLimit: the limit of time the algo should not exceed
        niv: the current depth reached by default 1 (for the first call)
output: the lowest score for ami (the caller of gagnantAmiAlphaBeta_user)
precond: the global variable start must be initialized (start = time.time())
'''
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

