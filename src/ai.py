from core import Core

class AI:
    score_list_enemy = [7, 16, 400, 1800, 100000]
    score_list_me =    [7, 36, 800, 15000,  1000000]
    init = 1

    def __init__(self, cor):
        self.core = cor

    def get_req_moves(tup):
        total = 0
        diff = []
        obs = []
        for i in range(4):
            diff[i] = abs(self.core.get_token_pos(tup[i][0], tup[i][1])[0] - tup[i][0]) + abs(self.core.get_token_pos(tup[i][0], tup[i][1])[1] + tup[i][1])
            for j in range(diff[i]):
                if self.grid[tup[i][0] + j*self.grid[tup[i][0]][tup[i][1]].where_is()[0]][tup[i][1] + j*self.grid[tup[i][0]][tup[i][1]].where_is()[1]].sign != 0:
                    obs[i] += 1
            diff[i] -= obs[i]
            total += diff[i]
        return total 

    def AI_next_move(grid, x ,y):
        self.grid = grid[:]
        eval_tuples(x, y)
        
    def get_tuples(self, i, j, k ,l):
        if i == k:
            return list(zip([i] * abs(j - l), range(j, l)))
        elif j == l:
            return list(zip(range(i, k), [j] * abs(i - k)))
        elif j > l:
            return list(zip(range(i, k), range(j, l, -1)))
        else:
            return list(zip(range(i, k), range(j, l)))

    def list_of_tuples(self, x ,y):
        ret_val = []
        for i in range(x - 3, x + 1):
            if i >= 0 and i + 3 < TABLESIZE:
                ret_val.append(self.get_tuples(i, y, i + 4, y))
                        
        for i in range(y - 3, y + 1):
            if i >= 0 and i + 3 < TABLESIZE:
                ret_val.append(self.get_tuples(x, i, x, i + 4))

        for i, j in zip(range(x - 3, x + 1), range(y - 3, y + 1)):
            if i >= 0 and j >=0 and i + 3 < TABLESIZE and j + 3 < TABLESIZE:
                ret_val.append(self.get_tuples(i, j, i + 4, j + 4))
                
        for i, j in zip(range(x - 3, x + 1), range(y, y - 4)):
            if i >= 0 and j - 3 >= 0 and j < TABLESIZE and i + 3 < TABLESIZE:
                ret_val.append(self.get_tuples(i, j, i + 4, j - 4))
        return ret_val

    def update_scores(self, tup, x, y):
        old_tup = tup_score(tup, x, y)

        pos = self.core.get_token_pos(x, y)

        self.insert_token(x, y, self.grid[pos[0]][pos[1]].sign)
        new_tup = tup_score(tup, x, y)
        self.remove_token()
        

    def count_me(self, tup):
        count = 0
        for i, j in tup:
            if self.grid[i][j].sign == self.me:
                count += 1
        return count
    
    def count_enemy(self, tup):
        count = 0
        for i, j in tup:
            if self.grid[i][j].sign == self.enemy:
                count += 1
        return count

    def proper_score(b_score, factor):
        return b_score // (2**factor)
    
    def tup_score(self, tup, x, y):
        me = self.count_me(tup)
        enemy = self.count_enemy(tup)
        if me and enemy:
            return 0
        elif enemy:
            return self.proper_score(self.score_list_enemy[enemy], self.get_req_moves(tup))
        elif me:
            return self.proper_score(self.score_list_me[me], self.get_req_moves(tup))
        else:
            if not self.init:
                raise Exception("neki je narobe")
            return 7

    def eval_tuples(self, x, y):
        lst = self.list_of_tuples(self.core.get_token_pos(x, y))
        for i in lst:
            self.update_scores(self.tup_score(i, x, y))

