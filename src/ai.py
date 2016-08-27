from score import score



def minimax(core, turn, depth):
    if turn:
        sign = 1
    else:
        sign = 2
    if not depth:
        print("score!!!")
        return score(core, sign)
    if turn:
        best = 1000000000000
        for i,j in core.valid_list:
            if core.grid[i][j].sign == 0:
                core.grid[i][j].sign = sign
                v = minimax(core, not turn, depth - 1)
                best = max(best, v)
                core.grid[i][j].sign = 0
        return best
    else:
        best = -1000000000000
        for i,j in core.valid_list:
            if core.grid[i][j].sign == 0:
                core.grid[i][j].sign =sign
                v = minimax(core, not turn, depth - 1)
                best = min(best, v)
        return best
