#handles option twoplayers
from boardsize import boardSizeMenu
def twoPlayers(menu, oldFrame):
    menuFrame.pack_forget()
    boardSizeMenu(menu, oldFrame)
    menu.destroy()
