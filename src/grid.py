"""This module contains definition of type Grid."""


from constants import *
from tile import Tile


class Grid:
    """ This type is used to represent the current state of a game.

    It supports iterating through its tiles as a generator and accesing 
    individual elements by their coordinates through subscripting.
    
    Although it is mutable, it supports hashing, 
    so it can be used as a dict key, with different game states 
    having different hash values.

    The following methods are defined:
    Grid.get_list_of_states(state)
    Grid.get_token_pos(x, y)
    Grid.update_tile(x, y, new_state)
    Grid.tup_list()
    """

    def __init__(self, game_options):
        """Grid object constructor.
        
        arguments:
        game_options -- 
        GameOptions object containing configuration used for the grid
        """

        shape = game_options.load_shape()
	self.config = game_options

        # TODO : move this assert to loader of config files
	assert not (self.x_size % 2 or self.y_size % 2)
        self._grid = []
	self.states_list = [[] for i in range(self.config.num_of_players)]
	for x in range(self.x_size):
	    self._grid.append([])
	    for y in range(self.y_size):
		if shape[x][y][0] == -42:
		    self._grid[x].append(Tile(x, y, Tile.BLOCKED, (-42, 0)))
		    self.states_list[Tile.BLOCKED].append(self._grid[x][-1])
		    continue
		self._grid[x].append(Tile(x, y, Tile.EMPTY, shape[x][y]))
		self.states_list[Tile.EMPTY].append(self._grid[x][-1])
	for tup in self.tup_list():
	    for tile in tup:
	        tile.add_tup(tup)

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
    
    def get_list_of_state(self, state):
        """ Returns a list of tiles whose state is the same as specified 
        by argument state.

        This function runs in constant time as list of tiles with the same
        state are cached and updated at each update of grid state
        """
        return  self.states_list[state]

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
        """ Changes the state of the tile at position specified by arguments
        x and y to state specified by new_state.

        Updates the score of the current grid and the lists 
        containing tiles with the same state.
        """
        curr_state = grid[x][y].state 
        for i, tile in enumerate(self.states_list[curr_state]):
            if tile.x == x and tile.y == y:
                self.states_list[curr_state].pop(i)
                break
        self.states_list[player].append(self[x][y])
        self.score += self[x][y].update(player)
    
    def tup_list(self):
        """ A generator object that yields all the tuples of tiles of length 
        required to win that can be drawn on the current grid.
        """
	for i in range(self.x_size):
	    for j in range(self.y_size):
		if i + self.win_len < self.x_size:
		    yield Tup(self, (i, j), (i + 5, j))
		if j + 5 < self.y_size:
		    yield Tup(self, (i, j), (i, j + 5))
		if i + 5 < self.x_size and j + 5 < self.y_size:
		    yield Tup(self, (i, j), (i + 5, j + 5))



