class Settings():
    """A class to store all settings for Tic Tac Toe"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screenWidth = 800
        self.screenHeight = 800
        
        # Board settings
        self.bgColor = (230, 230, 230) # light grey
        self.lineColor = (0, 0, 0) # black
        self.winLineColor = (0, 255, 0) # green

        # Player settings
        self.xColor = (0, 0, 255) # blue
        self.oColor = (255, 0, 0) # red

        # Button settings
        self.buttonBgColor = (50, 50, 50) # dark grey
        self.buttonTextColor = (255, 255, 255) # white
        self.buttonHoverTextColor = (255, 255, 0) # yellow