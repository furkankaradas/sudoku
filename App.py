import pygame
import sys

WINDOW_NAME = "Sudoku"
WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)


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
        self.window.fill(WHITE)
        pygame.display.update()
