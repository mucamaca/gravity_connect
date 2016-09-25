from core import Core
from constants import *


score_list = [7, 16, 400, 1800, 100000]


def score(core):
    scor = 0
    for i,j in core.valid_list:
        chg = core.where_is(i, j)
        pos = list(core.get_token_pos(i, j))
        if (pos[0] != 0 and pos[1] != 0 and
            pos[0] != TABLESIZE - 1 and pos[1] != TABLESIZE - 1):
            pos[0] += chg[0]
            pos[1] += chg[1]
        for t in list_of_tuples(core, *pos):
            scor += tup_score(core, t)
        if chg != (0, 0):
            while (pos[0] != 0 and pos[1] != 0 and
                   pos[0] != TABLESIZE - 1 and pos[1] != TABLESIZE - 1):
                pos[0] += chg[0]
                pos[1] += chg[1]
                for t in list_of_tuples(core, *pos):
                    scor += tup_score(core, t)
    return scor


def count(core, tup, sign):
    _count = 0
    for i, j in tup:
        try:
            if core.grid[i][j] == sign:
                _count += 1
        except IndexError:
            print(tup)
            raise
    return _count
           

def tup_score(core, tup):
    if count(core, tup, CENTER_SIGN):
        return 0
    computer = count(core, tup, COMPUTER_SIGN)
    player = count(core, tup, PLAYER_SIGN)
    if computer and player:
        return 0
    elif player:
        return score_list[player]# // (get_req_moves(core, tup) ** 2 + 1)
    elif computer:
        return -(score_list[computer])# // (get_req_moves(core, tup) ** 2 + 1))
    else:
        return 0


def list_of_tuples(core, x, y):
    ret_val = []
    for i in range(x - 3, x + 1):
        if i >= 0 and i + 3 < TABLESIZE:
            ret_val.append(get_tuples(i, y, i + 4, y))
            
    for i in range(y - 3, y + 1):
        if i >= 0 and i + 3 < TABLESIZE:
            ret_val.append(get_tuples(x, i, x, i + 4))

    for i, j in zip(range(x - 3, x + 1), range(y - 3, y + 1)):
        if i >= 0 and j >=0 and i + 3 < TABLESIZE and j + 3 < TABLESIZE:
            ret_val.append(get_tuples(i, j, i + 4, j + 4))
                
    for i, j in zip(range(x - 3, x + 1), range(y, y - 4)):
        if i >= 0 and j - 3 >= 0 and j < TABLESIZE and i + 3 < TABLESIZE:
            ret_val.append(get_tuples(i, j, i + 4, j - 4))
    return ret_val

#working
def get_tuples(i, j, k ,l):
    if i == k:
        return list(zip([i] * abs(j - l), range(j, l)))
    elif j == l:
        return list(zip(range(i, k), [j] * abs(i - k)))
    elif j > l:
        return list(zip(range(i, k), range(j, l, -1)))
    else:
        return list(zip(range(i, k), range(j, l)))


# workin'
# can be much optimized
def get_req_moves(core, tup):
    sm = val = 0
    for x,y in tup:
        if Core.is_special(x, y):
            continue
        where_to_move = Core.where_is(x, y)
        tmp_x = x
        tmp_y = y
        val = 0
        if where_to_move[0] == -1:
            while (core.grid[tmp_x][tmp_y] == 0 and
                   tmp_x + 1):
                tmp_x -= 1
                val += 1
            sm+=val -1
            continue
        if where_to_move[1] == -1:
            while (core.grid[tmp_x][tmp_y] == 0 and
                   tmp_y + 1):
                tmp_y -= 1
                val += 1
            sm+=val - 1
            continue

        if where_to_move[0] == 1:
            while (core.grid[tmp_x][tmp_y] == 0 and
                   tmp_x + 1 < core.size):
                tmp_x += 1
                val += 1
            if tmp_x + 1 < core.size and core.grid[tmp_x][tmp_y] != 0:
                sm+= val -1                    
            else:
                sm+=val
            continue

        if where_to_move[1] == 1:
            while (core.grid[tmp_x][tmp_y] == 0 and
                   tmp_y + 1 < core.size):
                tmp_y += 1
                val += 1
            if tmp_y + 1 < core.size and core.grid[tmp_x][tmp_y] != 0:
                sm+=val-1
            else:
                sm+=val
    return sm
