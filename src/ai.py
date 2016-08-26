from core import Core.get_token_pos as get_token_pos

class AI:
    score_list_me = [7, 16, 400, 1800, 100000]
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

    def tup_score(self, tup, x, y):
        no_1 = self.count_mark_1(tup)
        no_2 = self.count_mark_2(tup)
        if no_1 and no_2:
            return 0
        elif no_1 and not no_2:
            
            
        
        

    def eval_tuples(self, x, y):
        lst = self.list_of_tuples()
        for i in lst:
            self.update_scores(self.tup_score(i, x, y))

