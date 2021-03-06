import pygame
import random

class Board():
    """A class to for the Tic Tac Toe board"""

    def __init__(self, width, size):
        """Initialize the game's static settings"""
        self.size = size
        self.grid = [[0 for i in range(size)] for j in range(size)]
        self.currentTurn = "X"
        self.width = width
        self.gridSpacing = int(width / 3)
        self.winLine = None
        self.gameOver = False
        self.availableSpaces = self.getAvailableSpaces()

    def print(self):
        """Prints a text version of the board"""
        print("\n")
        for r in range(self.size):
            print(self.grid[r])

    def changeTurn(self, settings, sb):
        """Changes the current turn to the next player"""
        if self.currentTurn == "X":
            self.currentTurn = "O"
            sb.statusMsgColor = settings.oColor
        else:
            self.currentTurn = "X"
            sb.statusMsgColor = settings.xColor

    def getAvailableSpaces(self):
        """Returns a list of available spaces"""
        spaces = []
        size = self.size
        grid = self.grid
        for row in range(size):
            for col in range(size):
                if grid[row][col] == 0:
                    spaces.append([row, col])
        return spaces

    def getRandomMove(self):
        """Returns a random available move"""
        availableSpaces = self.availableSpaces
        return availableSpaces[random.randint(0, len(availableSpaces) - 1)]

    def draw(self, screen, settings, stats):
        """Draws the gameboard to the canvas"""
        
        # Draw the game board
        width = self.width
        spacing = self.gridSpacing
        pygame.draw.line(screen, settings.lineColor, [spacing, 0], [spacing, width], 8)
        pygame.draw.line(screen, settings.lineColor, [0, spacing], [width, spacing], 8)
        pygame.draw.line(screen, settings.lineColor, [2*spacing, 0], [2*spacing, width], 8)
        pygame.draw.line(screen, settings.lineColor, [0, 2*spacing], [width, 2*spacing], 8)

        # Draw the player spaces
        font = pygame.font.Font(None, 266)
        for row in range(self.size):
            for col in range(self.size):
                player = self.grid[row][col]
                if player != 0:
                    x = int((col + 0.5) * spacing)
                    y = int((row + 0.5) * spacing)

                    if player == "X":
                        text = font.render(player, True, settings.xColor)
                    else:
                        text = font.render(player, True, settings.oColor)
                    textRect = text.get_rect()
                    textRect.center = (x, y)
                    screen.blit(text, textRect)

        # Draw the win line if the game is over
        if self.gameOver:
            stats.gameActive = False
            if self.winLine:
                pygame.draw.line(screen, settings.winLineColor, self.winLine[0], self.winLine[1], 20)
            
    def pickSpot(self, settings, stats, sb, row, col):
        """Takes a spot if available and changes turn"""
        # Only take the spot if it is available
        if self.grid[row][col] == 0:
            self.grid[row][col] = self.currentTurn
            self.availableSpaces.remove([row, col])
            
            # Check if the last move has ended the game. Change turn if not.
            gameOver = self.checkGameOver()
            if gameOver == 0:
                # Game is still active. Change turn and update scoreboard status message.
                self.changeTurn(settings, sb)
                statusMsg = self.currentTurn + "'s Turn"
                sb.prepScore(statusMsg)
            else:
                # Game is over. Update scores and scoreboard.
                self.gameOver = True 
                if gameOver == 1 and self.currentTurn == "X":
                    stats.xScore += 1
                    sb.prepScore("X Wins!")
                elif gameOver == 1 and self.currentTurn == "O":
                    stats.oScore += 1
                    sb.prepScore("O Wins!")
                else:
                    sb.statusMsgColor = settings.lineColor
                    sb.prepScore("Tie Game!")

    def reset(self):
        """Resets the game board"""
        size = self.size
        self.grid = [[0 for i in range(size)] for j in range(size)]
        self.availableSpaces = self.getAvailableSpaces()
        self.currentTurn = "X"
        self.winLine = None
        self.gameOver = False
    
    def checkGameOver(self):
        """Checks if the game is over and returns True if so"""
        # Returns 1 if game is a win 
        # Returns 0 if game is still active
        # Returns -1 if game is a tie

        size = self.size
        
        # Check for a horizontal win
        for row in range(size):
            for col in range(size - 1):
                if self.grid[row][col] != self.grid[row][col + 1] or self.grid[row][col] == 0:
                    break
                elif col == size - 2:
                    spacing = self.gridSpacing
                    size = self.size
                    x1 = int(0.25 * spacing)
                    y1 = int(spacing * (row + 0.5))
                    x2 = int(spacing * (size - 0.25))
                    y2 = y1
                    self.winLine = [[x1, y1], [x2, y2]]
                    return 1

        # Check for a vertical win
        for col in range(size):
            for row in range(size - 1):
                if self.grid[row][col] != self.grid[row + 1][col] or self.grid[row][col] == 0:
                    break
                elif row == size - 2:
                    spacing = self.gridSpacing
                    size = self.size
                    x1 = int(spacing * (col + 0.5))
                    y1 = int(0.25 * spacing)
                    x2 = x1
                    y2 = int(spacing * (size - 0.25))
                    self.winLine = [[x1, y1], [x2, y2]]
                    return 1

        # Check for a diagonal down win
        for i in range(size - 1):
            if self.grid[i][i] != self.grid[i + 1][i + 1] or self.grid[i][i] == 0:
                break
            elif i == size - 2:
                spacing = self.gridSpacing
                size = self.size
                x1 = int(0.25 * spacing)
                y1 = x1
                x2 = int(spacing * (size - 0.25))
                y2 = x2
                self.winLine = [[x1, y1], [x2, y2]]
                return 1

        # Check for a diagonal up win
        for i in range(size - 1):
            if self.grid[size - 1 - i][i] != self.grid[size - 2 - i][i + 1] or self.grid[size - 1 - i][i] == 0:
                break
            elif i == 1:
                spacing = self.gridSpacing
                size = self.size
                x1 = int(0.25 * spacing)
                x2 = int(spacing * (size - 0.25))
                y1 = x2
                y2 = x1
                self.winLine = [[x1, y1], [x2, y2]]
                return 1

        # Check for a tie
        for col in range(size):
            for row in range(size):
                # Empty spaces remain, game still active
                if self.grid[row][col] == 0:
                    return 0
                # Tie game
                elif row == size - 1 and col == size - 1:
                    return -1


