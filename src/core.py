from constants import *

class Core:
    size = TABLESIZE
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
