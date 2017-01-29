from random import choice

class square:
	def __init__(self,ID,val):
		self.ID = ID
		self.value = val
		self.bigSq = self._getbigSq()
		self.smallSq = self._getsmallSq()
	def _getbigSq(self):
		#return 3*int(self.ID/27) + int((self.ID%9)/3)
		return int(self.ID/9)
	def _getsmallSq(self):
		return self.ID%9
		
		
class node:
	def __init__(self, board_data, score):
		self.board_data = board_data
		self.score = score
		self.children =[]
	
	def get_board_data(self):
		return self.board_data
	def get_score(self):
		return self.score
	def get_children(self, index):
		return self.children[index]
	
	def set_board_data(self, value):
		self.board_data = value
	def set_score(self, value):
		self.score = value
	def set_children(self, index, new_node):
		if (index < len(self.children)):
			self.children[index] = new_node
	def add_a_child(self, new_node=None):
		self.children.append(new_node)
		
	def isLeaf(self):
		if (self.children == []):
			return True
		return False
	
class Tree:
	def __init__(self):
		self.root = None
	
	def insert_node(self, node, board_data, score):
		if (self.root == None):
			self.root = node(board_data, score)
		else:
			root.add_a_child(node(board_data, score))
	
		return
	
	

def findValidMoves(squares,nextsquare):
	vm = []
	for i in range(81):
		if squares[i].bigSq==nextsquare or nextsquare>8:  #Have to play in the next square, unless you can play anywhere
			if squares[i].value == 0: #Square must be empty
				if isBoardWon(getBigBoard(squares,squares[i].bigSq))==0: #Can't play in a won board
					if not isBoardFull(getBigBoard(squares,squares[i].bigSq)): #Can't play in a full board

						vm.append(i)
	return vm

def isSmallBoardWon(state,small_board_data):
	# Return 1 if 1 won
	# Return 2 if 2 won
	# Return 0 if no on wins

	def compareSquares(s1, s2, s3, v):

		if state[small_board_data*9 +s1]==state[small_board_data*9 +s2] and state[small_board_data*9 +s1]==state[small_board_data*9 +s3] and int(state[small_board_data*9 +s1])==v:

			return True

		else:

			return False

	

	if compareSquares(0,1,2,1): return 1

	if compareSquares(0,1,2,2): return 2

	if compareSquares(3,4,5,1): return 1

	if compareSquares(3,4,5,2): return 2

	if compareSquares(6,7,8,1): return 1

	if compareSquares(6,7,8,2): return 2

	if compareSquares(0,3,6,1): return 1

	if compareSquares(0,3,6,2): return 2

	if compareSquares(1,4,7,1): return 1

	if compareSquares(1,4,7,2): return 2

	if compareSquares(2,5,8,1): return 1

	if compareSquares(2,5,8,2): return 2

	if compareSquares(0,4,8,1): return 1

	if compareSquares(0,4,8,2): return 2

	if compareSquares(2,4,6,1): return 1

	if compareSquares(2,4,6,2): return 2

	return 0

def isBoardWon(squares):
	#Input: squares = 8 item list of squares 
	#Output: 0 if not win, 1 if 1 won, 2 if 2 won
	def compareSquares(squares,s1,s2,s3,v):
		if squares[s1]==squares[s2] and squares[s1]==squares[s3] and squares[s1]==v:
			return True
		else:
			return False
	if compareSquares(squares,0,1,2,1): return 1
	if compareSquares(squares,0,1,2,2): return 2
	if compareSquares(squares,3,4,5,1): return 1
	if compareSquares(squares,3,4,5,2): return 2
	if compareSquares(squares,6,7,8,1): return 1
	if compareSquares(squares,6,7,8,2): return 2
	if compareSquares(squares,0,3,6,1): return 1
	if compareSquares(squares,0,3,6,2): return 2
	if compareSquares(squares,1,4,7,1): return 1
	if compareSquares(squares,1,4,7,2): return 2
	if compareSquares(squares,2,5,8,1): return 1
	if compareSquares(squares,2,5,8,2): return 2
	if compareSquares(squares,0,4,8,1): return 1
	if compareSquares(squares,0,4,8,2): return 2
	if compareSquares(squares,2,4,6,1): return 1
	if compareSquares(squares,2,4,6,2): return 2
	return 0
	
