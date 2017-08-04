from gameconfig import config
from grid import Grid
from tile import Tile

class Core:
    def __init__(self):
        Tile.configure()
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
        if not self.can_insert(x, y):
            return False
        tile = self.grid.get_token_pos(x, y)
        self.grid.update_tile(tile.x, tile.y, self.turn)
        self.turn = (self.turn+1) % config.num_of_players
        return True
