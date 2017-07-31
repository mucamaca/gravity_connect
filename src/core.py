    from constants import *
    from grid import Grid
    from shape_loader import load_shape


    class Core:
        size = TABLESIZE
        score_list = [0, 16, 400, 1800, 100000]
        def __init__(self, game_options=GameOptions()):

            self.num_of_players = game_options.num_of_players
            self.ai_players = game_options.ai_players
            self.grid = Grid(gametype)
            self.turn = 0

       ` 




