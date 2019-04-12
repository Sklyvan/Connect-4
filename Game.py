from Tools import GameTools
from Matrix import Matrix
from Board import Board
from LinkedList import LinkedList
from Artificial_Inteligence import RandomIA
import turtle


class MainGame:

    def __init__(self, nColumns, nRows):
        # That's the main game, here is where I initialize the tools.
        MainBoard = Board(nColumns, nRows) # Drawing the board.
        MainMatrix = Matrix(nColumns, nRows) # Creating matrix to save game data.
        myTools = GameTools() # I use that to read game data.
        playerStarter = myTools.randomStarter() # Using a tool to alternate the players.
        myPlayers = LinkedList() # Using a Linked List to save players movements.
        myPlayers.append(playerStarter) # Adding the first player movement.

        def getScreenClick(x, y): # Using that to read where is the player clicking.
            clickChecker = False
            buttonClick = None
            """Saving and Reading data methods are a little complicated, so they are explained where we create them.
            Also, there's an option when we are saving game data, if we introduce "Desk" as the saving location, it automatically goes to the desktop.
            That's just working for my desktop.
            """
            if x >= 320 and x <= 570:
                if y <= -26 and y >= -123:
                    clickChecker = True
                    buttonClick = True
                    # IA Mode Button.
                    # Basicaly restarting everything if the player clicked here. Matrix, Board and Linked List, once I did it, I'm getting a new first player.
                    # Then starts the game with the IA.
                    EasyIA = RandomIA(nColumns, nRows, MainMatrix)
                    MainBoard.Restart(6, 6, 2)
                    MainMatrix.Restart(6, 6)
                    myPlayers.clear()
                    playerStarter = myTools.randomStarter()
                    myPlayers.append(playerStarter)
                    turtle.onscreenclick(getScreenClick)

                elif y <= 100 and y >= 2:
                    clickChecker = True
                    buttonClick = True
                    # Restart Game Button.
                    # Basicaly restarting everything if the player clicked here. Matrix, Board and Linked List, once I did it, I'm getting a new first player.
                    if not MainMatrix.isEmpty(): # If the Game Matrix is empty, I don't restart the game.
                        MainBoard.Restart(6, 6, 1)
                        MainMatrix.Restart(6, 6)
                        myPlayers.clear()
                        playerStarter = myTools.randomStarter()
                        myPlayers.append(playerStarter)
                        turtle.onscreenclick(getScreenClick)

                elif y <= -275 and y >= -373:
                    clickChecker = True
                    buttonClick = True
                    # Save Data button clicked.
                    Path = turtle.textinput("Save Game Data.", "Where you want to save your data?") # That's creating a text window to the user, asking for the path.
                    auxLoop = True # Using this loop to repeat the window if the player puts a wrong save location.
                    while auxLoop is True:
                        """There's a bug that I can't solve. I don't know if I'm doing something wrong but I can't fix it.
                        If the user closes the input window, the turtle screen breaks, without showing any exception, just freezing it."""
                        if Path is not None: # Checking that input is not empty.
                            if Path == "Desk": # Developer option, just to make testing easier.
                                MainMatrix.saveGame("C:\\Users\joang\Desktop\DevGameData.dat", myPlayers) # Using my own method from my ADT Matrix.
                                auxLoop = False # Closing loop.
                            else:
                                try:
                                    Path += str("\GameData.dat") # Adding the name of the Data File.
                                    MainMatrix.saveGame(Path, myPlayers) # Using my own method from my ADT Matrix.
                                    auxLoop = False # Closing loop.
                                except: # If the user introduced a wrong location, Python is going to raise an Exeption, so if it happens, I'm showing the same window again.
                                    Path = turtle.textinput("Save Game Data.", "Wrong location, try again.")

                elif y <= -151 and y >= -248:
                    clickChecker = True
                    buttonClick = True
                    # Load Data button clicked.
                    Path = turtle.textinput("Load Game Data.", "Where is your game data stored?") # That's creating a text window to the user, asking for the path.
                    auxLoop = True # Using this loop to repeat the window if the player puts a wrong load data location.
                    while auxLoop is True:
                        """There's a bug that I can't solve. I don't know if I'm doing something wrong but I can't fix it.
                        If the user closes the input window, the turtle screen breaks, without showing any exception, just freezing it."""
                        if Path is not None: # Checking that input is not empty.
                            if Path == "Desk": # Developer option, just to make testing easier.
                                # Using my own tool to read the content of a .dat File, so it's returning two things, the Game Matrix, and the last player who clicked.
                                loadedMatrix = myTools.readData("C:\\Users\joang\Desktop\DevGameData.dat")[0]
                                lastMove = myTools.readData("C:\\Users\joang\Desktop\DevGameData.dat")[1]
                                # At that point, we have the game Matrix, so we are just creating a new Game Matrix, reading the text file.
                                for i in range(nColumns):
                                    for j in range(nRows):
                                        tempValue = loadedMatrix[i][j]
                                        MainMatrix.addValue(i, j, tempValue)
                                auxLoop = False # Closing the loop.
                            else:
                                try:
                                    # Using my own tool to read the content of a .dat File, so it's returning two things, the Game Matrix, and the last player who clicked.
                                    loadedMatrix = myTools.readData("C:\\Users\joang\Desktop\DevGameData.dat")[0]
                                    lastMove = myTools.readData("C:\\Users\joang\Desktop\DevGameData.dat")[1]
                                    # At that point, we have the game Matrix, so we are just creating a new Game Matrix, reading the text file.
                                    for i in range(nColumns):
                                        for j in range(nRows):
                                            tempValue = loadedMatrix[i][j]
                                            MainMatrix.addValue(i, j, tempValue)
                                    auxLoop = False # Closing the loop.
                                except: # If the user introduced a wrong location, Python is going to raise an Exeption, so if it happens, I'm showing the same window again.
                                    Path = turtle.textinput("Load Game Data.", "Wrong location, try again.")
                    MainBoard.Restart(6, 6, 1) # Clearing the screen.
                    MainMatrix.convertToGame() # That's drawing the matrix on the Game Board.
                    myPlayers.clear() # Clearing if there's any old moves.
                    myPlayers.append(lastMove) # Adding loaded game last move to the Linked List.
                    # Now I'm checking if there's a win, maybe I'm changing that soon, so I add on the Data File a Boolean indicating who has won the game.
                    if MainMatrix.checkVictory(1) is True: # Player One Victory.
                        MainBoard.WinnerText(1)
                    elif MainMatrix.checkVictory(2) is True: # Player Two Victory.
                        MainBoard.WinnerText(2)
                    elif MainMatrix.fullMatrix() is True: # Draw.
                        MainBoard.WinnerText(3)
                    else:
                        turtle.onscreenclick(getScreenClick)

            else: # If the player clicked on the Game Board, then...
                buttonClick = False
                if y <= 302 and y >= -302:
                    if x >= -550 and x <= 150:
                        clickChecker = True # Later, using that to be sure that the user clicked inside the Game Board.

            vPlayerOne = MainMatrix.checkVictory(1)[0] # Getting just if player one has won the game.
            vPlayerTwo = MainMatrix.checkVictory(2)[0] # Getting just if player two has won the game.

            if clickChecker is True and vPlayerOne is False and vPlayerTwo is False and MainMatrix.fullMatrix() is False: # If we are able to continue playing.
                if buttonClick is False: # If the player clicked into the board.
                    if myPlayers.last.data == 1: # If the last Linked List node is 1, player one is clicking, so I draw a token on the board.
                        # Not using the 'y' because the high depends on the game status.
                        createToken(x, 1)
                    else: # If the last Linked List node is 1, player one is clicking, so I draw a token on the board.
                        # Not using the 'y' because the high depends on the game status.
                        createToken(x, 2)

            elif MainMatrix.fullMatrix() is True: # If there's a draw, print draw text.
                MainBoard.WinnerText(3)

        def createToken(x, playerActing): # Function that creates a token depending where the player clicked.
            # Algorithm = -(Aux * 100) + K
            clickChecker = False
            K = 250

            # That's not drawing into the board, just converting the click positions, adding values to the Matrix and creating next move on the Linked List.
            if x >= -550 and x <= -452: # If the player clicked into column one.
                Aux = MainMatrix.getColumnState(1) # Getting how's the column to know where I have to draw the token.
                if Aux is not False: # If column is not full.
                    yPosition = -(Aux * 100) + K # Getting the high with a simply algorithm.
                    xPosition = -450 # x Position is a constant, since it depends on the column where the player clicked.
                    MainMatrix.addValue(Aux, 0, playerActing) # Adding the value to the matrix.
                    clickChecker = True
                    # Now adding the next move to the linked list.
                    if playerActing == 1:
                        myPlayers.append(2)
                    else:
                        myPlayers.append(1)

            if x >= -452 and x <= -353:
                Aux = MainMatrix.getColumnState(2)
                if Aux is not False:
                    yPosition = -(Aux * 100) + K
                    xPosition = -350
                    MainMatrix.addValue(Aux, 1, playerActing)
                    clickChecker = True
                    if playerActing == 1:
                        myPlayers.append(2)
                    else:
                        myPlayers.append(1)

            if x >= -353 and x <= -250:
                Aux = MainMatrix.getColumnState(3)
                if Aux is not False:
                    yPosition = -(Aux * 100) + K
                    xPosition = -250
                    MainMatrix.addValue(Aux, 2, playerActing)
                    clickChecker = True
                    if playerActing == 1:
                        myPlayers.append(2)
                    else:
                        myPlayers.append(1)

            if x >= -250 and x <= -153:
                Aux = MainMatrix.getColumnState(4)
                if Aux is not False:
                    yPosition = -(Aux * 100) + K
                    xPosition = -150
                    MainMatrix.addValue(Aux, 3, playerActing)
                    clickChecker = True
                    if playerActing == 1:
                        myPlayers.append(2)
                    else:
                        myPlayers.append(1)

            if x >= -153 and x <= -53:
                Aux = MainMatrix.getColumnState(5)
                if Aux is not False:
                    yPosition = -(Aux * 100) + K
                    xPosition = -50
                    MainMatrix.addValue(Aux, 4, playerActing)
                    clickChecker = True
                    if playerActing == 1:
                        myPlayers.append(2)
                    else:
                        myPlayers.append(1)

            if x >= -53 and x <= 46:
                Aux = MainMatrix.getColumnState(6)
                if Aux is not False:
                    yPosition = -(Aux * 100) + K
                    xPosition = 50
                    MainMatrix.addValue(Aux, 5, playerActing)
                    clickChecker = True
                    if playerActing == 1:
                        myPlayers.append(2)
                    else:
                        myPlayers.append(1)

            if clickChecker is True: # Now, drawing the token.
                # Deciding the token color.
                if playerActing == 1:
                    TokenColor = "red"
                if playerActing == 2:
                    TokenColor = "blue"
                MainBoard.drawToken(xPosition, yPosition, TokenColor) # Drawing it.
                # If there's a victory, the winner tokens change their colour.
                if MainMatrix.checkVictory(playerActing)[0] is True:
                    MainBoard.WinnerText(playerActing)

                    if MainMatrix.checkVictory(1)[0] is True and MainMatrix.isEmpty() is False:
                        wPositions = MainMatrix.checkVictory(1)[1]
                        turtle.onscreenclick(None)
                        MainBoard.WinnerToken(1, wPositions)
                        turtle.onscreenclick(getScreenClick)

                    elif MainMatrix.checkVictory(2)[0] is True and MainMatrix.isEmpty() is False:
                        wPositions = MainMatrix.checkVictory(2)[1]
                        turtle.onscreenclick(None)
                        MainBoard.WinnerToken(2, wPositions)
                        turtle.onscreenclick(getScreenClick)

                return True # I don't know why the fuck I'm using that.

        turtle.onscreenclick(getScreenClick) # Getting the next click.
        turtle.mainloop() # Main game loop.
