from tile import Tile

def score(grid):
    _score = 0
    for i,j in grid.get_state(Tile.CLICKABLE):
	chg = grid.where_is(i, j)
	pos = list(get_token_pos(i, j))
	if pos not in ((0, 0), (0, grid.size - 1), 
	        (grid.size - 1, 0), (grid.size - 1, grid.size - 1)):
	    pos[0] += chg[0]
	    pos[1] += chg[1]
	for t in get_tuple_list(pos):
	    _score += get_tuple_score(t)
	if chg != (0, 0):
	    while (pos not in ((0, 0), (0, grid.size - 1), 
                    (grid.size - 1, 0), (grid.size - 1, grid.size - 1)):
		pos[0] += chg[0]
		pos[1] += chg[1]
		for t in list_of_tuples(pos):
		    _score += tup_score(t)
    return _score


def count(tup, sign):
    _count = 0
    for i, j in tup:
	if self.grid[i][j] == sign:
	    _count += 1
    return _count


def tup_score(self, tup):
    if self.count(tup, CENTER_SIGN):
	return 0
    computer = self.count(tup, COMPUTER_SIGN)
    player = self.count(tup, PLAYER_SIGN)
    if computer and player:
	return 0
    elif player:
	return -(self.score_list[player]) // (self.get_req_moves(tup) ** 2 + 1)
    elif computer:
	return self.score_list[computer] // (self.get_req_moves(tup) ** 2 + 1)
    else:
	return 0

def list_of_tuples(self, x, y):
    ret_val = []
    for i in range(x - 3, x + 1):
	if i >= 0 and i + 3 < grid.size:
	    ret_val.append(self.get_tuples(i, y, i + 4, y))

    for i in range(y - 3, y + 1):
	if i >= 0 and i + 3 < grid.size:
	    ret_val.append(self.get_tuples(x, i, x, i + 4))

    for i, j in zip(range(x - 3, x + 1), range(y - 3, y + 1)):
	if i >= 0 and j >=0 and i + 3 < grid.size and j + 3 < grid.size:
	    ret_val.append(self.get_tuples(i, j, i + 4, j + 4))

    for i, j in zip(range(x - 3, x + 1), range(y, y - 4)):
	if i >= 0 and j - 3 >= 0 and j < grid.size and i + 3 < grid.size:
	    ret_val.append(self.get_tuples(i, j, i + 4, j - 4))
    return ret_val

def get_tuples(self, i, j, k ,l):
    if i == k:
	return list(zip([i] * abs(j - l), range(j, l)))
    elif j == l:
	return list(zip(range(i, k), [j] * abs(i - k)))
    elif j > l:
	return list(zip(range(i, k), range(j, l, -1)))
    else:
	return list(zip(range(i, k), range(j, l)))

# TODO: this method can be much optimized
def get_req_moves(self, tup):
    sm = val = 0
    for x,y in tup:
	if self.is_special(x, y):
	    continue
	where_to_move = self.where_is(x, y)
	tmp_x = x
	tmp_y = y
	val = 0
	if where_to_move[0] == -1:
	    while (self.grid[tmp_x][tmp_y] == 0 and
		   tmp_x + 1):
		tmp_x -= 1
		val += 1
	    sm+=val -1
	    continue
	if where_to_move[1] == -1:
	    while (self.grid[tmp_x][tmp_y] == 0 and
		   tmp_y + 1):
		tmp_y -= 1
		val += 1
	    sm+=val - 1
	    continue

	if where_to_move[0] == 1:
	    while (self.grid[tmp_x][tmp_y] == 0 and
		   tmp_x + 1 < self.size):
		tmp_x += 1
		val += 1
	    if tmp_x + 1 < self.size and self.grid[tmp_x][tmp_y] != 0:
		sm+= val -1                    
	    else:
		sm+=val
	    continue

	if where_to_move[1] == 1:
	    while (self.grid[tmp_x][tmp_y] == 0 and
		   tmp_y + 1 < self.size):
		tmp_y += 1
		val += 1
	    if tmp_y + 1 < self.size and self.grid[tmp_x][tmp_y] != 0:
		sm+=val-1
	    else:
		sm+=val
    return sm


