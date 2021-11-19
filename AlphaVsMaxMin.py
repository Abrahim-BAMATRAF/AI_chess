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
    if move == AlphaLastMove:
        move = randomMove(b)
    b.push(move)
    if counterAlpha%2 == 0:
        matchMaxMin(b, limit,MaxMinLastMove,move,counterMaxMin,counterAlpha+1)
    else:
        matchMaxMin(b, limit, MaxMinLastMove, AlphaLastMove, counterMaxMin,counterAlpha+1)
    b.pop()


def matchAlphaVsMaxMin(b, limit):
    matchAlpha(b,limit, None, None)