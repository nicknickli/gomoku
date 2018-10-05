def center(pixelsX, pixelsY, window):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    x = (screenWidth / 2) - (pixelsX / 2)
    y = (screenHeight / 2) - (pixelsY / 2)
    return x, y
