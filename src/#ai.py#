from core import Core
from tile import Tile

score_list_enemy = [7, 16, 400, 1800, 100000]
score_list_me =    [7, 36, 800, 15000,  1000000]
init = 1

def get_req_moves(core, tup):
    sm = val = 0
    for x,y in tup:
        if Tile(x, y).is_special:
            continue
        where_to_move = core.grid[x][y].where_is()
        tmp_x = x
        tmp_y = y
        val = 0
        if where_to_move[0] == -1:
            while (core.grid[tmp_x][tmp_y].sign == 0 and
                   tmp_x + 1):
                tmp_x -= 1
                val += 1
            sm+=val -1
            continue
        if where_to_move[1] == -1:
            while (core.grid[tmp_x][tmp_y].sign == 0 and
                   tmp_y + 1):
                tmp_y -= 1
                val += 1
            sm+=val - 1
            continue

        if where_to_move[0] == 1:
            while (core.grid[tmp_x][tmp_y].sign == 0 and
                   tmp_x + 1< core.size):
                tmp_x += 1
                val += 1
            if tmp_x + 1 and core.grid[tmp_x][tmp_y].sign != 0 < core.size:
                sm+= val -1                    
            else:
                sm+=val
            continue

        if where_to_move[1] == 1:
            while (core.grid[tmp_x][tmp_y].sign == 0 and
                   tmp_y + 1 < core.size):
                tmp_y += 1
                val += 1
            if tmp_y + 1 and core.grid[tmp_x][tmp_y].sign != 0 < core.size:
                sm+=val-1
            else:
                sm+=val
        return sm


def AI_next_move(core, x, y):
    eval_tuples(core, x, y)
        
        
def get_tuples(i, j, k ,l):
    if i == k:
        return list(zip([i] * abs(j - l), range(j, l)))
    elif j == l:
        return list(zip(range(i, k), [j] * abs(i - k)))
    elif j > l:
        return list(zip(range(i, k), range(j, l, -1)))
    else:
        return list(zip(range(i, k), range(j, l)))
    
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

def update_scores(core, tup, x, y):
    old_tup = tup_score(tup, x, y)
    pos = Core.get_token_pos(x, y)
    core.insert_token(x, y, core[pos[0]][pos[1]].sign)
    new_tup = tup_score(tup, x, y)
    core.remove_token()
        

def count_me(core, tup):
    count = 0
    for i, j in tup:
        if core.grid[i][j].sign == me:
            count += 1
    return count
    
def count_enemy(core, tup):
    count = 0
    for i, j in tup:
        if core.grid[i][j].sign == enemy:
            count += 1
    return count

def proper_score(b_score, factor):
    return b_score // (2**factor)
    
def tup_score(self, tup, x, y):
    me = count_me(tup)
    enemy = count_enemy(tup)
    if me and enemy:
        return 0
    elif enemy:
        return score_list_enemy[enemy] // (2**get_req_moves(tup)
    elif me:
        return proper_score(score_list_me[me], get_req_moves(tup))
    else:
        if not self.init:
            raise Exception("neki je narobe")
        return 7

def eval_tuples(core, x, y):
    lst = list_of_tuples(Core.get_token_pos(x, y))
    for i in lst:
        update_scores(tup_score(core, i, x, y))

