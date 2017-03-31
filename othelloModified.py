'''
This is the game Othello
[CS111 Winter 2016]
Made by Eva Zhong and Bethany Somes
'''
import graphics
import interfaceFile
import time
import random

def generateDictionary():
	"""this function generates a blank board, sets the original color as cyan4, and sets the color 
	of the tiles in the center of the board"""

	originalBoard = {}
	for i in range(8):
		"""i is the column of the board"""
		for j in range(8):
			"""j is the row of the board"""
			position = (i, j)
			originalBoard[position] = "cyan4"

	originalBoard[3,3] = "white"
	originalBoard[3,4] = "black"
	originalBoard[4,3] = "black"
	originalBoard[4,4] = "white"
	# these lines set the color of the tiles in the center of the board

	return originalBoard

class Player:
	
	def __init__(self, color, score, strategy):
		'''
		Parameters:
		color: either black or white, the color of the player's tiles (string)
		score: the players current score (integer)
		strategy: human or computer strategy name (string)
		'''
		self.color = color
		self.score = score
		self.strategy = strategy
	
	def getScore(self):
		return self.score

	def changeScore(self, newScore):
		self.score = newScore

	def getColor(self):
		return self.color

	def getStrategy(self):
		return self.strategy



class Board:

	def __init__(self, dictionary):
		self.board = dictionary

	def getTileColor(self, position):
		# this function takes in the position(a tuple) of a tile and return its current color(which is a string)

		return self.board[position]

	def getTilePosition(self, color):
		tilePosition = []
		for position in self.board:
			if self.board[position] == color:
				tilePosition.append(position)
		return tilePosition
		# this function returns the a list of the position of the tiles that has the specific color

	def getNumColor(self, color):
		colorList = self.getTilePosition(color)
		return len(colorList)
		# this function returns the number of tiles that has the spefic color

	def modifyBoard(self, position, color):
		self.board[position] = color
		# this function modifies the board by changing the color on the entered position into the new color.

	def getBoard(self):
		return self.board


