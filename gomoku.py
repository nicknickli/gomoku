"""@author: Nicholas Li
Gomoku (5 in a Row) implemented with Python"""

#Main function to run Gomoku
from Tkinter import *
from menu import mainMenu
from gamegraphics import Board
from aiwindow import AISimulation

quit = False

"""gameMode 0 means nothing is selected
gameMode 1 means singleplayer
gameMode 2 means two players
gameMode 3 means AI simulation"""
gameMode = 0

while quit != True:
    #creates window gui for user\
    menu = mainMenu()
    gameMode = menu.getmode()
    boardSize = menu.getsize()
    while gameMode == 1:
        board = Board(boardSize)
        gameMode = board.getquit()
    while gameMode == 2:
        board = Board(boardSize)
        gameMode = board.getquit()
    while gameMode == 3:
        AIinfo = AISimulation()

        gameMode = 0
    quit = menu.getquit()
