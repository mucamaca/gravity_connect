""" This module contains definition of type Grid. """


from gameconfig import config
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
        self._states_list = [[] for i in range(config.num_of_players + 2)]
        shape = config.load_shape()
        for x in range(config.x_size):
            self._grid.append([])
            for y in range(config.y_size):
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
        while(self[x + self[x][y].dir[0]][y + self[x][y].dir[1]].state
                != Tile.EMPTY):
            x += self[x][y].dir[0]
            y += self[x][y].dir[1]
        return self[x][y]

    def update_tile(self, x, y, new_state):
        self[x][y].state = new_state

    def check_win(self):
        """ method that checks if any of the players won """
        end = 0
        for i in range(config.x_size):
            for j in range(config.y_size):
                if i + config.win_len < config.x_size:
                    end = self._count((i, j), (i + config.win_len, j))
                    if end:
                        return end
                if j + config.win_len < config.y_size:
                    end = self._count((i, j), (i, j + config.win_len))
                    if end:
                        return end
                if i + config.win_len < config.x_size and j + config.win_len < config.y_size:
                    end = self._count((i, j), (i + config.win_len, j + config.win_len))
                    if end:
                        return end

    def _count(self, p1, p2):
        """ Method that counts occurences of different states in a tuple """

        # -1 if p2[0]<p1[0]
        #  0 if p2[0]==p1[0]
        #  1 if p2[0]>p1[0]
        dx = (p2[0] - p1[0])//config.win_len

        # -1 if p2[1]<p1[1]
        #  0 if p2[1]==p1[1]
        #  1 if p2[1]>p1[1]
        dy = (p2[1] - p1[1])//config.win_len

        x, y = p1
        state_count = [0]*(config.num_of_players + 2)
        while (x, y) != p2:
            x+=dx
            y+=dy
            state_count[self[x][y].state] += 1
        for i,j in enumerate(state_count):
            if j == config.win_len and i in Tile.PLAYERS:
                return i
        return 0
