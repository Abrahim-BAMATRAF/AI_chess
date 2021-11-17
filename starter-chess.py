# -*- coding: utf-8 -*-
import time
import chess
from random import randint, choice

def randomMove(b):
    '''Renvoie un mouvement au hasard sur la liste des mouvements possibles. Pour avoir un choix au hasard, il faut
    construire explicitement tous les mouvements. Or, generate_legal_moves() nous donne un itérateur.'''
    return choice([m for m in b.generate_legal_moves()])

def deroulementRandom(b):
    '''Déroulement d'une partie d'échecs au hasard des coups possibles. Cela va donner presque exclusivement
    des parties très longues et sans gagnant. Cela illustre cependant comment on peut jouer avec la librairie
    très simplement.'''
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    b.push(randomMove(b))
    deroulementRandom(b)
    b.pop()

board = chess.Board()
#deroulementRandom(board)

#-----------------------E2 - 1 ----------------------------------------------

def search(b, limit):
    if (b.is_game_over() or limit == 0):
        return 1
    res = 0
    for move in b.generate_legal_moves():
        b.push(move)
        res += search(b, limit-1)
        b.pop()
    return res

#print(search(board,3))

#-----------------------E2 - 2 ----------------------------------------------
#consedring white = Ami , black = Enemi 
test = board.piece_map().items()
#print(test)

#return 2 lists white_piece and black_piece
# if symbol = B then white (upper case)
# if symbol = b then black (lower case)
def get_piece(b):
    white_piece = []
    black_piece = []
    for piece in b.piece_map().items():
        car = piece[1].symbol()
        if(car.isupper()):
            white_piece.append(car)
        else:
            black_piece.append(car)
    return white_piece, black_piece
            

w,b =  get_piece(board)

def calculate_score(list_p):
    score = 0
    for piece in list_p:
        if(piece.lower() == 'k'):
            score += 200
        elif(piece.lower() == 'q'):
            score += 9
        elif(piece.lower() == 'r'):
            score += 5
        elif(piece.lower() == 'b'):
            score += 3
        elif (piece.lower() == 'n'):
            score += 3
        else:
            score += 1
    return score

score = calculate_score(b)
#print(score)
        
        
#return scoreWhite - scoreBlack
def heuristique(b):
    white,black = get_piece(b)
    score_white = calculate_score(white)
    score_black = calculate_score(black)
    if b.turn:
        return score_white - score_black
    else:
        return score_black - score_white


#TODO Ajoutez un moyend’exprimer qu’il est préférable d’avancer ses pions pour les mener éventuellement à la Reine
    
#-------------------E3-----------------------------------------
    
def gagnantAmi(b, limit, niv=1):
    bestMove = None
    if(b.is_game_over()):
        return heuristique(b)
    if(limit == 1):
        return randomMove(b)
    if(niv == limit):
        return heuristique(b)
    elif(niv == 1):
        maxx = -239
        for move in b.generate_legal_moves():
            b.push(move)
            minn=gagnantEnnemi(b, limit, niv+1)
            b.pop()
            if minn>maxx:
                maxx=minn
                bestMove = move
        return bestMove
    else:
        maxx = -239
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
        minn = 239
        for move in b.generate_legal_moves():
            b.push(move)
            maxx=gagnantAmi(b, limit, niv+1)
            b.pop()
            if maxx<minn:
                minn=maxx
        return minn

#-----testing

#print(gagnantAmi(board,2))

#-----------------E4-------------------------------
def match_Enemi(b, limit):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    b.push(randomMove(b))
    match_Ami(b, limit)
    b.pop()
    
def match_Ami(b,limit):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    b.push(gagnantAmi(b,limit))
    match_Enemi(b, limit)
    b.pop()

def match(b, limit):
    match_Ami(b,limit)

#match(board, 3)

#-----------Partie trois----------------------------------
#-----------1-------------------------------------------

