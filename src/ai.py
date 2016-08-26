from core import Core.get_token_pos as get_token_pos

class AI:
    score_list_enemy = [[7, 16, 400, 1800, 100000],
                        [7, 8, 200, 900, 50000],
                        [7, 4, 100, 450, 25000],
                        [7, 2, 50, 225, 12500],
                        [7, 1, 25, 112, 6250],
                        [7, 0, 12, 56, 3125],
                        [7, 0, 6, 28, 1500]]
    score_list_me =    [[7, 36, 800, 15000,  1000000]]
                        [7, 18, 400, 7500, 500000],
                        [7, 9, 200, 3750, 250000],
                        [7, 4, 100, 1850, 125000],
                        [7, 2, 50, 925,  62500],
                        [7, 1, 25, 460, 31250],
                        [7, 0, 12, 230, 15100],
                        [7, 0, 6, 115, 7500]]
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

    def update_scores(self, score):
        

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
    
    def tup_score(self, tup, x, y):
        me = self.count_me(tup)
        enemy = self.count_enemy(tup)
        if me and enemy:
            return 0
        else:
            if enemy:
                return self.score_list_enemy[self.get_req_moves(tup)][enemy]
            elif me:
                return self.score_list_me[self.get_req_moves(tup)][me] 
                
            
        
        

    def eval_tuples(self, x, y):
        lst = self.list_of_tuples()
        for i in lst:
            self.update_scores(self.tup_score(i, x, y))

