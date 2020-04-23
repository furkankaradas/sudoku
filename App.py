import pygame
import sys

WINDOW_NAME = "Sudoku"
WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKYBLUE = (135, 206, 235)
GRID_START = 115
GRID_END = 585
BLANK = 65


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_NAME)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.mousePosition = None
        self.selected = (GRID_START, GRID_START)

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
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected = self.mouseOnGrid()

    def update(self):
        self.mousePosition = pygame.mouse.get_pos()

    def draw(self):
        self.drawWindow()
        self.drawGrid()
        self.fillGrid()
        pygame.display.update()

    def drawWindow(self):
        self.window.fill(WHITE)
        pygame.draw.rect(self.window, BLACK, (GRID_START, GRID_START, GRID_END, GRID_END), 3)

    def drawGrid(self):
        # Horizontal Vertices
        for gridPosition in range(9):
            if gridPosition % 3 == 0:
                pygame.draw.line(self.window, BLACK, (GRID_START + (gridPosition * BLANK), GRID_START),
                                 (GRID_START + (gridPosition * BLANK), GRID_START + GRID_END), 3)
            else:
                pygame.draw.line(self.window, BLACK, (GRID_START + (gridPosition * BLANK), GRID_START),
                                 (GRID_START + (gridPosition * BLANK), GRID_START + GRID_END), 1)
        # Vertical Vertices
        for gridPosition in range(9):
            if gridPosition % 3 == 0:
                pygame.draw.line(self.window, BLACK, (GRID_START, GRID_START + (gridPosition * BLANK)),
                                 (GRID_START + GRID_END, GRID_START + (gridPosition * BLANK)), 3)
            else:
                pygame.draw.line(self.window, BLACK, (GRID_START, GRID_START + (gridPosition * BLANK)),
                                 (GRID_START + GRID_END, GRID_START + (gridPosition * BLANK)), 1)

    def fillGrid(self):
        pygame.draw.rect(self.window, SKYBLUE,
                         (self.selected[0] * BLANK + GRID_START,
                          self.selected[1] * BLANK + GRID_START, BLANK, BLANK))

    # posX = (self.mousePosition[0] - GRID_START) // BLANK
    # posY = (self.mousePosition[1] - GRID_START) // BLANK
    def mouseOnGrid(self):
        if GRID_START < self.mousePosition[0] < GRID_START + GRID_END and GRID_START < self.mousePosition[1] \
                < GRID_START + GRID_END:
            return (self.mousePosition[0] - GRID_START) // BLANK, (self.mousePosition[1] - GRID_START) // BLANK
        else:
            return GRID_START, GRID_START
