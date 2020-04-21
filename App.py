import pygame
import sys

WINDOW_NAME = "Sudoku"
WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_START = 115
GRID_END = 585
BLANK = 65


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_NAME)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.drawWindow()
        self.drawGrid()
        pygame.display.update()

    def drawWindow(self):
        self.window.fill(WHITE)
        pygame.draw.rect(self.window, BLACK, (GRID_START, GRID_START, GRID_END, GRID_END), 3)

    def drawGrid(self):
        for gridPosition in range(9):
            if gridPosition % 3 == 0:
                pygame.draw.line(self.window, BLACK, (GRID_START + (gridPosition * BLANK), GRID_START),
                                 (GRID_START + (gridPosition * BLANK), GRID_START + GRID_END), 3)
            else:
                pygame.draw.line(self.window, BLACK, (GRID_START + (gridPosition * BLANK), GRID_START),
                                 (GRID_START + (gridPosition * BLANK), GRID_START + GRID_END), 1)
        for gridPosition in range(9):
            if gridPosition % 3 == 0:
                pygame.draw.line(self.window, BLACK, (GRID_START, GRID_START + (gridPosition * BLANK)),
                                 (GRID_START + GRID_END, GRID_START + (gridPosition * BLANK)), 3)
            else:
                pygame.draw.line(self.window, BLACK, (GRID_START, GRID_START + (gridPosition * BLANK)),
                                 (GRID_START + GRID_END, GRID_START + (gridPosition * BLANK)), 1)
