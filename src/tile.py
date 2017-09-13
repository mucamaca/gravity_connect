""" This module contains the definition of type Tile. """

from gameconfig import config
from tup import Tup

class Tile:
    def __init__(self, _x, _y, _state, _dir):
        """ Tile constructor

        parameters:
            _x -- x coordinate
            _y -- y coordinate
            _state -- tile state
            _dir -- direction of falling from tile
        """
        self.x = _x
        self.y = _y
        self.dir = _dir
        self.state = _state
        self.tup_list = []

    def __repr__(self):
        return "Tile({0.x!r},{0.y!r},{0.state!r},{0.dir!r})".format(self)

    def __len__(self):
        return len(self.tup_list)

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

    def get_pos(self):
        """ Return tile coordinates as a 2-tuple """
        return (self.x, self.y)

    def add_tup(self, tup):
        """ Append tup to tile's tup list """
        self.tup_list.append(tup)

    def inverted_dir(self):
        """ Return inverted direction of falling from the tile """
        return (-self.dir[0], -self.dir[1])

    def update(self, new_state):
        """ Update tile state and return change in tup values """
        old_state = self.state
        self.state = new_state
        return sum((tup.update_score(old_state, new_state) for tup in
                    self.tup_list))

    @classmethod
    def configure(cls):
        """ A classmethod that configures tiles for a number of players
        specified in config
        """
        cls.PLAYERS = list(range(config.num_of_players))
        cls.EMPTY = len(cls.PLAYERS)
        cls.BLOCKED = cls.EMPTY + 1

