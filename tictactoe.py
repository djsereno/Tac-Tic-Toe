import pygame
from settings import Settings
from board import Board
from game_stats import GameStats
import gamefunctions as gf
 
def run_game():

    # Initialize pygame, settings, and screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    width = screen.get_width()
    pygame.display.set_caption("Tic Tac Toe")

    # Create game board
    stats = GameStats()
    board = Board(width, 3)

    # Start the main loop for the game
    while True:
        gf.check_events(screen, board)

        if stats.gameActive:
            gf.update_screen(settings, screen, stats, board)

run_game()