def gagnantAmiAlphaBeta_user(b, limit):
    white, black = get_piece(board)
    if b.turn:
        alpha = calculate_score(white)
        beta = -1 * calculate_score(black)
    else:
        alpha = calculate_score(black)
        beta = -1 * calculate_score(white)
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
            alpha = max(alpha,gagnantEnnemiAlphaBeta(b, limit, alpha, beta, niv + 1))
            b.pop()
            if (alpha >= beta):
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
            beta = min(beta,gagnantAmiAlphaBeta(b, limit, alpha, beta, niv + 1))
            b.pop()
            if alpha >= beta :
                return alpha
        return beta



#--------testing time taken for research---------------
'''
start = time.time()
print(gagnantAmi(board,5))
end = time.time()
print("the time of gagnantAmi : " , end - start)
#the time of gagnantAmi :  47.63324475288391
'''

'''
start = time.time()
print(gagnantAmiAlphaBeta_user(board, 5))
end = time.time()
print("the time of gagnantAmiAvecCoupe : " , end - start)
'''
#---------2---------------------------------------------

def gagnantAmiAlphaBetaWithTime_user(b, limit, timeLimit=10):
    white, black = get_piece(board)
    if b.turn:
        alpha = calculate_score(white)
        beta = -1 * calculate_score(black)
    else:
        alpha = calculate_score(black)
        beta = -1 * calculate_score(white)
    return gagnantAmiAlphaBetaWithTime(b, limit, alpha, beta, timeLimit)

def gagnantAmiAlphaBetaWithTime(b, limit, alpha, beta, timeLimit, niv=1):
    bestMove = None
    global start
    end = time.time()
    if end - start >= timeLimit:
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
            alpha = max(alpha,gagnantEnnemiAlphaBetaWithTime(b, limit, alpha, beta, timeLimit, niv + 1))
            b.pop()
            if (alpha >= beta):
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
            beta = min(beta,gagnantAmiAlphaBetaWithTime(b, limit, alpha, beta, timeLimit, niv + 1))
            b.pop()
            if alpha >= beta :
                return alpha
        return beta

#------testing-----
'''
start_test = time.time()
start = time.time()
print(gagnantAmiAlphaBetaWithTime_user(board,5,0.008))
end_test = time.time()
print("the time of gagnantAmiAvecCoupe : " , end_test - start_test)
'''

#----------------match alpha Vs MaxMin-----------------

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


def matchAlpha(b,limit,MaxMinLastMove, AlphaLastMove, counterMaxMin=0, counterAlpha=0):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    move = gagnantAmiAlphaBeta_user(b,limit)
    if move == MaxMinLastMove:
        move = randomMove(b)
    b.push(move)
    if counterAlpha%2 == 0:
        matchMaxMin(b, limit,MaxMinLastMove,move,counterMaxMin,counterAlpha+1)
    else:
        matchMaxMin(b, limit, MaxMinLastMove, AlphaLastMove, counterMaxMin,counterAlpha+1)
    b.pop()


def matchAlphaVsMaxMin(b, limit):
    matchAlpha(b,limit, None, None)


#matchAlphaVsMaxMin(board,3)

#---------------------human player------------
#chess.Move.from_uci()
#board.is_legal()

def getMove(b):
    print("choose on of the legal moves")
    print("legal moves")
    print([ m for m in b.generate_legal_moves()] )
    move = input('Enter your move: ')
    move = chess.Move.from_uci(move)
    while not(b.is_legal(move)):
        move = input('Enter your move: ')
        move = chess.Move.from_uci(move)
    return move

#---------human vs Alpha------------------
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

def matchHumanVsAlpha_alpha(b,limit, AlphaLastMove, counterAlpha=0):
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    move = gagnantAmiAlphaBeta_user(b,limit)
    b.push(move)
    if counterAlpha%2 == 0:
        matchHumanVsAlpha_human(b, limit,move,counterAlpha+1)
    else:
        matchHumanVsAlpha_human(b, limit, AlphaLastMove,counterAlpha+1)
    b.pop()


def matchAlphaVsMaxMin(b, limit):
    matchHumanVsAlpha_human(b,limit, None)

matchAlphaVsMaxMin(board,3)