""" This module defines the type for storing game configuration. """

class GameConfig:
    num_of_players = 2
    ai_players = [None, None]
    x_size = 10
    y_size = 10

    game_type = 0

    #                0         1       2        3        4
    _dir_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0),
    #      5       6        7      8      9
        (0, 1), (1, -1), (1, 0), (1, 1), None]

    def load_shape():
        shape = []
        game_type = 0
        with open("../maps/" + str(game_type) +'.mode') as conf:
            for line in conf:
                shape.append([])
                for c in line:
                    shape[-1].append(_dir_list[c])
        x_size = len(shape[0])
        y_size = len(shape)
        return shape
