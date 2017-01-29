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
		
class tree:

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
	
	if compareSquares(0,1,2,we): return TRUE
	if compareSquares(0,1,2,op): return FALSE
	if compareSquares(3,4,5,we): return TRUE
	if compareSquares(3,4,5,op): return FALSE
	if compareSquares(6,7,8,we): return TRUE
	if compareSquares(6,7,8,op): return FALSE
	if compareSquares(0,3,6,we): return TURE
	if compareSquares(0,3,6,op): return FALSE
	if compareSquares(1,4,7,we): return TRUE
	if compareSquares(1,4,7,op): return FALSE
	if compareSquares(2,5,8,we): return TRUE
	if compareSquares(2,5,8,op): return FALSE
	if compareSquares(0,4,8,we): return TRUE
	if compareSquares(0,4,8,op): return FALSE
	if compareSquares(2,4,6,we): return TRUE
	if compareSquares(2,4,6,op): return FALSE
	return 0

def isLeaf(node):
	# Retunr FLASE/ TRUE
	return 


def miniMAX(node, maximizingPlayer):
	# Return an integer
	if isLeaf(node) or (isBoardWon != 0):
		return get_score(node.board_data)
	
	if maximizingPlayer:
		bestValue = -10000
		for each sub_node in node.child:
			v = miniMax(sub_child, FALSE)
			node.score = v
			bestValue = max(bestValue, v)
		return bestValue
		
	else:
		bestValue = 10000
		for each sub_child in node.child:
			v = miniMax(sub_child, TRUE)
			node.score = v
			bestValue = min(bestValue, v)
		return bestValue
		
	return 


def get_score(board_data):
	# move = [0:80]
	# board_data = string
	
	return 
	# return an Integer

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


def get_move(timeout,data):
	# Tree construction
	
	# 
	PLAYER=int(data[0])
	nextsquare=int(data[1])
	squares = []
	for i in range(2,83): 
		squares.append(square(i-2,int(data[i])))
	validMoves=findValidMoves(squares,nextsquare)
	return choice(validMoves)
	






