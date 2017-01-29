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
	
def isSmallBoardWon(small_board_data):
	# Return TRUE if we won
	# Return FALSE if opponent won
	# Return 0 if no on wins
	def compareSquares(s1, s2, s3, v):
		if data[small_board_data*9 +s1]==data[small_board_data*9 +s2] and data[small_board_data*9 +s1]==data[small_board_data*9 +s3] and data[small_board_data*9 +s1]==v:
			return True
		else:
			return False
	we = data[0];
	if(we == '1'): op = '2';
	else: op ='1';
	
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
	if node.isLeaf() or (isBoardWon != 0):
		return get_score(node.get_board_data())
	
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



def get_score(board_data):
	score = 0
	# board_data = string
	###	
	## giving score based on 9x9
	for board_index in range(9):
		stat = ''
		cur = isSmallBoardWon(board_index)
		if(cur): 
			score = score +5
			if(board_index == 4): score += 10
			else if(board_index in [0, 2, 6, 8]): score += 3
			#cur = "1"
			stat.append(board_index)
		else if(not cur):
			# do nothing because opponent already won this board
		else if(board_index not in [1, 3, 5, 7]):
			# when unwon board has our mark as center
			if(board_data[9*board_index +4] == board_data[1]): score += 3
			
			# when either unwon center or corner boards have our mark
			i = True
			c = 0
			while(i):
				if(board_data[9*board_index +c] == board_data[1]): 
					i = False
					if(board_index == 4): score += 2
					else if(board_index in [0, 2, 6, 8]): score += 1
				c +=1
			
		#stat += cur
		# 'stat' having 9 members is array of 9x9 board
		# True if the board is occupied by us, False if the board is occupied by opponent, and 0 if no one occupies
		
	
###
	return score
	# return an Integer
	
def free_move(board_data, we):
	
	# 'board_data' is a string of length of 83
	vm = {}
	for i in range(81):
		if(board_data(i+2) == 0): # checkinh if the square is occupied or not
			tmp_board_data = board_data[:i+2] +we +board_data[i+3:] 
			vm[str(i)] = get_score(tmp_board_data)
	return vm

def board_modification(data, move, mover):
	# take in 83-long-string current board status "data", and index of destination (0-80) as "move"
	# "mover" is 1 if 'X' and 2 if 'O'
	# Return a new 83-long-string board status "new-board"
	new_board = data[0:move] +  mover + data[move+1:]
	return new_board	
	
def isBoardFull(squares):
	for i in range(9):
		if squares[i]==0:
			return False
	return True

def getBigBoard(squares,bigSq):
	sq = []
	for i in range(81):
		if squares[i].bigSq == bigSq:
			sq.append(squares[i].value)
	return sq


def initialize_tree(root, move, board_data, depth, depth_counter, mover):
	
	#base
	if (depth_counter == depth):
		return None
	
	#expand
	depth_counter += 1
	
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
			initialize_tree(root.get_children(i), str(i), new_board, depth, depth_counter, tmp_mover)
		
		#null pointer
		else:
			root.add_a_child( )
	
	return root
	
	
def get_move(timeout,data):
	#getting input
	PLAYER=int(data[0])
	nextsquare=int(data[1])
	
	
	# Tree construction
	root = node(data[2:83], 0)
	root = initialize_tree(root, data[1], data[2:83], 5, 0, PLAYER);
	
	
	return choice(validMoves)
	






