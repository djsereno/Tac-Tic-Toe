import pygame.font

class Button():
    
    def __init__(self, screen, settings, msg, location):
        """Initialize button attributes"""
        self.screen = screen
        self.screenRect = screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.buttonColor = settings.buttonBgColor
        self.textColor = settings.buttonTextColor
        self.textHoverColor = settings.buttonHoverTextColor
        self.font = pygame.font.SysFont(None, 48)
        self.location = location
        self.hover = False
        self.msg = msg

        # The button message need to be prepped only once
        self.prepMsg()

        # Build the button's rect object and center it
        self.width = self.msgImageRect.width + 20
        self.height = self.msgImageRect.height + 20
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.location

    def prepMsg(self):
        """Turn msg into a rendered image and center text on the button"""
        # Change text color if hovering or not
        if self.hover:
            color = self.textHoverColor
        else:
            color = self.textColor
        self.msgImage = self.font.render(self.msg, True, color, self.buttonColor)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.center = self.location

    def drawButton(self):
        # Draw blank button and then draw the message
        self.screen.fill(self.buttonColor, self.rect)
        self.screen.blit(self.msgImage, self.msgImageRect)
