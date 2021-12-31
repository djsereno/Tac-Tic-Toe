import sys
import pygame
from time import sleep

def checkEvents(settings, screen, stats, sb, board, playButton):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeydownEvents(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # If game is not over, pick the spot that the user has chosen
            if not board.gameOver:
                row, col = getGridPosition(screen, board)
                board.pickSpot(settings, stats, sb, row, col)
            else:
                mouseX, mouseY = pygame.mouse.get_pos()
                checkPlayButton(settings, stats, sb, playButton, board, mouseX, mouseY)

def checkKeydownEvents(event):
    """Respond to keypresses"""
    if event.key == pygame.K_q:
        sys.exit()

def getGridPosition(screen, board):
    """Returns the grid position of the cursor"""
    x, y = pygame.mouse.get_pos()
    width = screen.get_width()
    spacing = int(width / board.size)
    row = int(y / spacing)
    col = int(x / spacing)
    return row, col

def checkPlayButton(settings, stats, sb, playButton, board, mouseX, mouseY):
    """Start a new game when the player clicks Play"""
    buttonClicked = playButton.rect.collidepoint(mouseX, mouseY)
    if buttonClicked and not stats.gameActive:
        # Reset the game statistics
        stats.gameActive = True

        # Reset the game board and scoreboard status message
        board.reset()
        sb.statusMsgColor = settings.xColor
        sb.prepScore("X's Turn")

def updateScreen(settings, screen, stats, sb, board, playButton):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen
    screen.fill(settings.bgColor)

    # Draw the game board
    board.draw(screen, settings, stats)

    # draw the score information
    sb.showScore()
    
    # Draw the play button if the game is inactive
    if not stats.gameActive:
        playButton.drawButton()
    
    # Make the most recently drawn screen visible
    pygame.display.flip()