class Game:
	def __init__(self, player1, player2, interface):
		#removed board from game class
		self.player1 = player1 # a player object
		self.player2 = player2
		self.interface = interface
		#self.board = board # a board object

	def generatePossibleMoves(self, board, player):
		"""
		Algorithm:
		1. what's the color of this player
		2. generates a list of all the tiles of this color
		3. for each tile of this color, look at the eight tiles around it. If there is one(or more) tile of the other
		color, it will follow the line in which the tile of the opposite color is located. 
		4. If there is a "cyan4" in the line, saves the coordinates of the cyan4 in the "possiblemove"list.
		5. if it hits one tile of its own color, it moves on to the next tile in the list and repeat the same process.
		"""
		curColor = player.getColor()
		if curColor == "white":
			oppositeColor = "black"
		else:
			oppositeColor = "white"

		curColorPositionList = board.getTilePosition(curColor)
		possibleMovesList = []
		for item in curColorPositionList:
			originali = item[0]   # row
			originalj = item[1]   # column

			for i in range(originali-1, originali+2):  
				for j in range(originalj-1, originalj+2):

					if i >= 0 and i <= 7 and j >= 0 and j <= 7:
						if (i == originali) and (j == originalj):
							pass

						elif board.getTileColor((i,j)) != curColor and board.getTileColor((i,j)) != "cyan4":
						#Look at the 8 tiles around it and find tiles of the opposite color.
							ichange = i - originali  
							jchange = j - originalj 

							newPosition = (i+ichange, j+jchange) 
							'''this is the position of the tile along the direction'''

							#if newPosition[0] >= 0 and newPosition[0] <= 7 and newPosition[1] >= 0 and newPosition[1] <= 7:
							"""check if the tile on the new position is within the range of the board"""

								#while self.board.getTileColor(newPosition) != curColor and newPosition not in possibleMovesList:
							while newPosition[0] >= 0 and newPosition[0] <= 7 and newPosition[1] >= 0 and newPosition[1] <= 7 and board.getTileColor(newPosition) != curColor and newPosition not in possibleMovesList:
									
									if board.getTileColor(newPosition) == "cyan4":
										possibleMovesList.append(newPosition)

									else:
										newPosition = (newPosition[0]+ichange, newPosition[1]+jchange)
										"""
										if there is a cyan4 tile along the direction it's checking,
										store the position as a possible move; else, check the next 
										tile along that direction
										"""
		

		return possibleMovesList

	def checkMovePossible(self, moveCoordinates, player, board):
		# the moveCoordinates is a tuple of the player's click
		possibleMovesList = self.generatePossibleMoves(board, player)  ## confirm it!
		if moveCoordinates in possibleMovesList:
			return True
		else:
			return False

	def takeTurns(self, player, otherPlayer, board):

		"""
		1. get a click from the user
		2. call function checkMovePossible
		3. if the move is not possible, use a while loop to prompt the user to click somewhere else until the move is possible
		4. modify the board based on the user's click
		"""

		curColor = player.getColor()
		if curColor == "white":
			oppositeColor = "black"
		else:
			oppositeColor = "white"
		self.interface.turn(player)
		possibleMovesList = self.generatePossibleMoves(board, player)
		if len(possibleMovesList) > 0: #this will change to input the strategy to generate a move
			if player.getStrategy() == "human": #human strategy
				click = self.interface.win.getMouse()
				moveCoordinates = self.interface.getBox(click)
				while self.checkMovePossible(moveCoordinates, player, board) == False:
					
					click = self.interface.win.getMouse()
					moveCoordinates = self.interface.getBox(click)

			elif player.getStrategy() == "level3ComputerStrategy": #computer strategy 3
				moveCoordinates = self.level3ComputerStrategy(board, player, otherPlayer)
			elif player.getStrategy() == "level2ComputerStrategy":
				moveCoordinates = self.level2ComputerStrategy(board, player, otherPlayer) #level 2
			elif player.getStrategy() == "level1ComputerStrategy":
				moveCoordinates = self.level1ComputerStrategy(board, player, otherPlayer) 

			flipTileList = self.flippableTiles(board, player, moveCoordinates)
			board.modifyBoard(moveCoordinates, curColor)
			self.interface.drawCircle(moveCoordinates, curColor)
			time.sleep(0.2)
			for item in flipTileList:
				board.modifyBoard(item, curColor)
				self.interface.drawCircle(item, curColor)
				time.sleep(0.1)
			numCurColor = board.getNumColor(curColor)
			player.changeScore(numCurColor)
			numOtherColor = board.getNumColor(oppositeColor)
			otherPlayer.changeScore(numOtherColor)
		else:
			self.interface.passMove(player)
		self.interface.endTurn(player)




	def flippableTiles(self, board, player, moveCoordinates):
		'''This function generates a list of the tiles that should be fliped by a players move.
		Algoritm:
		1. look around this tile and find tiles of the opposite color
		2. Go along the direction of the opposite-color tile and add the positions of the opposite color into a temporary list.
		3. If it did not reach a tile of the curColor, delete the itmes in the list; if it reaches a tile of the curColor, add these positions into a "flipTileList".
		4. Do the same thing to the next tile surround it.
		5. return the list
		'''

		curColor = player.getColor()
		if curColor == "white":
			oppositeColor = "black"
		else:
			oppositeColor = "white"
		originali = moveCoordinates[0]
		originalj = moveCoordinates[1]

		flippableTileList = []
		endPointList = []
		for i in range(originali-1, originali+2):  
				for j in range(originalj-1, originalj+2):

					if i >= 0 and i <= 7 and j >= 0 and j <= 7:
						if (i == originali) and (j == originalj):
							pass

						elif board.getTileColor((i,j)) == oppositeColor:
						#Look at the 8 tiles around it and find tiles of the opposite color.
							temporaryList = []
							ichange = i -originali  
							jchange = j - originalj 
							temporaryList.append((i,j))

							newPosition = (i+ichange, j+jchange)

							'''this is the position of the tile along the direction'''

							#if newPosition[0] >= 0 and newPosition[0] <= 7 and newPosition[1] >= 0 and newPosition[1] <= 7:
							"check if the tile on the new position is within the range of the board"

								#while self.board.getTileColor(newPosition) != "cyan4" and newPosition not in endPointList:
									#if newPosition[0] >= 0 and newPosition[0] <= 7 and newPosition[1] >= 0 and newPosition[1] <= 7:	
							while newPosition[0] >= 0 and newPosition[0] <= 7 and newPosition[1] >= 0 and newPosition[1] <= 7 and board.getTileColor(newPosition) != "cyan4" and newPosition not in endPointList:
								if board.getTileColor(newPosition) == oppositeColor:
									temporaryList.append(newPosition)
									newPosition = (newPosition[0]+ichange, newPosition[1]+jchange)
								elif board.getTileColor(newPosition) == curColor:
									endPointList.append(newPosition)
									flippableTileList = flippableTileList + temporaryList
		return flippableTileList

	def level3ComputerStrategy(self,board, player, otherPlayer):
		'''Returns a tuple of coordinates with the move chosen
		ALgorithem:
		1. generate possible moves list
		2. Call other function that narrows to best possible moves
			1. check if corner --  change moves list to just be the corners
			2. check if tiles surounding the corners (that arent curColor) in list, if they are and can be eliminated from the list, eliminate them
			3. generate a newMoveDict which is a dictionary, the key will be the coordinates
		3. if only one key in dictionary, return that move
		4. for items in newMoveDict, call flippable tiles and store the number of tiles it can flip as the first value in the dictionary;  
		5. for items in newMoveDict, create a temporaryBoard(that adds the current tile and flip the flippable tiles), generate a list of possible moves for 
		the opponent.
		6. for each possible moves of the opponent, generate flippable tiles, and store the move that returns the greatest flippable tiles in the newMoveDict
		7. for each item in the dictionary, calculate the sum (value1 - value2), and return the key that has the greatest sum'''
		curColor = player.getColor()
		if curColor == "white":
				oppositeColor = "black"
		else:
			oppositeColor = "white"

		possibleMovesList = self.generatePossibleMoves(board, player)
		newPossibleMovesDict = self.narrowPossibleMovesList(board, possibleMovesList, player)
		if len(newPossibleMovesDict) == 1:
			for key in newPossibleMovesDict:
				return key #return if only one choice

		for key in newPossibleMovesDict:
			flippableTiles = self.flippableTiles(board, player, key)
			newPossibleMovesDict[key].append(len(flippableTiles))
			
			temporaryDictToCopy = board.getBoard()
			temporaryDict = temporaryDictToCopy.copy()
			temporaryBoard = Board(temporaryDict)
			temporaryBoard.modifyBoard(key, curColor)
			
			for item in flippableTiles: #changes temp board
				temporaryBoard.modifyBoard(item, curColor)
		
			opponentPossibleMoves = self.generatePossibleMoves(board, otherPlayer)
			if len(opponentPossibleMoves) == 0:
					return key #if a move doesn't let them do anything, choose it

			opponentMaxScore = 0
			for move in opponentPossibleMoves:
				opponentPoints = len(self.flippableTiles(temporaryBoard, otherPlayer, move))
					#this line returns the number of tiles the opponent can get if they choose this move
				if opponentPoints > opponentMaxScore:
					opponentMaxScore = opponentPoints
			newPossibleMovesDict[key].append(opponentMaxScore)
			newPossibleMovesDict[key].append(newPossibleMovesDict[key][0] - opponentMaxScore) #for each move: [score, opponentbest score, total ranking]
		bestScore = -100 #arbitrarily small number 
		bestMove = []
		for key in newPossibleMovesDict:
			if newPossibleMovesDict[key][2] > bestScore:
				bestScore =newPossibleMovesDict[key][2]
				bestMove = key
		return bestMove


	def narrowPossibleMovesList(self,board, possibleMovesList, player):
		'''tries to get the corner if possible
		treis to avoid letting the other player get the corner (so don't choose the squares directly next to an empty corner'''

		curColor = player.getColor()
		newMoveDict = {}
		cornersList = [(0,0), (0,7), (7,0), (7,7)]
		suroundingCornerList = [(0,1), (1,0), (1,1), (0,6), (1,6), (1,7), (6,0),(6,1), (7,1), (7,6),(6,6),(6,7)]
		for item in cornersList:
			if item in possibleMovesList:
				newMoveDict[item] = []
		if len(newMoveDict) > 0:
			return newMoveDict
		#if no corners available	
		for item in possibleMovesList:
			if item in suroundingCornerList:
				x = item[0]
				y = item[1]
				if x == 0 or 1:
					cornerX = 0
				else:
					cornerX = 7 

				if y ==0 or 1:
					cornerY = 0
				else:
					cornerY = 7
				if board.getTileColor((cornerX, cornerY)) == curColor:
					newMoveDict[item] = []	
			else:
				newMoveDict[item] = []

		if len(newMoveDict) > 0:
			return newMoveDict

		else:
			for item in possibleMovesList:
				newMoveDict[item] = []

		return newMoveDict

	def level1ComputerStrategy(self,board, player, otherPlayer):
		'''Returns a tuple of coordinates with the move chosen
		This is the easiest strategy which will randomly choose a move from the list of possible moves'''
		curColor = player.getColor()
		if curColor == "white":
				oppositeColor = "black"
		else:
			oppositeColor = "white"

		possibleMovesList = self.generatePossibleMoves(board, player)
		num = len(possibleMovesList)
		randInt = random.randint(0,num-1)
		moveCoordinates = possibleMovesList[randInt]
		return moveCoordinates

	def level2ComputerStrategy(self,board, player, otherPlayer):
		'''Returns a tuple of coordinates with the move chosen
		This is going to try to get the corner if possible, and then if not, choose the move that flips the most tiles'''
		
		curColor = player.getColor()
		if curColor == "white":
				oppositeColor = "black"
		else:
			oppositeColor = "white"
		
		cornersList = [(0,0), (0,7), (7,0), (7,7)]
		possibleMovesList = self.generatePossibleMoves(board, player)
		for item in cornersList:
			if item in possibleMovesList:
				return item
		bestMove = []
		bestNumFlips = 0
		for item in possibleMovesList:
			flippableTiles = self.flippableTiles(board, player, item)
			if len(flippableTiles) > bestNumFlips:
				bestNumFlips = len(flippableTiles)
				bestMove = item
		return bestMove
			
def main():
	boardDict = generateDictionary()
	board = Board(boardDict)
	interface = interfaceFile.BoardInterface()
	level=interface.getLevel()
	if level == "human":
		player1 = Player("black", 2, "human")
		player2 = Player("white", 2, "human")
	else:
		player1 = Player("black", 2, "human")
		player2 = Player("white", 2, level)
	interface.drawOriginal()
	
	interface.scoreBoard(player1.getScore(), player2.getScore())

	myGame = Game(player1, player2, interface)
	totalNumTile = player1.getScore() + player2.getScore()
	while totalNumTile != 64 and player1.getScore() >0 and player2.getScore() >0:
	
		myGame.takeTurns(player1, player2, board)   # player1's turn
		time.sleep(0.5)
		interface.scoreBoard(player1.getScore(), player2.getScore())
	
		myGame.takeTurns(player2, player1, board)   # player2's turn	
		time.sleep(0.5)		
		totalNumTile = player1.getScore() + player2.getScore()
		interface.scoreBoard(player1.getScore(), player2.getScore())
	choice = interface.endGameScreen(player1, player2)
	if choice == "EXIT":
		interface.win.close()
	if choice =="Play Again":
		interface.win.close()
		main()

if __name__ == '__main__':
	main()







