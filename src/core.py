from gameconfig import GameConfig
from grid import Grid


class Core:
    def __init__(self):
        self.grid = Grid()
        self.turn = 0

    def can_insert(self, x, y):
        """ Returns True if it is possible to put a token on self.grid[x][y],
        otherwise returns False
        """
        if(self.grid[x][y].state == Tile.EMPTY):
            return True
        return False


    def insert_token(self, x, y):
        """ Checks where a token would fall when put in grid[x][y] 
        and inserts it there. Returns True on success, False otherwise
        """
        if(self.grid[x][y].state != Tile.EMPTY):
            return False
        update_tile(x, y, self.turn)
        self.turn = (self.turn+1) % GameConfig.num_of_players
        return True
