import pygame
import sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_WIDTH = 25
SPACE = 50
CROSS_COLOR = (66, 66, 66)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
window.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


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


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(window, CIRCLE_COLOR, (int(
                    col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(window, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE -
                                                       SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(window, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


draw_lines()

player = 1
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            clicked_row = int(mouse_y // 200)
            clicked_col = int(mouse_x // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1
                draw_figures()

    pygame.display.update()
