import turtle


class Matrix:

    def __init__(self, numberColumns, numberRows):
        # Using this class to save the board data, and search for a victory.
        self.gameMatrix = []
        self.numberColumns = numberColumns
        self.numberRows = numberRows

        for i in range(numberRows):
            self.gameMatrix.append([None] * numberColumns)  # Creating game matrix.

    def Restart(self, numberColumns, numberRows): # Basicaly creating the Game Matrix again.
        self.gameMatrix = []
        self.numberColumns = numberColumns
        self.numberRows = numberRows

        for i in range(numberRows):
            self.gameMatrix.append([None] * numberColumns)  # Restarting game matrix.

    def addValue(self, xPosition, yPosition, addingValue):  # Adding a value to the matrix.
        self.gameMatrix[xPosition][yPosition] = addingValue
        return addingValue

    def checkVictory(self, checkedItem):  # Checking victory.
        # Checking Vertical
        for i in range(self.numberColumns):
            for j in range(self.numberRows - 3):
                if self.gameMatrix[j][i] == self.gameMatrix[j + 1][i] == self.gameMatrix[j + 2][i] == self.gameMatrix[j + 3][i] == checkedItem:
                    wPositions = [[j, i], [j + 1, i], [j + 2, i], [j + 3, i]]
                    return True, wPositions

        # Checking Horizontal.
        for i in range(self.numberRows):
            for j in range(self.numberColumns - 3):
                if self.gameMatrix[i][j] == self.gameMatrix[i][j + 1] == self.gameMatrix[i][j + 2] == self.gameMatrix[i][j + 3] == checkedItem:
                    wPositions = [[i, j], [i, j + 1], [i, j + 2], [i, j + 3]]
                    return True, wPositions

        # Checking Diagonal.
        for i in range(self.numberRows):  # Right.
            for j in range(self.numberColumns):
                try:
                    if self.gameMatrix[j][i] == self.gameMatrix[j - 1][i + 1] == self.gameMatrix[j - 2][i + 2] == self.gameMatrix[j - 3][i + 3] == checkedItem:
                        wPositions = [[j, i], [j - 1, i + 1], [j - 2, i + 2], [j - 3, i + 3]]
                        return True, wPositions
                except:
                    pass

        for i in range(self.numberRows):  # Left.
            for j in range(self.numberColumns):
                try:
                    if self.gameMatrix[i][j] == self.gameMatrix[i + 1][j + 1] == self.gameMatrix[i + 2][j + 2] == self.gameMatrix[i + 3][j + 3] == checkedItem:
                        wPositions = [[i, j], [i + 1, j + 1], [i + 2, j + 2], [i + 3, j + 3]]
                        return True, wPositions
                except:
                    pass

        return False, None

    def columnIsFull(self, nColumn): # Knowing if a Matrix Column is full or not.
        nColumn -= 1 # Counting column 0.
        for mRows in range(self.numberRows):
            if self.gameMatrix[mRows][nColumn] is None:
                return False
        return True


    def getColumnState(self, checkColumn): # Getting if a column is empty or not, if not, then we get the highest position.
        for mRows in range(-(self.numberRows-1), 1):
            if self.gameMatrix[-mRows][checkColumn-1] is None:
                return -mRows

        return False

    def fullMatrix(self): # Getting True if the Matrix is full, so there's a draw.
        for i in self.gameMatrix:
            for j in i:
                if j is None:
                    return False
        return True

    def isEmpty(self): # Getting if the Matrix is empty, not sure if I'm using that. lol
        for i in self.gameMatrix:
            for j in i:
                if j is not None:
                    return False
        return True

    def saveGame(self, dataPath, linkedList): # For a GameMatrix, we create a text file, saving all the data.
        aux = []
        for i in self.gameMatrix: # Going through the matrix and adding it to the Data file.
            for j in i:
                aux.append(j)
                aux.append(".") # Splitting the positions with a '.'.
            aux[-1] = "" # Deleting last point, to know that I'm on a new row.
            aux.append("&")
        aux[-1] = ""
        gameData = ""
        for i in aux:
            gameData += str(i) # Creating data string.

        # Creating a file and adding data inside it.
        dataFile = open(dataPath, "w")
        dataFile.write(str(self.numberColumns) + str("_") + str(self.numberRows)) # Splitting the number of columns/rows with a "_".
        dataFile.write("=") # Splitting the type of data with "=".
        dataFile.write(gameData)
        dataFile.write("=")
        dataFile.write(str(linkedList.last.data)) # Last move information.
        dataFile.close()

        return gameData

    def clearGame(self): # Restarting the matrix.
        for i in range(self.numberRows):
            self.gameMatrix.append([None] * self.numberColumns)

    def convertToGame(self): # If we have a Matrix, we convert the matrix to a visual game.
        # Using K1 and K2 to create the position where I draw on screen.
        K1 = -500
        K2 = 200
        Matrix = self.gameMatrix
        # Going through the matrix, and drawing every position.
        for Mx in range(self.numberColumns):
            for My in range(self.numberRows):
                mValue = Matrix[Mx][My]
                if mValue is not None: # If the value is None, it means that there's an empty position.
                    xPosition = K1 + My * 100 # Creating screen position where I draw the token.
                    yPosition = K2 + Mx * (-100) # Creating screen position where I draw the token.
                    # Depending on the value, it's a red or blue token.
                    if mValue == 1:
                        tokenColor = "red"
                    if mValue == 2:
                        tokenColor = "blue"
                    # Then the pointer goes to the position, and creates the token.
                    turtle.hideturtle()
                    turtle.speed(100)
                    turtle.pensize(10)
                    turtle.color("black", tokenColor)
                    turtle.penup()
                    turtle.goto(xPosition, yPosition)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(50)
                    turtle.end_fill()

    def __str__(self): # Just used for some tests, that returns the Game Matrix as a String.
        # To use it, just use print(Matrix).
        matrixString = ""
        for i in self.gameMatrix:
            matrixString += str(i)
            matrixString += str("\n")

        return matrixString