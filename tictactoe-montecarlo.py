import pygame
import gamefunctions as gf
from montecarlo import monteCarlo
from settings import Settings
from board import Board
from game_stats import GameStats
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
    x = screen.get_rect().centerx
    y = screen.get_rect().centery - 40
    playButton = Button(screen, settings, "Play Again?", [x, y])

    # Create the 'Reset' button
    x = screen.get_rect().centerx
    y = screen.get_rect().centery + 40
    resetButton = Button(screen, settings, "Reset Scores?", [x, y])

    # Start the main loop for the game
    while True:
        gf.checkEvents(settings, screen, stats, sb, board, playButton, resetButton)
        gf.updateScreen(settings, screen, stats, sb, board, playButton, resetButton)

        # For now, have the computer (O player) randomly make a move
        if stats.gameActive and board.currentTurn == "O":
            [row, col] = monteCarlo(board, 10)
            board.pickSpot(settings, stats, sb, row, col)

runGame()