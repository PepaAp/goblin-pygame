import time, pygame
from world.world import World
from entities.player import Player
from entities.goblin import Goblin
from core.constants import WIDTH, TIMER_COLOR, TIMER_SIZE

class PlayState:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.world = World()
        self.player = Player(self.world)
        self.goblin = Goblin(self.world)

        self.start_time = time.time()

    def update(self, dt):
        self.player.handle_input(dt)
        self.goblin.update(dt, self.player.pos)

        if self.player.collides_with(self.goblin):
            self.game.restart()

    def draw(self):
        self.world.draw(self.screen)
        self.player.draw(self.screen)
        self.goblin.draw(self.screen)

        elapsed = time.time() - self.start_time
        font = pygame.font.SysFont(None, TIMER_SIZE)
        text = font.render(f"Timer: {elapsed:.1f} sec.", True, TIMER_COLOR)
        self.screen.blit(text, (10, 10))