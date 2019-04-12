import turtle

Scr = turtle.Screen()
Pointer = turtle.Turtle()
Scr.setup(1200, 800)


class Board:

    def __init__(self, nColumns, nRows): # Creating the game board.
        print("Loading...")
        Scr.bgcolor("azure4")
        Pointer.pencolor("black")
        Pointer.hideturtle()

        Pointer.speed(100)
        Pointer.pensize(10)
        Pointer.penup()
        Pointer.goto(150, 250)
        Pointer.write("Connect 4", font=("Weather Sunday - Personal Use", 60))
        print("*", end="")
        Rx = -600
        for j in range(nColumns): # Drawing game board.
            print("*", end="")
            Ry = 300
            Rx += 100
            for i in range(nRows):
                Ry -= 100
                Pointer.penup()
                Pointer.goto(Rx, Ry)
                Pointer.pendown()
                Pointer.circle(50)

        Pointer.penup()

        Pointer.goto(-590, -390)
        Pointer.write("Sklyvan", font=("Burbank Big Condensed", 15))
        print("*", end="")

        # Save Data Button.
        Pointer.penup()
        Pointer.goto(320, -275)
        Pointer.pendown()
        Pointer.color("black", "MistyRose2")
        Pointer.begin_fill()
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.left(-90)
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.end_fill()
        Pointer.penup()
        Pointer.goto(350, -355)
        Pointer.write("Save Data", font=("Burbank Big Condensed", 40))
        Pointer.left(-90)
        print("*", end="")

        # Load Data Button.
        Pointer.penup()
        Pointer.goto(320, -150)
        Pointer.pendown()
        Pointer.color("black", "MistyRose2")
        Pointer.begin_fill()
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.left(-90)
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.end_fill()
        Pointer.penup()
        Pointer.goto(350, -230)
        Pointer.write("Load Data", font=("Burbank Big Condensed", 40))
        print("*", end="")

        Pointer.left(-90)

        # IA Mode Button.
        Pointer.penup()
        Pointer.goto(320, -25)
        Pointer.pendown()
        Pointer.color("black", "darkcyan")
        Pointer.begin_fill()
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.left(-90)
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.penup()
        Pointer.goto(370, -105)
        Pointer.write("IA Mode", font=("Burbank Big Condensed", 40))
        Pointer.end_fill()
        print("*", end="")

        Pointer.left(-90)

        # Reset Game Button.
        Pointer.penup()
        Pointer.goto(320, 100)
        Pointer.pendown()
        Pointer.color("black", "darkkhaki")
        Pointer.begin_fill()
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.left(-90)
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.penup()
        Pointer.goto(332.5, 20)
        Pointer.write("Restart Game", font=("Burbank Big Condensed", 35))
        Pointer.end_fill()
        print("*", end="")

        Pointer.goto(370, -105)
        print("\n")
        print("Game Ready!")

    def drawToken(self, x, y, tokenColor):
        Pointer.color("black", tokenColor)
        Pointer.penup()
        Pointer.goto(x, y)
        Pointer.pendown()
        Pointer.begin_fill()
        Pointer.circle(50)
        Pointer.end_fill()

    def WinnerText(self, playerIdent):
        Pointer.speed(100)
        Pointer.pensize(10)
        Pointer.penup()
        Pointer.goto(-435, 320)
        Pointer.pendown()

        if playerIdent == 1:
            Pointer.color("black")
            Pointer.write("Player 1 Winner!", font=("Futura", 35))

        if playerIdent == 2:
            Pointer.color("black")
            Pointer.write("Player 2 Winner!", font=("Futura", 35))

        if playerIdent == 3:
            Pointer.color("black")
            Pointer.penup()
            Pointer.goto(-330, 320)
            Pointer.pendown()
            Pointer.write("DRAW!", font=("Futura", 35))

    def WinnerToken(self, playerWinner, wPositions):
        Pointer.speed(1)
        if playerWinner == 1:
            colour = "red"
        elif playerWinner == 2:
            colour = "blue"

        K1 = -500
        K2 = 200
        try:
            for i in range(4):
                for j in range(1):
                    x = wPositions[i][j]
                    y = wPositions[i][j + 1]
                    xPosition = K1 + y * 100
                    yPosition = K2 + x * (-100)

                    turtle.hideturtle()
                    turtle.speed(50)
                    turtle.pensize(10)
                    turtle.color("black", "darkgoldenrod")
                    turtle.penup()
                    turtle.goto(xPosition, yPosition)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(50)
                    turtle.end_fill()
            for i in range(4):
                for j in range(1):
                    x = wPositions[i][j]
                    y = wPositions[i][j + 1]
                    xPosition = K1 + y * 100
                    yPosition = K2 + x * (-100)

                    turtle.hideturtle()
                    turtle.speed(50)
                    turtle.pensize(10)
                    turtle.color("black", colour)
                    turtle.penup()
                    turtle.goto(xPosition, yPosition)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(50)
                    turtle.end_fill()
            for i in range(4):
                for j in range(1):
                    x = wPositions[i][j]
                    y = wPositions[i][j + 1]
                    xPosition = K1 + y * 100
                    yPosition = K2 + x * (-100)

                    turtle.hideturtle()
                    turtle.speed(25)
                    turtle.pensize(10)
                    turtle.color("black", "darkgoldenrod")
                    turtle.penup()
                    turtle.goto(xPosition, yPosition)
                    turtle.pendown()
                    turtle.begin_fill()
                    turtle.circle(50)
                    turtle.end_fill()
        except:
            pass

    def Restart(self, nColumns, nRows, RestartMode):
        Scr.clear()
        Pointer.left(-90)
        print("Restarting...")
        Scr.bgcolor("azure4")
        Pointer.pencolor("black")
        Pointer.hideturtle()

        Pointer.speed(100)
        Pointer.pensize(10)
        Pointer.penup()
        Pointer.goto(150, 250)
        Pointer.circle(50)

        Pointer.write("Connect 4", font=("Weather Sunday - Personal Use", 60))
        print("*", end="")
        Rx = -600
        for j in range(nColumns): # Drawing game board.
            print("*", end="")
            Ry = 300
            Rx += 100
            for i in range(nRows):
                Ry -= 100
                Pointer.penup()
                Pointer.goto(Rx, Ry)
                Pointer.pendown()
                Pointer.circle(50)

        Pointer.penup()

        Pointer.goto(-590, -390)
        Pointer.write("Sklyvan", font=("Burbank Big Condensed", 15))
        print("*", end="")

        # Save Data Button.
        Pointer.penup()
        Pointer.goto(320, -275)
        Pointer.pendown()
        Pointer.color("black", "MistyRose2")
        Pointer.begin_fill()
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.left(-90)
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.end_fill()
        Pointer.penup()
        Pointer.goto(350, -355)
        Pointer.write("Save Data", font=("Burbank Big Condensed", 40))
        Pointer.left(-90)
        print("*", end="")

        # Load Data Button.
        Pointer.penup()
        Pointer.goto(320, -150)
        Pointer.pendown()
        Pointer.color("black", "MistyRose2")
        Pointer.begin_fill()
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.left(-90)
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.end_fill()
        Pointer.penup()
        Pointer.goto(350, -230)
        Pointer.write("Load Data", font=("Burbank Big Condensed", 40))
        print("*", end="")

        Pointer.left(-90)

        # IA Mode Button.
        Pointer.penup()
        Pointer.goto(320, -25)
        Pointer.pendown()
        Pointer.color("black", "darkcyan")
        Pointer.begin_fill()
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.left(-90)
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.penup()
        Pointer.goto(370, -105)
        if RestartMode == 1:
            Pointer.write("IA Mode", font=("Burbank Big Condensed", 40))
        if RestartMode == 2:
            Pointer.write("2P Mode", font=("Burbank Big Condensed", 40))
        Pointer.end_fill()

        Pointer.left(-90)

        # Reset Game Button.
        Pointer.penup()
        Pointer.goto(320, 100)
        Pointer.pendown()
        Pointer.color("black", "darkkhaki")
        Pointer.begin_fill()
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.left(-90)
        Pointer.forward(250)
        Pointer.left(-90)
        Pointer.forward(100)
        Pointer.penup()
        Pointer.goto(332.5, 20)
        Pointer.write("Restart Game", font=("Burbank Big Condensed", 35))
        Pointer.end_fill()
        print("*", end="")

        Pointer.goto(370, -105)
        print("\n")
        print("Ready!")