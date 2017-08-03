from constants import *

class Tile:
    PLAYERS = [0, 1, 2, 3]
    EMPTY = 4
    BLOCKED = 5

    def __init__(self, _x, _y, _state, _dir):
	self.x = _x
	self.y = _y
        self.dir = _dir
	assert 0 <= _state <= 5 
	self.state = _state 
	self.tup_list = []

    def __eq__(self, other):
	return self.state == other.state

    def __getitem__(self, index):
	if index == 0:
	    return self.x
	if index == 1:
	    return self.y
	raise IndexError

