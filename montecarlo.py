import random
import time
import copy
from settings import Settings
from board import Board
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def monteCarlo(board, numSimulations, screen):
    """Returns the next best move based on a Monte Carlo simulation.
    It is assumed that the player whose turn is active is the player whose
    move shall be determined (i.e. return the best move for the currently 
    active player)."""

    # Create a dictionary to rank the potential moves
    currentTurn = board.currentTurn
    rankedSpaces = {}
    for space in board.availableSpaces:
        rankedSpaces[tuple(space)] = 0

    for i in range(numSimulations):
        # Create a fresh copy of the current board
        tempBoard = copy.deepcopy(board)

        # Don't like how this is implemented, needs refactoring
        # For now, create copies to preserve the originals
        tempSettings = Settings()
        tempStats = GameStats()
        tempSb = Scoreboard(tempSettings, screen, tempStats)

        # Make a move at random (bookmark first move)
        [fistMoveRow, fistMoveCol] = tempBoard.getRandomMove()
        tempBoard.pickSpot(tempSettings, tempStats, tempSb, fistMoveRow, fistMoveCol)

        # Proceed to make moves at random until game is over
        while not tempBoard.gameOver:
            [row, col] = tempBoard.getRandomMove()
            tempBoard.pickSpot(tempSettings, tempStats, tempSb, row, col)

        # Rank the first move based on outcome
        # tie += 0, win += 1, loss -= 1
        if tempBoard.winner == currentTurn:
            rankedSpaces[(fistMoveRow, fistMoveCol)] += 1
        elif tempBoard.winner == None:
            rankedSpaces[(fistMoveRow, fistMoveCol)] += 0
        else:
            rankedSpaces[(fistMoveRow, fistMoveCol)] -= 5

    # Determine which initial move is best
    highestRank = -numSimulations * 100
    for val in rankedSpaces:
        if rankedSpaces[val] > highestRank:
            bestMove = val
            highestRank = rankedSpaces[val]

    # For now, randomly make a move
    return bestMove