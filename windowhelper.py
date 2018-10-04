def center(pixels, window):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    x = (screenWidth / 2) - (pixels / 2)
    y = (screenHeight / 2) - (pixels / 2)
    return x, y
