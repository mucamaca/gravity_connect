import tiles
from constants import *

class Core:
    size = TABLESIZE
    def __init__(self):
        self.grid = [[tiles.Square(i, j) for i in range(self.size)] for j in range(self.size)]
        self.token_to_move = None
    
    def get_token_pos(self, x, y):
        if tiles.Square(x, y).is_special:
            print("im special", x, y)
            return (x, y)
        where_to_move = self.grid[x][y].where_is()
        tmp_x = x
        tmp_y = y        
        if where_to_move[0] == -1:
            while self.grid[tmp_x][tmp_y].inhabitor == None and tmp_x:
                tmp_x -= 1
        elif where_to_move[0] == 1:
            while self.grid[tmp_x][tmp_y].inhabitor == None and tmp_x + 1 < self.size:
                tmp_x += 1
        elif where_to_move[1] == -1:
            while self.grid[tmp_x][tmp_y].inhabitor == None and tmp_y:
                tmp_y -= 1
        elif where_to_move[1] == 1:
            while self.grid[tmp_x][tmp_y].inhabitor == None and tmp_y + 1 < self.size:
                tmp_y += 1
        return (tmp_x, tmp_y)

    def insert_token(self, x, y, sign):
       # assert (abs(x + y - self.size) == 1 or x == y + 1 or x + 1 == y or)
        token_pos = self.get_token_pos(x, y)
        self.grid[token_pos[0]][token_pos[1]].inhabitor = tiles.Token(token_pos[0], token_pos[1], sign)


    def end(self):
        return False
    

    
        
            
            
                
            
        
        
        
