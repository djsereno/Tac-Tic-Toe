import pygame
import sys
import math
 
def drawLineRounded(surface, color, start_pos, end_pos, width):
    x1, y1 = start_pos
    x2, y2 = end_pos
    angle = math.atan((y2 - y1) / (x2 - x1))
    x1off = x1 + (width / 2) * math.cos(angle)
    y1off = y1 + (width / 2) * math.sin(angle)
    x2off = x2 - (width / 2) * math.cos(angle)
    y2off = y2 - (width / 2) * math.sin(angle)
    pygame.draw.line(surface, color, [x1off, y1off], [x2off, y2off], width)


def test():

    # Initialize pygame, settings, and screen object
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Test")

    # Start the main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((230, 230, 230))
        
        [x, y] = pygame.mouse.get_pos()
        lineColor = [0, 0, 255]
        lineWidth = 20
        start_pos = [100, 100]
        end_pos = [x, y]

        # pygame.draw.line(screen, lineColor, start_pos, end_pos, lineWidth)
        # pygame.draw.circle(screen, lineColor, start_pos, lineWidth / 2) 
        # pygame.draw.circle(screen, lineColor, end_pos, lineWidth / 2) 

        drawLineRounded(screen, lineColor, start_pos, end_pos, lineWidth)
        
        pygame.display.flip()

test()