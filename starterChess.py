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

#----------------------- party 2 - 1 ----------------------------------------
#role: perform a search to a decided level
#return : nb of (noeuds)
def search(b, limit):
    if (b.is_game_over() or limit == 0):
        return 1
    res = 0
    for move in b.generate_legal_moves():
        b.push(move)
        res += search(b, limit-1)
        b.pop()
    return res

def searchWithTime(b, limit, timeLimit=30):
    global start
    end = time.time()
    if end - start >= timeLimit:
        return 1
    if (b.is_game_over() or limit == 0):
        return 1
    res = 0
    for move in b.generate_legal_moves():
        b.push(move)
        res += searchWithTime(b, limit-1,timeLimit)
        b.pop()
    return res

#print(search(board,2))
#start = time.time()
#print(searchWithTime(board,5,2))

#-----testing

#print(gagnantAmi(board,2))

#-----------------E4-------------------------------



#-----------Partie trois----------------------------------
#-----------1-------------------------------------------




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





#----------------match alpha Vs MaxMin-----------------




#matchAlphaVsMaxMin(board,3)

#---------------------human player------------
#chess.Move.from_uci()
#board.is_legal()



#matchAlphaVsMaxMin(board,3)