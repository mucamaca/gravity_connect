""" This module contains the definition of type Tile. """

from gameconfig import GameConfig

class Tile:

    def __init__(self, _x, _y, _state, _dir):
        self.PLAYERS = list(range(GameConfig.num_of_players))
        self.EMPTY = len(self.PLAYERS)
        self.BLOCKED = self.EMPTY + 1
        self.x = _x
        self.y = _y
        self.dir = _dir
        assert 0 <= _state <= 5
        self.state = _state
        self.tup_list = []

    def __eq__(self, other):
        return self.state == other.state

    def __getitem__(self, index):
        """ This method enables accesing tile
        coordinates by subscripting the 2-tuple (x, y).
        """
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError
