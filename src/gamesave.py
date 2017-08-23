from gameconfig import config

SAVEDIR = '../saves/'
LASTSAVE = 'last.save'

def save_game_state(grid, _file=None):
    if _file is None:
        print(repr(grid))
        return
    with open(_file, 'w') as f:
        f.write(repr(grid)+'\n')

def load_game_state(_file=None):
    if _file is None:
        l=[]
        try:
            while True:
                l.append(input())
        except EOFError:
            return ''.join(l)
    with open(_file, 'r') as f:
        return ''.join((line for line in f))


