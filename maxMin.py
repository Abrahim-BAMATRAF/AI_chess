"""
party 2 - E 3
creating the function MaxMin and Minmax with a specific depth
"""
from starterChess import randomMove
from heuristique import heuristique


'''
role: implements maxmin algorithm 
input: b: the chess board ; limit: the limit of the depth
        niv: the current depth reached by default 1 (for the first call)
output: returns the move 
'''
def gagnantAmi(b, limit, niv=1):
    bestMove = None
    if b.is_game_over():
        return heuristique(b)
    if limit == 1:
        return randomMove(b)
    if niv == limit:
        return heuristique(b)
    elif niv == 1:
        maxx = -2390
        for move in b.generate_legal_moves():
            b.push(move)
            minn = gagnantEnnemi(b, limit, niv + 1)
            b.pop()
            if minn > maxx:
                maxx = minn
                bestMove = move
        return bestMove
    else:
        maxx = -2390
        for move in b.generate_legal_moves():
            b.push(move)
            minn = gagnantEnnemi(b, limit, niv + 1)
            b.pop()
            if minn > maxx:
                maxx = minn
        return maxx


'''
role: implements minmax algorithm 
input: b: the chess board ; limit: the limit of the depth
        niv: the current depth reached by default 1 (for the first call)
output: the lowest score for ami
'''
def gagnantEnnemi(b, limit, niv=1):
    if b.is_game_over():
        return heuristique(b)
    if niv == limit:
        return heuristique(b)
    else:
        minn = 2390
        for move in b.generate_legal_moves():
            b.push(move)
            maxx = gagnantAmi(b, limit, niv + 1)
            b.pop()
            if maxx < minn:
                minn = maxx
        return minn

