import time


# role: perform a search to a decided level
# return : nb of (noeuds)
def search(b, limit):
    if b.is_game_over() or limit == 0:
        return 1
    res = 0
    for move in b.generate_legal_moves():
        b.push(move)
        res += search(b, limit - 1)
        b.pop()
    return res


start = time.time()


def searchWithTime(b, limit, timeLimit=30, level=0):
    global start
    end = time.time()
    if end - start >= timeLimit:
        return level, True
    if b.is_game_over() or limit == 0:
        return level, False
    res = 0, False
    for move in b.generate_legal_moves():
        b.push(move)
        tmp = searchWithTime(b, limit - 1, timeLimit, level + 1)
        if res[0] < tmp[0]:
            res = tmp
        b.pop()
    return res


def searchWithTime_user(b, timeLimit=30):
    start = time.time()
    ind = 1
    res = searchWithTime(b, ind, timeLimit)
    while not res[1]:
        start = time.time()
        res = searchWithTime(b, ind, timeLimit)
        ind += 1
    return ind
