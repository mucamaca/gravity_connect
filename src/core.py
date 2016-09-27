from constants import *

class Core:
    size = TABLESIZE
    score_list = [0, 16, 400, 1800, 100000]
    def __init__(self):
        self.valid_list = []
        for i, j in zip(range(self.size),range(self.size)):
            if i != self.size // 2 and i != self.size // 2 - 1:
                self.valid_list.append((i, j))
            if i + 1 < self.size and i + 1 != self.size // 2:
                self.valid_list.append((i+1, j))
                self.valid_list.append((i, j+1))
        for i, j in zip(range(self.size), range(self.size - 1, -1, -1)):
            if i + j + 1 == self.size and ( 
                    not self.size // 2 - 2 < j < self.size // 2 + 1):
                self.valid_list.append((i, j))
            if i + 1 < self.size and (
                    not self.size // 2 - 1 < j < self.size // 2 + 1):
                self.valid_list.append((i+1, j))
                self.valid_list.append((i, j-1))

        self.grid = [[0] * self.size for i in range(self.size)]
        self.grid[self.size // 2 - 1][self.size // 2 - 1] = CENTER_SIGN
        self.grid[self.size // 2 - 1][self.size // 2] = CENTER_SIGN
        self.grid[self.size // 2][self.size // 2 - 1] = CENTER_SIGN
        self.grid[self.size // 2][self.size // 2] = CENTER_SIGN
        
    @staticmethod    
    def is_special(x, y):
        if x == y or x + y + 1 == TABLESIZE:
            return True
        else:
            return False
    @staticmethod
    def where_is(x, y):
        if x > y and x + y < TABLESIZE - 1:
            return 0, -1
        elif x > y and x + y > TABLESIZE - 1:
            return 1, 0
        elif x < y and x + y < TABLESIZE - 1:
            return -1, 0
        elif x < y and x + y > TABLESIZE - 1:
            return 0, 1
        else:
            return 0, 0

    def get_token_pos(self, x, y):
        if self.is_special(x, y):
            return (x, y)
        where_to_move = self.where_is(x, y)
        tmp_x = x
        tmp_y = y        
        if where_to_move[0] == -1:
            while (self.grid[tmp_x][tmp_y] == 0 and
                   tmp_x + 1):
                tmp_x -= 1
            return [tmp_x + 1, tmp_y]

        if where_to_move[1] == -1:
            while (self.grid[tmp_x][tmp_y] == 0 and
                   tmp_y + 1):
                tmp_y -= 1
            return [tmp_x, tmp_y + 1]

        if where_to_move[0] == 1:
            while (self.grid[tmp_x][tmp_y] == 0 and
                   tmp_x + 1< self.size):
                tmp_x += 1
            if self.grid[tmp_x][tmp_y] != 0:
                return [tmp_x - 1, tmp_y]
            else:
                return [tmp_x, tmp_y]

        if where_to_move[1] == 1:
            while (self.grid[tmp_x][tmp_y] == 0 and
                   tmp_y + 1 < self.size):
                tmp_y += 1
            if self.grid[tmp_x][tmp_y] != 0:
                return [tmp_x, tmp_y - 1]
            else:
                return [tmp_x, tmp_y]
            
    def get_click_pos(self, x, y):
            dir = self.where_is(x, y)
            for i in range(0, 4):
                if (x - i*dir[0], y - i*dir[1]) in self.valid_list:
                    return (x - i*dir[0], y - i*dir[1])

    def valid_coords(self, x, y):
        if (x, y) in self.valid_list and self.grid[x][y] == 0:
            return True
        return False

    def insert_token(self, x, y, turn):
        self.grid[x][y] = [PLAYER_SIGN, COMPUTER_SIGN][int(turn)]

    def remove_token(self, x, y):
        self.grid[pos[0]][pos[1]] = 0            
        
    def end(self, x, y):
        c_sign = self.grid[x][y]
        found = 0
        
        for i in range(1, 4):
            if x + i > 9:
                break
            elif self.grid[x + i][y] == c_sign:
                found +=1
            else:
                break
        for i in range(1, 4):
            if x - i < 0:
                break
            if self.grid[x - i][y] == c_sign:
                found +=1
            else:
                break

        if found > 2:
            return c_sign

        found = 0

        for i in range(1, 4):
            if y + i > 9:
                break
            if self.grid[x][y + i] == c_sign:
                found +=1
            else:
                break
        for i in range(1, 4):
            if y - i < 0:
                break
            if self.grid[x][y - i] == c_sign:
                found +=1
            else:
                break

        if found > 2:
            return c_sign

        found = 0

        for i in range(1, 4):
            if x + i > 9 or y + i > 9:
                break
            if self.grid[x + i][y + i] == c_sign:
                found += 1
            else:
                break
        for i in range(1, 4):
            if x - i < 0 or y - i < 0:
                break
            if self.grid[x - i][y - i] == c_sign:
                found += 1
            else:
                break

        if found > 2:
            return c_sign

        found = 0
        for i in range(1, 4):
            if x + i > 9 or y - i < 0:
                break
            if self.grid[x + i][y - i] == c_sign:
                found += 1
            else:
                break
        for i in range(1, 4):
            if x - i < 0 or y + i > 9:
                break
            if self.grid[x - i][y + i] == c_sign:
                found += 1
            else:
                break

        if found > 2:
            return c_sign

        return False

    
    def score(self):
        scor = 0
        for i,j in self.valid_list:
            chg = self.where_is(i, j)
            pos = list(self.get_token_pos(i, j))
            if (pos[0] != 0 and pos[1] != 0 and
                pos[0] != TABLESIZE - 1 and pos[1] != TABLESIZE - 1):
                pos[0] += chg[0]
                pos[1] += chg[1]
            for t in self.list_of_tuples(*pos):
                scor += self.tup_score(t)
            if chg != (0, 0):
                while (pos[0] != 0 and pos[1] != 0 and
                       pos[0] != TABLESIZE - 1 and pos[1] != TABLESIZE - 1):
                    pos[0] += chg[0]
                    pos[1] += chg[1]
                    for t in self.list_of_tuples(*pos):
                        scor += self.tup_score(t)
        return scor


    def count(self, tup, sign):
        _count = 0
        for i, j in tup:
            if self.grid[i][j] == sign:
                _count += 1
        return _count


    def tup_score(self, tup):
        if self.count(tup, CENTER_SIGN):
            return 0
        computer = self.count(tup, COMPUTER_SIGN)
        player = self.count(tup, PLAYER_SIGN)
        if computer and player:
            return 0
        elif player:
            return -(self.score_list[player]) // (self.get_req_moves(tup) ** 2 + 1)
        elif computer:
            return self.score_list[computer] // (self.get_req_moves(tup) ** 2 + 1)
        else:
            return 0

    def list_of_tuples(self, x, y):
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

    
    def get_tuples(self, i, j, k ,l):
        if i == k:
            return list(zip([i] * abs(j - l), range(j, l)))
        elif j == l:
            return list(zip(range(i, k), [j] * abs(i - k)))
        elif j > l:
            return list(zip(range(i, k), range(j, l, -1)))
        else:
            return list(zip(range(i, k), range(j, l)))


    
    # can be much optimized
    def get_req_moves(self, tup):
        sm = val = 0
        for x,y in tup:
            if self.is_special(x, y):
                continue
            where_to_move = self.where_is(x, y)
            tmp_x = x
            tmp_y = y
            val = 0
            if where_to_move[0] == -1:
                while (self.grid[tmp_x][tmp_y] == 0 and
                       tmp_x + 1):
                    tmp_x -= 1
                    val += 1
                sm+=val -1
                continue
            if where_to_move[1] == -1:
                while (self.grid[tmp_x][tmp_y] == 0 and
                       tmp_y + 1):
                    tmp_y -= 1
                    val += 1
                sm+=val - 1
                continue

            if where_to_move[0] == 1:
                while (self.grid[tmp_x][tmp_y] == 0 and
                       tmp_x + 1 < self.size):
                    tmp_x += 1
                    val += 1
                if tmp_x + 1 < self.size and self.grid[tmp_x][tmp_y] != 0:
                    sm+= val -1                    
                else:
                    sm+=val
                continue

            if where_to_move[1] == 1:
                while (self.grid[tmp_x][tmp_y] == 0 and
                       tmp_y + 1 < self.size):
                    tmp_y += 1
                    val += 1
                if tmp_y + 1 < self.size and self.grid[tmp_x][tmp_y] != 0:
                    sm+=val-1
                else:
                    sm+=val
        return sm

