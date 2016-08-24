from tile import Tile
from constants import *

class Core:
    size = TABLESIZE
    def __init__(self):
        self.grid = [[Tile(i, j) for i in range(self.size)]
                     for j in range(self.size)]
        self.token_to_move = None
    
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


    def insert_token(self, x, y, sign):
        token_pos = self.get_token_pos(x, y)
        self.grid[token_pos[0]][token_pos[1]].sign = sign

    def end(self, x ,y):
        c_sign = self.grid[x][y].sign
        
        for i in range(x - 3, x + 1):
            if(i >= 0 and i + 3 < TABLESIZE):
                for j in range(i, i + 4):
                    if self.grid[j][y].sign != c_sign:
                        return False
        for i in range(y - 3, y + 1):
            if(i >= 0 and i + 3 < TABLESIZE):
                for j in range(i, i + 4):
                    if self.grid[x][j].sign != c_sign:
                        return False
        for i, j in zip(range(x - 3, x + 1), range(y - 3, y + 1)):
            if i >= 0 and j >=0 and i + 3 < TABLESIZE and j + 3 < TABLESIZE:
                for k, l in zip(range(i, i + 4), range(j, j + 4)):
                    if self.grid[k][l].sign != c_sign:
                        return False
        for i, j in zip(range(x - 3, x + 1), range(y, y - 4)):
            if i >= 0 and j - 3 >= 0 and j < TABLESIZE and i + 3 < TABLESIZE:
                for k, l in zip(range(i, i + 4), range(j, j - 4)):
                    if self.grid[k][l].sign != c_sign:
                        return False
        return True
        
        
    

    
        
            
            
                
            
        
        
        
