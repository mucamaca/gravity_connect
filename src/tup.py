from gameconfig import config

class Tup:
    def __init__(self, grid, p1, p2):
        assert p1[0]<=p2[0]
        assert p1[1]<=p2[1]
        self.range = (p1, p2)
        self.tiles = []
        if p1[0] != p2[0]:
            dx = 1
        else:
            dx = 0
        if p1[1] != p2[1]:
            dy = 1
        else:
            dy = 0
        x, y = p1
        self.state_count = []
        self.score = 0
        self.num_of_players = config.num_of_players
        self.state_count = [0] * (self.num_of_players + 2)
        self.tiles.append(grid[x][y])
        while (x, y) != p2:
            x+=dx
            y+=dy
            self.tiles.append(grid[x][y])

        #print(p2 if p2 in [tile.get_pos() for tile in self.tiles] else None )

    def __eq__(self, other):
        return self.range == other.range or (self.range[1], self.range[0]) == other.range

    def __iter__(self):
        for tile in self.tiles:
            yield tile

    def update_score(self, old_state, new_state):
        self.state_count[old_state] -= 1
        self.state_count[new_state] += 1
        old_score = self.score
        self.score = self.get_score_from_state_count()
        return self.score - old_score


    # TODO : replace the fancy and elegant logic in this method
    #        with some faster and uglier dict from outer space
    def get_score_from_state_count(self):
        if self.state_count[1]:
            return 0
        tup_state = -1
        for i,count in enumerate(self.state_count[2:]):
            if count!= 0:
                if tup_state == -1:
                    tup_state = i
                else:
                    return 0
            if tup_state == -1:
                return -1
            return tup_state + 2
