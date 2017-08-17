from gameconfig import config

def save_game_state(grid, _file=None):
    if _file is None:
        print(repr(config)+repr(grid))
    with open(_file, 'w') as f:
        f.write(repr(config+repr(grid)))

def load_game_state(_file=None):
    if _file is None:
        l=[]
        try:
            while True:
                l.append(input())
        except EOFError:
            return ''.join(l)
    with open(_file, 'r') as f:
        return ''.join((line[:-1] for line in f))


