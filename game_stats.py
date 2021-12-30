class GameStats():
    """Track statistics for Tic Tac Toe"""

    def __init__(self):
        """Initialize statistics"""
        # self.ai_settings = ai_settings
        # self.reset_stats()
        # # High score should never be reset
        # self.high_score = 0

        # Start Tic Tac Toe in an inactive state
        self.gameActive = True

    def reset_stats(self):
        """Initialize statistic that can change during the game"""
        # self.ships_left = self.ai_settings.ship_limit
        # self.score = 0