from tile import Tile
from constants import *

class Core:
    size = TABLESIZE
    def __init__(self):
        self.valid_list = []
        for i in range(TABLESIZE):
            for j in range (TABLESIZE):
                if i == j:
                    self.valid_list.append((i, j))
                    if not (i + 1 > 9 or j + 1 > 9):
                        self.valid_list.append((i+1, j))
                        self.valid_list.append((i, j+1))
                if i + j + 1 == TABLESIZE:
                    self.valid_list.append((i, j))
                    if not (i + 1 > 9 or j - 1 < 0):
                        self.valid_list.append((i+1, j))
                        self.valid_list.append((i, j-1))
        print(len(self.valid_list),
              
              self.valid_list.remove((TABLESIZE//2, TABLESIZE//2)),
              self.valid_list.remove((TABLESIZE//2-1, TABLESIZE//2)),
              self.valid_list.remove((TABLESIZE//2, TABLESIZE//2-1)),
              self.valid_list.remove((TABLESIZE//2-1,TABLESIZE//2-1)),

              self.valid_list.remove((TABLESIZE//2, TABLESIZE//2)),
              self.valid_list.remove((TABLESIZE//2-1, TABLESIZE//2)),
              self.valid_list.remove((TABLESIZE//2, TABLESIZE//2-1)),
              self.valid_list.remove((TABLESIZE//2-1,TABLESIZE//2-1)),
              len(self.valid_list)
        )
        self.grid = [[Tile(i, j) for i in range(self.size)]
                     for j in range(self.size)]

    def get_token_pos(self, x, y):
        if Tile(x, y).is_special:
            return (x, y)
        where_to_move = self.grid[x][y].where_is()
        tmp_x = x
        tmp_y = y        
        if where_to_move[0] == -1:
            while (self.grid[tmp_x][tmp_y].sign == 0 and
                   tmp_x + 1):
                tmp_x -= 1
            return (tmp_x + 1, tmp_y)

        if where_to_move[1] == -1:
            while (self.grid[tmp_x][tmp_y].sign == 0 and
                   tmp_y + 1):
                tmp_y -= 1
            return (tmp_x, tmp_y + 1)

        if where_to_move[0] == 1:
            while (self.grid[tmp_x][tmp_y].sign == 0 and
                   tmp_x + 1< self.size):
                tmp_x += 1
            if tmp_x + 1 and self.grid[tmp_x][tmp_y].sign != 0 < self.size:
                return (tmp_x - 1, tmp_y)
            else:
                return (tmp_x, tmp_y)

        if where_to_move[1] == 1:
            while (self.grid[tmp_x][tmp_y].sign == 0 and
                   tmp_y + 1 < self.size):
                tmp_y += 1
            if tmp_y + 1 and self.grid[tmp_x][tmp_y].sign != 0 < self.size:
                return (tmp_x, tmp_y - 1)
            else:
                return (tmp_x, tmp_y)

    def get_click_pos(self, x, y):
            dir = self.grid[x][y].where_is()
            for i in range(0, 4):
                if (x - i*dir[0], y - i*dir[1]) in self.valid_list:
                    return (x - i*dir[0], y - i*dir[1])

    def valid_coords(self, x, y):
        if (x, y) in self.valid_list and self.grid[x][y].sign == 0:
            return True
        return False

    def insert_token(self, x, y, sign):
        token_pos = self.get_token_pos(x, y)
        self.grid[token_pos[0]][token_pos[1]].sign = sign
        return self.end(*token_pos)            
        
    def end(self, x, y):
        c_sign = self.grid[x][y].sign
        found = 0
        
        for i in range(1, 4):
            if x + i > 9:
                break
            elif self.grid[x + i][y].sign == c_sign:
                found +=1
            else:
                break
        for i in range(1, 4):
            if x - i < 0:
                break
            if self.grid[x - i][y].sign == c_sign:
                found +=1
            else:
                break

        if found > 2:
            return True

        found = 0

        for i in range(1, 4):
            if y + i > 9:
                break
            if self.grid[x][y + i].sign == c_sign:
                found +=1
            else:
                break
        for i in range(1, 4):
            if y - i < 0:
                break
            if self.grid[x][y - i].sign == c_sign:
                found +=1
            else:
                break

        if found > 2:
            return True

        found = 0

        for i in range(1, 4):
            if x + i > 9 or y + i > 9:
                break
            if self.grid[x + i][y + i].sign == c_sign:
                found += 1
            else:
                break
        for i in range(1, 4):
            if x - i < 0 or y - i < 0:
                break
            if self.grid[x - i][y - i].sign == c_sign:
                found += 1
            else:
                break

        if found > 2:
            return True

        found = 0
        for i in range(1, 4):
            if x + i > 9 or y - i < 0:
                break
            if self.grid[x + i][y - i].sign == c_sign:
                found += 1
            else:
                break
        for i in range(1, 4):
            if x - i < 0 or y + i > 9:
                break
            if self.grid[x - i][y + i].sign == c_sign:
                found += 1
            else:
                break

        if found > 2:
            return True

        return False
