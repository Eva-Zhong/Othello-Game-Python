


import graphics
import random
import time

class BoardInterface:
	def __init__(self):
		'''creates the window '''
		self.win = graphics.GraphWin("Othello", 620, 720)
		self.win.setCoords(-20, -20, 620, 720)
	
	def drawOriginal(self):
		'''draws original board'''
		backgroundRectangle = graphics.Rectangle(graphics.Point(-20,-20), graphics.Point(620,620))
		backgroundRectangle.setFill("black")
		backgroundRectangle.draw(self.win)
		for i in range(8):
			for j in range(8):
				box = graphics.Rectangle(graphics.Point(75*i, 75*j), graphics.Point(75*(i+1),75*(j+1)))
				box.setFill("cyan4")
				box.draw(self.win)
		self.drawCircle((3,3), "white")
		self.drawCircle((4,4), "white")
		self.drawCircle((4,3), "black")
		self.drawCircle((3,4), "black")
		#black score
		blackScore= graphics.Rectangle(graphics.Point(20,630), graphics.Point(200,690))
		blackScore.setFill("white")
		blackScore.draw(self.win)
		self.blackCircle = graphics.Circle(graphics.Point(20, 675), 30)
		self.blackCircle.setFill("black")
		self.blackCircle.setOutline("white")
		self.blackCircle.draw(self.win)
		#white score
		whiteScore= graphics.Rectangle(graphics.Point(420,630), graphics.Point(600,690))
		whiteScore.setFill("black")
		whiteScore.draw(self.win)
		self.whiteCircle = graphics.Circle(graphics.Point(420, 675), 30)
		self.whiteCircle.setFill("white")
		self.blackCircle.setOutline("white")
		self.whiteCircle.draw(self.win)
		#title
		title = graphics.Text(graphics.Point(300,660), "OTHELLO")
		title.setSize(36)
		title.setFace("courier")
		title.setFill("black")
		title.setStyle("bold")
		title.draw(self.win)
		self.score1 = None

	def getBox(self, clickPoint):
		'''This function takes the click coordinates (a point object) and converts them to the box on the grid of the board
		returns this tuple'''
		xCoor = clickPoint.getX()
		yCoor = clickPoint.getY()
		# xCoor 
		xVariable = 600//xCoor
		if xCoor >= 525:
			xVariable = 7
		elif xCoor>= 450:
			xVariable = 6
		elif xCoor >= 375:
			xVariable = 5
		elif xCoor>= 300:
			xVariable = 4
		elif xCoor >= 225:
			xVariable = 3
		elif xCoor>= 150:
			xVariable = 2
		elif xCoor >= 75:
			xVariable = 1
		else:
			xVariable = 0
		#ycoor
		if yCoor <= 75:
			yVariable = 7
		elif yCoor<=150:
			yVariable = 6
		elif yCoor<=225:
			yVariable = 5
		elif yCoor<= 300:
			yVariable = 4
		elif yCoor <= 375:
			yVariable = 3
		elif yCoor<= 450:
			yVariable = 2
		elif yCoor <= 525:
			yVariable = 1
		else:
			yVariable = 0
		square = (xVariable, yVariable)
		return square


	def coordinatesCenterPoint(self, coordinates):
		'''this function takes in a tuple that represents a box and returns a list with 4 integers 
		(x and y coordinates for each of the corner points of the square that will be effected) in order
		[x1, y1, x2, y2]
		'''
		xCoor = coordinates.getX()
		yCoor = coordinates.getY()
		x1 = 75*(xCoor)
		x2 = 75*(xCoor+1)
		centerX = (x1+x2)/2
		centerY = 637.5-75*(yCoor+1)
		centerPoint = graphics.Point(centerX, centerY)
		return centerPoint

	def drawCircle(self, coordinates, color):
		'''This function takes a list of tuples for tiles to change, a color to change them to and a window to draw in and draws these squares in that color'''
		centerPoint = self.coordinatesCenterPoint(graphics.Point(coordinates[0], coordinates[1]))
		circle = graphics.Circle(centerPoint, 35)
		
		circle.setFill(color)
		circle.draw(self.win)

		

		
	def scoreBoard(self, player1Score, player2Score):
		''' erases past score and draws new score
		'''
		if self.score1:
			self.score1.undraw()
			self.score2.undraw()
		#black
		self.score1 = graphics.Text(graphics.Point(150,660), str(player1Score))
		self.score1.setSize(36)
		self.score1.setFace("courier")
		self.score1.setFill("black")
		self.score1.setStyle("bold")
		self.score1.draw(self.win)
		#white
		self.score2 = graphics.Text(graphics.Point(550,660), str(player2Score))
		self.score2.setSize(36)
		self.score2.setFace("courier")
		self.score2.setFill("white")
		self.score2.setStyle("bold")
		self.score2.draw(self.win)

	def getLevel(self):
		'''allows a choice between 3 levels, outputs the level chosen (1, 2 or 3)
		'''
		rectangle = graphics.Rectangle(graphics.Point(-20,-20), graphics.Point(620,720))
		rectangle.setFill("darkslategrey")
		rectangle.draw(self.win)
		othello = graphics.Image(graphics.Point(300,500), "othello.gif")
		'''for i in range(30):
			randomX = random.randint(100, 500)
			randomY = random.randint(0, 500)
			if i%2 == 0:
				color = "black"
			else:
				color = "white"
			circle = graphics.Circle(graphics.Point(randomX, randomY), 50)
			circle.setFill(color)
			circle.draw(self.win)'''
		circle1 = graphics.Circle(graphics.Point(220,280), 90)
		circle1.setFill("black")
		circle1.draw(self.win)
		circle2=graphics.Circle(graphics.Point(380,280), 90)
		circle2.setFill("white")
		circle2.draw(self.win)
		circle3=graphics.Circle(graphics.Point(380,120), 90)
		circle3.setFill("black")
		circle3.draw(self.win)
		circle4=graphics.Circle(graphics.Point(220,120), 90)
		circle4.setFill("white")
		circle4.draw(self.win)
		#labels
		humanLabel = graphics.Text(graphics.Point(220,280), "Human\nvs.\nHuman")
		humanLabel.setFill("white")
		humanLabel.setFace("courier")
		humanLabel.setStyle("bold")
		humanLabel.setSize(25)
		humanLabel.draw(self.win)
		level1Label = graphics.Text(graphics.Point(380,280), "Level 1")
		level1Label.setFill("black")
		level1Label.setFace("courier")
		level1Label.setStyle("bold")
		level1Label.setSize(25)
		level1Label.draw(self.win)
		level2Label = graphics.Text(graphics.Point(380,120), "Level 3")
		level2Label.setFill("white")
		level2Label.setFace("courier")
		level2Label.setStyle("bold")
		level2Label.setSize(25)
		level2Label.draw(self.win)
		level3Label = graphics.Text(graphics.Point(220,120), "Level 2")
		level3Label.setFill("black")
		level3Label.setFace("courier")
		level3Label.setStyle("bold")
		level3Label.setSize(25)
		level3Label.draw(self.win)
		
		othello.draw(self.win)

		level = None

		while level == None:
			clickPoint = self.win.getMouse()
			if clickPoint.getX() > 130 and clickPoint.getX() < 290 and clickPoint.getY()>210 and clickPoint.getY() < 370:
				level = "human"
			elif clickPoint.getX() > 310 and clickPoint.getX() < 470 and clickPoint.getY()>210 and clickPoint.getY() < 370:
				level = "level1ComputerStrategy"
			elif clickPoint.getX() > 130 and clickPoint.getX() < 290 and clickPoint.getY()>30 and clickPoint.getY() < 190:
				level = "level2ComputerStrategy"
			elif clickPoint.getX() > 310 and clickPoint.getX() < 470 and clickPoint.getY()>30 and clickPoint.getY() < 190:
				level = "level3ComputerStrategy"
		rectangle = graphics.Rectangle(graphics.Point(-20,-20), graphics.Point(620,720))
		rectangle.setFill("white")
		rectangle.draw(self.win)

		return level

	def passMove(self, player):
		'''pass banner if no moves available, undraws after 1.5 secs'''
		if player.getColor() == "black":
			blackRectangle= graphics.Rectangle(graphics.Point(100,630), graphics.Point(200,690))
			blackRectangle.setFill("red")
			blackRectangle.draw(self.win)
			#black pass
			passMove1 = graphics.Text(graphics.Point(150,660), "PASS")
			passMove1.setSize(36)
			passMove1.setFace("courier")
			passMove1.setFill("black")
			passMove1.setStyle("bold")
			passMove1.draw(self.win)
			time.sleep(1.5)
			blackRectangle.undraw()
			passMove1.undraw()


		elif player.getColor() == "white":
			whiteRectangle= graphics.Rectangle(graphics.Point(500,630), graphics.Point(600,690))
			whiteRectangle.setFill("red")
			whiteRectangle.draw(self.win)
			#white pass
			passMove2 = graphics.Text(graphics.Point(550,660), "PASS")
			passMove2.setSize(36)
			passMove2.setFace("courier")
			passMove2.setFill("black")
			passMove2.setStyle("bold")
			passMove2.draw(self.win)
			time.sleep(1.5)
			whiteRectangle.undraw()
			passMove2.undraw()
	def turn(self, player):
		''''''
		if player.getColor() == "white":
			#draw a white circle as the background
			self.whiteTurnCircle1 = graphics.Circle(graphics.Point(420, 675), 32)
			self.whiteTurnCircle1.setFill("white")
			self.whiteTurnCircle1.setOutline("white")
			self.whiteTurnCircle1.draw(self.win)

			self.whiteTurnCircle = graphics.Circle(graphics.Point(420, 675), 20)
			self.whiteTurnCircle.setFill("white")
			self.whiteTurnCircle.setOutline("black")
			self.whiteTurnCircle.draw(self.win)
			
		elif player.getColor() == "black":
			self.whiteTurnCircle1 = graphics.Circle(graphics.Point(20, 675), 32)
			self.whiteTurnCircle1.setFill("white")
			self.whiteTurnCircle1.setOutline("white")
			self.whiteTurnCircle1.draw(self.win)
			
			self.blackTurnCircle = graphics.Circle(graphics.Point(20, 675), 20)
			self.blackTurnCircle.setFill("black")
			self.blackTurnCircle.draw(self.win)
	
	def endTurn(self, player):

		if player.getColor() == "white":
			self.whiteTurnCircle.undraw()
			self.whiteTurnCircle1.undraw()
			
			
		elif player.getColor() == "black":
			self.blackTurnCircle.undraw()
			self.whiteTurnCircle1.undraw()

	def endGameScreen(self, player1, player2):
		if  player1.getScore() != player2.getScore():
			if player1.getScore() > player2.getScore():
				winColor = player1.getColor()
			elif player1.getScore() < player2.getScore():
				winColor = player2.getColor()

			if winColor == "white":
				oppositeColor = "black"
			else:
				oppositeColor = "white"
			endRect = graphics.Rectangle(graphics.Point(100, 180), graphics.Point(500, 420))
			endRect.setFill(oppositeColor)
			endRect.draw(self.win)
			winCircle = graphics.Circle(graphics.Point(200, 320), 55)
			winCircle.setFill(winColor)
			winCircle.draw(self.win)
			winText = graphics.Text(graphics.Point(350, 320), "WINS!")
			winText.setFill(winColor)
			winText.setFace("courier")
			winText.setStyle("bold")
			winText.setSize(36)
			winText.draw(self.win)
		
		elif player1.getScore() == player2.getScore():
			endRect = graphics.Rectangle(graphics.Point(100, 180), graphics.Point(500, 420))
			endRect.setFill("white")
			endRect.setOutline("white")
			endRect.draw(self.win)
			endTriangle = graphics.Polygon(graphics.Point(100, 180),graphics.Point(100, 420), graphics.Point(500,180))
			endTriangle.setFill("black")
			endTriangle.draw(self.win)
			text1 = graphics.Text(graphics.Point(220,300), "YOU")
			text1.setFill("white")
			text1.setFace("courier")
			text1.setStyle("bold")
			text1.setSize(36)
			text1.draw(self.win)
			text2 = graphics.Text(graphics.Point(380,300), "TIE")
			text2.setFill("black")
			text2.setFace("courier")
			text2.setStyle("bold")
			text2.setSize(36)
			text2.draw(self.win)
			

		playAgainText = graphics.Text(graphics.Point(220,210), "PLAY AGAIN")
		playAgainText.setFill("cyan4")
		playAgainText.setFace("courier")
		playAgainText.setStyle("bold")
		playAgainText.setSize(20)
		playAgainText.draw(self.win)
		exitText = graphics.Text(graphics.Point(380, 210), "EXIT" )
		exitText.setFill("cyan4")
		exitText.setFace("courier")
		exitText.setStyle("bold")
		exitText.setSize(20)
		exitText.draw(self.win)	

		choice = None

		while choice == None:
			clickPoint = self.win.getMouse()
			if clickPoint.getX() > 170 and clickPoint.getX()<270 and clickPoint.getY() > 200 and clickPoint.getY() < 220:
				choice = "Play Again"
			elif clickPoint.getX()>355 and clickPoint.getX()<405 and clickPoint.getY() > 200 and clickPoint.getY() < 220:
				choice = "EXIT"
		return choice

