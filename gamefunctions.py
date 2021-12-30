import sys
import pygame
from time import sleep

def check_events(screen, board):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row, col = getGridPosition(screen, board)
            board.pickSpot(row, col)

def check_keydown_events(event):
    """Respond to keypresses"""
    if event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        print("hi")

def getGridPosition(screen, board):
    """Returns the grid position of the cursor"""
    x, y = pygame.mouse.get_pos()
    width = screen.get_width()
    spacing = int(width / board.size)
    row = int(y / spacing)
    col = int(x / spacing)
    return row, col

def update_screen(settings, screen, stats, board):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen
    screen.fill(settings.bgColor)

    # Draw the game board
    board.draw(screen, settings, stats)

    # # draw the score information
    # sb.show_score()
    
    # # Draw the play button if the game is inactive
    # if not stats.game_active:
    #     play_button.draw_button()
    
    # Make the most recently drawn screen visible
    pygame.display.flip()