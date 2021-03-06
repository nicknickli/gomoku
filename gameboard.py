#handles the board state and initializes the board
from Tkinter import *
import numpy as np
from gamegraphics import Board

#initializes the board with user board size
#0 represents empty space, 1 represents black, 2 represents white
def startGame(playerNum, boardSize, menuWindow):
    menuWindow.destroy()

    if playerNum == 1:
        Board(boardSize)
    elif playerNum == 2:
        Board(boardSize)
    else:
        raise Exception("Player number is invalid")
