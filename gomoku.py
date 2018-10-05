"""@author: Nicholas Li
Gomoku (5 in a Row) implemented with Python"""

#Main function to run Gomoku
from Tkinter import *
from menu import mainMenu

quit = False

while quit != True:
    #creates window gui for user
    menu = mainMenu()
    quit = menu.getquit()