def isBigBoardWon(board_data):
	for board_index in range(9):
		data = ''
		cur = isSmallBoardWon(board_data[2:], board_index)
		if(cur):
			data += board_data(0)
		elif(not cur):
			data += '3'
		else:
			data += '0'

	def compareSquares(s1, s2, s3, v):
		if data[s1]==data[s2] and data[s1]==data[s3] and data[s1]==v:
			return True
		else:
			return False
	we = board_data[0];
	op = '3'
	
	if compareSquares(0,1,2,we): return True
	if compareSquares(0,1,2,op): return False
	if compareSquares(3,4,5,we): return True
	if compareSquares(3,4,5,op): return False
	if compareSquares(6,7,8,we): return True
	if compareSquares(6,7,8,op): return False
	if compareSquares(0,3,6,we): return True
	if compareSquares(0,3,6,op): return False
	if compareSquares(1,4,7,we): return True
	if compareSquares(1,4,7,op): return False
	if compareSquares(2,5,8,we): return True
	if compareSquares(2,5,8,op): return False
	if compareSquares(0,4,8,we): return True
	if compareSquares(0,4,8,op): return False
	if compareSquares(2,4,6,we): return True
	if compareSquares(2,4,6,op): return False
	return 0
	


def miniMAX(node, maximizingPlayer):
	# Return an integer
	if node.isLeaf() or (isBigBoardWon(node.board_data) != 0):
		a = node.get_board_data()
		return score(a, int(a[0]))
	
	if maximizingPlayer:
		bestValue = -10000
		for child in node.get_children():
			v = miniMax(child, False)
			node.set_score(v)
			bestValue = max(bestValue, v)
		
	else:
		bestValue = 10000
		for child in node.get_children():
			v = miniMax(child, True)
			node.set_score(v)
			bestValue = min(bestValue, v)
	
	return bestValue


def convert_big_board_to_list(state):
    list = []
    for i in range(0,9):
        list.append([])
    for i in range(0,81):
        board = int(i/9)
        #pos = i%9
        list[board].append(int(state[i])) 
    return list

def check_adj_hori(tuple, list_neutral_board):
    a, b = tuple
    if (a%3==0):    #e.g a=3 
        return (b==a+1 and a+2 in list_neutral_board) or (b == a+2 and a+1 in list_neutral_board)   #e.g.b=4 and 5 is neutral
                                                                                                    #or b=5 and 4 is neutral
    elif (a%3==1):   #a in col1
        return (b==a+1) and (a-1 in list_neutral_board)
    return False
        
def check_adj_vert(tuple, list_neutral_board):
    a, b = tuple
    if a in range(0,3): #a in row0
        return (b==a+3 and a+6 in list_neutral_board) or (b==a+6 and a+3 in list_neutral_board)
    elif a in range(3,6):    #a in row1
        return (b==a+3) and (a-3 in list_neutral_board)
    return False

def check_adj_diag(tuple, list_neutral_board):
    a, b = tuple
    if a==0:
        return (b==4 and 8 in list_neutral_board) or (b==8 and 4 in list_neutral_board)
    elif a==2:
        return (b==4 and 6 in list_neutral_board) or (b==6 and 4 in list_neutral_board)
    elif a==4:
        return (b==6 and 2 in list_neutral_board) or (b==8 and 1 in list_neutral_board)
    return False
        
            


def find_num_adj_win(list_win, list_neutral_board):
    num = 0
    list_win_tuple = convert_list_win_board_to_list_tuple(list_win)
    for tuple in list_win_tuple:
        
        if check_adj_hori(tuple, list_neutral_board):
            num += 1
            continue
        elif check_adj_vert(tuple, list_neutral_board):
            num += 1
            continue
        elif check_adj_diag(tuple, list_neutral_board):
            num += 1
    return num
        
def convert_list_win_board_to_list_tuple(list):
    list_tuple = []
    length_list = len(list)
    for i in range(length_list):
        for j in range(i+1, length_list):
            list_tuple.append((list[i],list[j]))
    return list_tuple

