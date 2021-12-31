import pygame.font

class Scoreboard():
    """A class to report scoring information"""

    def __init__(self, settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screenRect = screen.get_rect()
        self.settings = settings
        self.stats = stats
        self.statusMsgColor = self.settings.xColor

        # Font settings for scoring information
        self.font = pygame.font.SysFont(None, 32)

        # Prepare the initial score images
        self.prepScore("X's Turn")

    def prepScore(self, statusMsg):
        """Turn the score into a rendered image"""
        self.font = pygame.font.SysFont(None, 32)

        # Prep the X score
        xScore = self.stats.xScore
        xScoreStr = "X Wins: " + str(xScore)
        self.xScoreImage = self.font.render(xScoreStr, True, self.settings.xColor, self.settings.bgColor)

        # Display the score at the top left of the screen
        self.xScoreRect = self.xScoreImage.get_rect()
        self.xScoreRect.left = self.screenRect.left + 10
        self.xScoreRect.top = 10

        # Prep the O score
        oScore = self.stats.oScore
        oScoreStr = "O Wins: " + str(oScore)
        self.oScoreImage = self.font.render(oScoreStr, True, self.settings.oColor, self.settings.bgColor)

        # Display the score at the top right of the screen
        self.oScoreRect = self.oScoreImage.get_rect()
        self.oScoreRect.right = self.screenRect.right - 10
        self.oScoreRect.top = 10

        # Display the message at the top center of the screen
        self.font = pygame.font.SysFont(None, 48)
        statusMsgStr = statusMsg
        statusMsgColor = self.statusMsgColor
        self.statusMsgImage = self.font.render(statusMsgStr, True, statusMsgColor, self.settings.bgColor)
        self.statusMsgRect = self.statusMsgImage.get_rect()
        self.statusMsgRect.center = self.screenRect.center
        self.statusMsgRect.top = 10

    def showScore(self):
        """Draw scores to the screen"""
        self.screen.blit(self.xScoreImage, self.xScoreRect)
        self.screen.blit(self.oScoreImage, self.oScoreRect)
        self.screen.blit(self.statusMsgImage, self.statusMsgRect)