class Settings():
    """A class to store all settings for Tic Tac Toe"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screenWidth = 800
        self.screenHeight = 800
        self.bgColor = (230, 230, 230)
        self.lineColor = (0, 0, 0)
        self.xColor = (0, 0, 255)
        self.oColor = (255, 0, 0)
        self.winLineColor = (0, 255, 0)