from gameconfig import config
from grid import Grid
from tile import Tile
import gamesave
import sys

class Core:
    def __init__(self):
        Tile.configure()
        if len(sys.argv)>1 and sys.argv[1] == '-l':
            self.grid = eval(gamesave.load_game_state(gamesave.SAVEDIR+gamesave.LASTSAVE))
        else:
            self.grid = Grid()
        self.turn = 0
        self.gameover = False

    def save(self):
        gamesave.save_game_state(self.grid, gamesave.SAVEDIR+gamesave.LASTSAVE)

    def can_insert(self, x, y):
        """ Returns True if it is possible to put a token on self.grid[x][y],
        otherwise returns False
        """
        if(self.grid[x][y].state == Tile.EMPTY and not self.gameover):
            return True
        return False

    def insert_token(self, x, y):
        """ Checks where a token would fall when put in grid[x][y]
        and inserts it there. Returns True on success, False otherwise
        """
        if not self.can_insert(x, y):
            return -1
        tile = self.grid.get_token_pos(x, y)
        self.grid.update_tile(tile.x, tile.y, self.turn)
        self.turn = (self.turn+1) % config.num_of_players
        self.gameover = self.end(x, y) 


        return self.turn if self.gameover else -1

    # def check_for_gameover(self):
    #     """ Checks for winning and tie situations in the current grid
    #     and returns True if it found any of them, False otherwise
    #     """
    #     return self.grid.check_win() != -1 or self.grid.is_full()
   
    def end(self, x, y):
        c_state = self.grid[x][y].state
        found = 0
        for i in range(1, 4):
            if x + i > 9:
                break
            elif self.grid[x + i][y].state == c_state:
                found +=1
            else:
                break
        for i in range(1, 4):
            if x - i < 0:
                break
            if self.grid[x - i][y].state == c_state:
                found +=1
            else:
                break

        if found > 2:
            return True

        found = 0

        for i in range(1, 4):
            if y + i > 9:
                break
            if self.grid[x][y + i].state == c_state:
                found +=1
            else:
                break
        for i in range(1, 4):
            if y - i < 0:
                break
            if self.grid[x][y - i].state == c_state:
                found +=1
            else:
                break

        if found > 2:
            return True

        found = 0

        for i in range(1, 4):
            if x + i > 9 or y + i > 9:
                break
            if self.grid[x + i][y + i].state == c_state:
                found += 1
            else:
                break
        for i in range(1, 4):
            if x - i < 0 or y - i < 0:
                break
            if self.grid[x - i][y - i].state == c_state:
                found += 1
            else:
                break

        if found > 2:
            return True

        found = 0
        for i in range(1, 4):
            if x + i > 9 or y - i < 0:
                break
            if self.grid[x + i][y - i].state == c_state:
                found += 1
            else:
                break
        for i in range(1, 4):
            if x - i < 0 or y + i > 9:
                break
            if self.grid[x - i][y + i].state == c_state:
                found += 1
            else:
                break

        if found > 2:
            return True

        return False
