from score import score


def minimax(core, turn, depth, x, y):
    sign = (not turn) + 1
    if not depth:
        return score(core, sign), x, y
    if turn:
        best = 1000000000000
        for i, j in core.valid_list:
            i, j = core.get_token_pos(i, j)
            core.grid[i][j] = sign
            v = minimax(core, not turn, depth - 1, i, j)
            core.grid[i][j] = 0
            if best > v[0]:
                best, x, y = v 
        return best, x, y
    else:
        best = -1000000000000
        for i, j in core.valid_list:
            i, j = core.get_token_pos(i, j)
            core.grid[i][j] = sign
            v = minimax(core, not turn, depth - 1, i, j)
            core.grid[i][j] = 0
            if best < v[0]:
                best, x, y = v
        return best, x, y
