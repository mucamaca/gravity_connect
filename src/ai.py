from score import score



def minimax(core, turn, depth):
	if not depth:
		return score(core)
	if turn:
		sign = 1
	else:
		sign = 2
	list_of_values = []
	for i,j in core.valid_list:
		if core.grid[i][j].sign == 0:
                    pos = core.get_token_pos(i, j)
		    core.grid[i][j].sign = sign
		    list_of_values.append(minimax(core, not turn, depth - 1))
		    core.grid[i][j].sign = 0

	if not turn:
            return min(list_of_values)
	else:
	    return max(list_of_values)
                                          
 
