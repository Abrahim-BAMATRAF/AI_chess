import chess

'''
party 2 - E 2 
creating a heuristique for the game chess folowing Claude Shannon
'''
#role : finding out the remaining pieces in the game
#output: two lists of pieces white_piece and black_piece
#precond: uppercase pieces are white , lowercase pieces are black
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
            
#role: calculate the score of each list with k=200, q=9, r=5, b=3, n= 3, p =1
#output: the score
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

#role: finding the white pawns and thier position
def getWhitePawns(b):
    whitePawns = []
    for piece in b.piece_map().items():
        car = piece[1].symbol()
        if car == 'B':
            whitePawns.append(piece)
    return whitePawns
            
    
#role: calculate the score of white pawns in relation to thier position each raw they advance increase thier score with 1
def scoreWhitePawns(whitePawns):
    score = 0
    for piece in whitePawns:
        score += piece[0]//8
    return score

#role: finding the black pawns and thier position
def getBlackPawns(b):
    blackPawns = []
    for piece in b.piece_map().items():
        car = piece[1].symbol()
        if car == 'b':
            blackPawns.append(piece)
    return blackPawns

#role: calculate the score of black pawns in relation to thier position each raw they advance increase thier score with 1
def scoreBlackPawns(blackPawns):
    score = 0
    for piece in blackPawns:
        score += piece[0]//8
    return score

#role: uses calculate_score() and scoreBlackPawns() and scoreWhitePawns() to calculate a total score for each player
#output: the difference between the scores of each player
def heuristique(b):
    white,black = get_piece(b)
    score_white = calculate_score(white)
    score_black = calculate_score(black)
    whitePawns = getWhitePawns(b)
    blackPawns = getBlackPawns(b)
    if b.turn:
        return (score_white + scoreWhitePawns(whitePawns)) - (score_black + scoreBlackPawns(blackPawns))
    else:
        return (score_black + scoreBlackPawns(blackPawns)) - (score_white + scoreWhitePawns(whitePawns))
  