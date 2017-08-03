from gameconfig import config
from grid import Grid


class Core:
    def __init__(self):
        self.grid = Grid()
        self.turn = 0

    def insert_token(self, x, y):
        if(self.grid[x][y].state != Tile.EMPTY):
            return False
        update_tile(x, y, self.turn)
        self.turn = (self.turn+1) % config.num_of_players
        return True

