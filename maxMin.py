'''
party 2 - E 3
creating the function MaxMin and Minmax with a specific depth
'''
import chess
from starterChess import randomMove
from heuristique import heuristique

def gagnantAmi(b, limit, niv=1):
    bestMove = None
    if(b.is_game_over()):
        return heuristique(b)
    if(limit == 1):
        return randomMove(b)
    if(niv == limit):
        return heuristique(b)
    elif(niv == 1):
        maxx = -2390
        for move in b.generate_legal_moves():
            b.push(move)
            minn=gagnantEnnemi(b, limit, niv+1)
            b.pop()
            if minn>maxx:
                maxx=minn
                bestMove = move
        return bestMove
    else:
        maxx = -2390
        for move in b.generate_legal_moves():
            b.push(move)
            minn=gagnantEnnemi(b, limit, niv+1)
            b.pop()
            if minn>maxx:
                maxx=minn
        return maxx

def gagnantEnnemi(b, limit, niv=1):
    if(b.is_game_over()):
        return heuristique(b)
    if(niv == limit):
        return heuristique(b)
    else:
        minn = 2390
        for move in b.generate_legal_moves():
            b.push(move)
            maxx=gagnantAmi(b, limit, niv+1)
            b.pop()
            if maxx<minn:
                minn=maxx
        return minn

#---------testing-------
board = chess.Board()
print(gagnantAmi(board,3))
