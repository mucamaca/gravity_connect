from score import score


def minimax(core, turn, depth):
    sign = not turn + 1
    if not depth:
        print("score!!!")
        return score(core, sign)
    if turn:
        best = 1000000000000
        for i, j in core.valid_list:
            core.grid[i][j] = sign
            v = minimax(core, not turn, depth - 1)
            core.grid[i][j] = 0
            if best < v:
                best = v
        return best
    else:
        best = -1000000000000
        for i, j in core.valid_list:
            core.grid[i][j] = sign
            v = minimax(core, not turn, depth - 1)
            core.grid[i][j] = 0
            if best > v:
                best = v
        return best
