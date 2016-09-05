from core import Core
from constants import *


score_list_enemy = [7, 16, 400, 1800, 100000]
score_list_me =    [7, 36, 800, 15000,  1000000]


def score(core, sign):
    scor = 0
    for i,j in core.valid_list:
        if core.grid[i][j] == 0:
            pos = core.get_token_pos(i, j)
        else:
            pos = (i, j)
        for k in list_of_tuples(core, *pos):
            scor += tup_score(core, k, sign)
    return scor


def count(core, tup, sign):
    _count = 0
    for i, j in tup:
        if core.grid[i][j] == sign:
            _count += 1
    return _count
           

def tup_score(core, tup, sign):
    if sign == 2:
        me = count(core, tup, 2)
        enemy = count(core, tup, 1)
    else:
        enemy = count(core, tup, 2)
        me = count(core, tup, 1)
    if me and enemy:
        return 0
    elif enemy:
        return score_list_enemy[enemy] // (2 ** get_req_moves(core, tup))
    elif me:
        return score_list_me[me] // (2 ** get_req_moves(core, tup))
    else:
        return 7


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
