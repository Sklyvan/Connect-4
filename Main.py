from Game import MainGame

if __name__ == "__main__":
    myGame = MainGame(6, 6)
else:
    print("Something went wrong...")

# After winning a game, if I restart the game, there's a bug which causes that there's a missing part on the board.
# IA Mode is not implemented.