"""@author: Nicholas Li
Gomoku (5 in a Row) implemented with Python"""

#Main function to run Gomoku
from Tkinter import *
from menu import mainMenu
menuWindow = Tk()
menuWindow.title("Gomoku")
menuWindow.geometry("500x500")
mainMenu(menuWindow)
menuWindow.mainloop()

def startGame(playerNum, boardSize):
    if playerNum == 1:
        singlePlayer()
    elif playerNum == 2:
        twoPlayers()
    else:
        raise Exception("Wrong number of players inputted. Value {} was inputted instead".format(playerNum))
