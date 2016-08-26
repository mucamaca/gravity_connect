from score import score



def minimax(core, turn, depth):
	if depth == 3:
		return score(core)
	if turn:
		sign = 1
	else:
		sign = 2
	list_of_values = []
	for i in core.valid_list:
		if core.grid[i[0]][i[1]].sign == 0:
			core.insert_token(core.get_token_pos(i[0], i[1])[0], core.get_token_pos(i[0], i[1])[1], sign)
			list_of_values.append(minimax(core, not turn, depth + 1))
			core.remove_token()

	if not turn:
		return min(list_of_values)
	else:
		return max(list_of_values)
