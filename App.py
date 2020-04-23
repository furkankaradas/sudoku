import pygame
import sys

# Settings
NEWGAMEBUTTON = (225, 40, 150, 50)
SOLVEBUTTON = (425, 40, 150, 50)
WHITE = (255, 255, 255)
WINDOW_NAME = "Sudoku"
BLACK = (0, 0, 0)
GRID_START = 115
GRID_END = 585
HEIGHT = 800
WIDTH = 800
BLANK = 65


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(WINDOW_NAME)
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.newButton = pygame.Rect(NEWGAMEBUTTON)
        self.solveButton = pygame.Rect(SOLVEBUTTON)
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
                if self.newButton.collidepoint(self.mousePosition):
                    print("New Game Button")
                if self.solveButton.collidepoint(self.mousePosition):
                    print("Solve Button")

    def update(self):
        self.mousePosition = pygame.mouse.get_pos()

    def draw(self):
        self.drawWindow()
        self.drawButton()
        self.drawGrid()
        self.fillGrid()
        pygame.display.update()

    def drawWindow(self):
        self.window.fill(WHITE)
        pygame.draw.rect(self.window, BLACK, (GRID_START, GRID_START, GRID_END, GRID_END), 3)

    def drawButton(self):
        # New Game Button
        pygame.draw.rect(self.window, BLACK, self.newButton, 3)
        text = pygame.font.Font('freesansbold.ttf', 18).render('New Game', True, BLACK)
        textRect = text.get_rect()
        textRect.center = (NEWGAMEBUTTON[0] + 75, NEWGAMEBUTTON[1] + 25)
        self.window.blit(text, textRect)

        # Solve Button
        pygame.draw.rect(self.window, BLACK, self.solveButton, 3)
        text = pygame.font.Font('freesansbold.ttf', 18).render('Solve', True, BLACK)
        textRect = text.get_rect()
        textRect.center = (SOLVEBUTTON[0] + 75, SOLVEBUTTON[1] + 25)
        self.window.blit(text, textRect)

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
        pygame.draw.rect(self.window, BLACK,
                         (self.selected[0] * BLANK + GRID_START,
                          self.selected[1] * BLANK + GRID_START, BLANK, BLANK))

    def mouseOnGrid(self):
        if GRID_START < self.mousePosition[0] < GRID_START + GRID_END and GRID_START < self.mousePosition[1] \
                < GRID_START + GRID_END:
            return (self.mousePosition[0] - GRID_START) // BLANK, (self.mousePosition[1] - GRID_START) // BLANK
        else:
            return GRID_START, GRID_START
