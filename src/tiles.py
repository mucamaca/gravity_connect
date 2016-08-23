import constants


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def where_is(self):
        if self.x < self.y and self.x + self.y < Grid.size:
            return (-1, 0)
        elif self.x < self.y and self.x + self.y > Grid.size:
            return (0, 1)
        elif self.x > self.y and self.x + self.y < Grid.size:
            return (1, 0)
        elif self.x > self.y and self.x + self.y > Grid.size:
            return (0, -1)
        else:
            return (0, 0)
        

class Token(Tile):
    cross = 1
    circle = 2
    def __init__(self, x, y, sign):
        super().__init__(x, y)
        self.sign = sign
        
        
class Square(Tile):
    empty = 0
    cross = 1
    circle = 2
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sign = self.empty
        self.inhabitor = None
        if x == y or x + y == constants.TABLESIZE:
            self.is_special = True
        else:
            self.is_special = False
        
    # @property
    # def inhabitor(self):
    #     return self._inhabitor

    # @inhabitor.setter
    # def inhabitor(self, value):
    #     if value == None:
    #         self._inhabitor = None
    #         self.sign = empty
    #     else:
    #         self._inhabitor = inhabitor
    #         self.sign = inhabitor.sign

    # @inhabitor.deletter
    # def inhabitor(self):
    #     del self._inhabitor
    
        
