class GameStats():
    """Track statistics for Tic Tac Toe"""

    def __init__(self):
        """Initialize statistics"""
        # Reset the game scores
        self.resetStats()

        # Start Tic Tac Toe in an inactive state
        self.gameActive = True

    def resetStats(self):
        """Initialize statistic that can change during the game"""
        self.xScore = 0
        self.oScore = 0