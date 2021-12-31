import pygame
from settings import Settings
from board import Board
from game_stats import GameStats
import gamefunctions as gf
from button import Button
from scoreboard import Scoreboard
 
def runGame():

    # Initialize pygame, settings, and screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
    width = screen.get_width()
    pygame.display.set_caption("Tic Tac Toe")

    # Create game board
    stats = GameStats()
    sb = Scoreboard(settings, screen, stats)
    board = Board(width, 3)

    # Create the 'Play' button
    playButton = Button(screen, settings, "Play Again?")

    # Start the main loop for the game
    while True:
        gf.checkEvents(settings, screen, stats, sb, board, playButton)
        gf.updateScreen(settings, screen, stats, sb, board, playButton)

runGame()