import pygame
from core.constants import *
from states.play import PlayState

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Escape THE Goblin")
        self.clock = pygame.time.Clock()
        self.running = True

        self.state = PlayState(self.screen)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.state.update(dt)

            self.screen.fill(BG_COLOR)
            self.state.draw()
            pygame.display.flip()

        pygame.quit()