import random


class RandomIA:

    def __init__(self, nRows, nColumns, GameMatrix):

        if GameMatrix.isEmpty is True:
            print("Ficha en el Centro.")