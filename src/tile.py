from constants import *


class Tile:
    empty = 0
    circle = 1
    cross = 2
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sign = self.empty
        
        if x == y or x + y + 1 == TABLESIZE:
            self.is_special = True
        else:
            self.is_special = False
    @staticmethod
    def where_is(x, y):
        if y < x and y + x + 1 < TABLESIZE:
            return (-1, 0)
        elif y < x and y + x + 1 > TABLESIZE:
            return (0, 1)
        elif y > x and y + x + 1 < TABLESIZE:
            return (0, -1)
        elif y > x and y + x + 1 > TABLESIZE:
            return (1, 0)
        else:
            return (0, 0)
