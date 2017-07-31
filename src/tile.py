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

    def __len__(self):
	return len(self.tup_list)

    def __iter__(self):
	return self.tup_list

    def __getitem__(self, index):
	if index == 0:
	    return self.x
	if index == 1:
	    return self.y
	raise IndexError


    def add_tup(self, tup):
	self.tup_list.append(tup)

    def update(self, new_state):
	old_state = self.state
	self.state = new_state
	return sum((tup.update_score(old_state, new_state) for tup in self.tup_list))
