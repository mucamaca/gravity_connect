from constants import *
from tile import Tile

class Grid:
    def __init__(self, game_options):
        shape = game_options.load_shape()
	self.x_size = game_options.x_size
	self.y_size = game_options.y_size
        self.num_of_players = game_option.num_of_players

	assert not (self.x_size % 2 or self.y_size % 2)
        self._grid = []
	self.states_list = [[] for i in range(NUM_OF_PLAYERS)]
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

    def __hash__(self):
        s = 17
	z= 43
	h = 0
	for i, row in enumerate(self._grid):
	    t=0
	    for j, tile in enumerate(row):
	        t += (tile.state + 1) * s ** j
	    h += t * z ** i
	return hash(h)
    
    def __getitem__(self, index):
        return self._grid[index]

    def get_state(self, state):
        return  self.states_list[state]

    def get_token_pos(self, x, y):
        while(self[x + self[x][y].dir[0]][y + self[x][y].dir[1].state] != Tile.EMPTY):
            x += self[x][y].dir[0]
            y += self[x][y].dir[1]
        return self[x][y]

    def update_tile(self, new_state, x, y):
        curr_state = grid[x][y].state 
        for i, tile in enumerate(self.states_list[curr_state]):
            if tile.x == x and tile.y == y:
                self.states_list[curr_state].pop(i)
                break
        self.states_list[player].append(self[x][y])
        return self[x][y].update(player)
        
    
    def tup_list(self):
	for i in range(self.x_size):
	    for j in range(self.y_size):
		if i + 5 < self.x_size:
		    yield Tup(self, (i,j), (i + 5), self.num_of_players)
		if j + 5 < self.y_size:
		    yield Tup(self, (i,j), (i, j + 5), self.num_of_players)
		if i + 5 < self.x_size and j + 5 < self.y_size:
		    yield Tup(self, (i, j), (i + 5, j + 5), self.num_of_players)