def utility(we, state):     #we is either 1(X) or 2(O), state is the 81 characters string
    list = convert_big_board_to_list(state)
    list_win_small_board = []   #list of small board won
    list_neutral_board = []     #list of neutral small board
    score = 0
    for coord_big in range(9):
        player = isSmallBoardWon(state, coord_big)  #player = who won the small board at coord_big(which small table)
        if player == we: 
            score += 5
            if (coord_big in [0, 2, 3, 5, 6, 8]):   #won corner board
                score += 3
            if (coord_big == 4): #won center board
                score += 10
            list_win_small_board.append(coord_big)
        elif player == 0:
            list_neutral_board.append(coord_big)
    score += find_num_adj_win(list_win_small_board, list_neutral_board)*4
    
    
    list_win_square = []    #list of win square within a small board
    list_neutral_square = []    #list of neutral square within a small board
    for i in list_neutral_board:  #i is board index i.e coord_big
        for j in range(9):  #j is index within board i.e small_coord
            if list[i][j] == we:
                if i == 4:  #any square in center
                    score += 3
                if j == 4:  #center square in any small board
                    score += 3
                list_win_square.append(j)
            elif list[i][j] == 0:   
                list_neutral_square.append(j)
        score += find_num_adj_win(list_win_square, list_neutral_square)*2
    return score

def score(state, we):
    utility1 = utility(1, state)
    utility2 = utility(2, state)
    if we == 1: #we is X
        return utility1 - utility2
    elif we == 2:
        return utility2 - utility1
	
def free_move(board_data, we):
	
	# 'board_data' is a string of length of 83
	vm = {}
	for i in range(81):
		if(board_data[i+2] == 0): # checkinh if the square is occupied or not
			tmp_board_data = board_data[:i+2] +we +board_data[i+3:] 
			vm[str(i)] = score(tmp_board_data[2:], int(tmp_board_data[0]))
	return vm

def board_modification(data, move, mover):
	# take in 83-long-string current board status "data", and index of destination (0-80) as "move"
	# "mover" is 1 if 'X' and 2 if 'O'
	# Return a new 83-long-string board status "new-board"
	new_board = data[0:move] +  mover + data[move+1:]
	return new_board	
	
def isBoardFull(squares):
	for i in range(9):
		if (squares[i]==0):
			return False
	return True

def getBigBoard(squares,bigSq):
	sq = []
	for i in range(81):
		if squares[i].bigSq == bigSq:
			sq.append(squares[i].value)
	return sq


def initialize_tree(root, move, board_data, depth, depth_counter, mover, player):
	
	
	
	#base
	if (depth_counter == depth):
		return None
	
	#expand
	depth_counter += 1
	
	#if the move results a free move
	#find all scores of the possible moves,
	#if mover is us, get max 9
	if (isSmallBoardWon(board_data[2+i*9:2+9*(i+1)])!=0):
		all_possible_mv_sc = free_move(data[2:83], mover)
		sorted_mv_sc = sorted(all_scores.items(), key=lambda all_scores: all_scores[1], reverse=(mover==player))[0:9]
		
		for i in range(9):
			new_board = board_modification(board_data, sorted_mv_sc[i], mover)
			root.add_a_child( node(new_board, 0) )
			
			#expand further into its child
			#switch player
			if (mover == "1"):
				tmp_mover = "2"
			else:
				tmp_mover = "1"
			
			initialize_tree(root.get_children(i), str(i), new_board, depth, depth_counter, tmp_mover, player)
		
	else:
		#normal moves
		for i in range(9):
			#if valid move, insert node
			if (board_data[int(move)*9+i] == "0"):

				#modify the board
				new_board = board_modification(board_data, int(move)*9+i, mover)
				root.add_a_child( node(new_board, 0) )

				#expand further into its child
				#switch player
				if (mover == "1"):
					tmp_mover = "2"
				else:
					tmp_mover = "1"



				initialize_tree(root.get_children(i), str(i), new_board, depth, depth_counter, tmp_mover, player)

			#null pointer
			else:
				root.add_a_child( )
	
	return root
	
	
def get_move(timeout,data):
	#getting input
	PLAYER=int(data[0])
	nextsquare=int(data[1])
	
	#free move or first move
	if (nextsquare == "9" or data[2:83] == "0"*81):
		all_scores = free_move(data[2:83], PLAYER)
		#get the move with highest score
		move = sorted(all_scores.items(), key=lambda all_scores: all_scores[1], reverse=True)[0]
		
	else:
		# Tree construction
		root = node(data[2:83], 0)
		root = initialize_tree(root, data[1], data[2:83], 5, 0, PLAYER)

	
	return choice(validMoves)
	






