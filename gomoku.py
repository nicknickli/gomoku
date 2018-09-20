"""@author: Nicholas Li
Gomoku (5 in a Row) implemented with Python"""

#Main function to run Gomoku
from menu import mainMenu
from Tkinter import *
menuWindow = Tk()
menuWindow.title("Gomoku")
menuWindow.geometry("500x500")
mainMenu(menuWindow)
menuWindow.mainloop()
