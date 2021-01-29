import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
window.fill(BG_COLOR)
# location, color, start, end, width
# pygame.draw.line(window, RED, (10, 10), (300, 300), 10)


def draw_lines():
    # first horizontal line
    # location, color, start position, end position, width
    pygame.draw.line(window, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # second horizontal line
    pygame.draw.line(window, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # first vertical line
    pygame.draw.line(window, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # second vertical line
    pygame.draw.line(window, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


draw_lines()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
