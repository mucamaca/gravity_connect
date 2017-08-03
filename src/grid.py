""" This module contains definition of type Grid. """


from gameconfig import GameConfig
from tile import Tile


class Grid:
    """ This type is used to represent the current state of a game.

    It supports iterating through its tiles as a generator and accesing
    individual elements by their coordinates through subscripting.

    Although it is mutable, it supports hashing,
    so it can be used as a dict key, with different game states
    having different hash values.

    The following methods are defined:
    Grid.get_token_pos(x, y)
    Grid.update_tile(x, y, new_state)
    """

    def __init__(self):
        """ Grid object constructor. """
        self._grid = []
        self._states_list = [[] for i in range(GameConfig.num_of_players)]
        with GameConfig.load_shape() as shape:
            for x in range(GameConfig.x_size):
                self._grid.append([])
                for y in range(GameConfig.y_size):
                    if shape[x][y] is None:
                        self._grid[x].append(Tile(x, y, Tile.BLOCKED, None))
                        self._states_list[Tile.BLOCKED].append(self._grid[x][-1])
                        continue
                    self._grid[x].append(Tile(x, y, Tile.EMPTY, shape[x][y]))
                    self._states_list[Tile.EMPTY].append(self._grid[x][-1])

    def __iter__(self):
    	for row in self._grid:
    	    for tile in row:
    	        yield tile

    def __getitem__(self, index):
        return self._grid[index]

    def __hash__(self):
        """ A kind of rolling hash used to distinguish different game states. """
        s = 17
        z= 43
        h = 0
        for i, row in enumerate(self._grid):
    	    t=0
    	    for j, tile in enumerate(row):
    	        t += (tile.state + 1) * s**j
    	    h += t * z**i
        return h

    def get_token_pos(self, x, y):
        """ Returns the position where a token placed at coordinates
        specified by arguments x and y would end its path
        through the grid.
        """
        while(self[x + self[x][y].dir[0]][y + self[x][y].dir[1].state]
                != Tile.EMPTY):
            x += self[x][y].dir[0]
            y += self[x][y].dir[1]
        return self[x][y]

    def update_tile(self, x, y, new_state):
        self[x][y].state = new_state
