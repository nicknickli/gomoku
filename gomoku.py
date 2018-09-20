"""@author: Nicholas Li
Gomoku (5 in a Row) implemented with Python"""

#Main function to run Gomoku
from Tkinter import *
from menu import mainMenu
#creates window gui for user
menuWindow = Tk()
menuWindow.title("Gomoku")
menuWindow.geometry("500x500")
mainMenu(menuWindow)
menuWindow.mainloop()
