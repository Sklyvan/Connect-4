from Matrix import Matrix
import random


class GameTools:

    def readData(self, dataPatch):
        """ Used to read a .dat file, and then return a Game Matrix and the last value of the Linked List, which is the last player to play.
        That's used to load a saved data, 'Load Data' button. """
        aux = False
        dataFile = open(dataPatch, "r")
        for textString in dataFile:
            fileData = textString.split("=") # Since the .dat file is splitted into 3 parts, (Matrix Size, Matrix Values, Last Player), I split these 3 values and put them into a list (fileData).

        matrixInfo = fileData[0].split("_") # Array matrixInfo contains Matrix Size.
        matrixData = fileData[1].split("&") # An array with all the matrix rows, splitted by a '.'
        lastPlayer = fileData[2] # String, contains last player.

        matrixNumbers = []
        for aux in matrixData: # Creating an array containing all matrix values. (Not a Matrix!)
            auxList = aux.split(".")
            matrixNumbers.append(auxList)

        matrixColumns = int(matrixInfo[0])
        matrixRows = int(matrixInfo[1])

        restoredMatrix = []
        for i in range(matrixRows): # Creating the Game Matrix (Without the values, everything is None.)
            restoredMatrix.append([None] * matrixColumns)

        for i in range(matrixColumns): # Adding the values to the matrix.
            for j in range(matrixRows):
                tempValue = matrixNumbers[i][j]
                if tempValue is "None":
                    restoredMatrix[i][j] = None
                else:
                    if tempValue == "1":
                        restoredMatrix[i][j] = 1
                    if tempValue == "2":
                        restoredMatrix[i][j] = 2

        return restoredMatrix, lastPlayer # Returning Matrix and Last Player.

    def randomStarter(self): # Just returning a random 1 or 2, used to get the game starter.
        rPlayer = random.randint(1, 2)
        return rPlayer

    def createGameID(self):
        """
        Esta función depende del servidor, que es el que tiene las partidas guardadas y las ID's usadas.
        Un script en PHP nos devolverá la última ID creada, lastID.
        :return: La GameID que se ha generado para identificar este juego.
        """
        raise NotImplementedError("Online Mode is not avaliable.")