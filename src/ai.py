def minimax(core, turn, depth, x, y):
    if not depth:
        m = core.score(), x, y
        return m
    if turn:
        best = -1000000000000
        for i, j in core.valid_list:
            i, j = core.get_token_pos(i, j)
            core.grid[i][j] = turn + 1
            v = minimax(core, not turn, depth - 1, i, j)
            core.grid[i][j] = 0
            if best < v[0]:
                best, x, y = v 
        return best, x, y
    else:
        best = 1000000000000
        for i, j in core.valid_list:
            i, j = core.get_token_pos(i, j)
            core.grid[i][j] = turn + 1
            v = minimax(core, not turn, depth - 1, i, j)
            core.grid[i][j] = 0
            if best > v[0]:
                best, x, y = v
        return best, x, y
