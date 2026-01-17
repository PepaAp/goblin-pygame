import time, pygame
from world.world import World
from entities.player import Player
from entities.goblin import Goblin
from core.constants import WIDTH, HEIGHT, TIMER_COLOR, TIMER_SIZE

class PlayState:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.world = World()
        self.player = Player(self.world)
        self.goblin = Goblin(self.world)

        self.start_time = time.time()
        self.dead = False
        self.dead_time = 0

    def update(self, dt):
        if self.dead:
            if time.time() - self.dead_time > 2:
                self.game.restart()
            return

        self.player.handle_input(dt)
        self.goblin.update(dt, self.player.pos)

        if self.player.collides_with(self.goblin):
            self.dead = True
            self.dead_time = time.time()

    def draw(self):
        self.world.draw(self.screen)
        self.player.draw(self.screen)
        self.goblin.draw(self.screen)

        elapsed = time.time() - self.start_time
        font = pygame.font.SysFont(None, TIMER_SIZE)
        text = font.render(f"Time: {elapsed:.1f} sec.", True, TIMER_COLOR)
        self.screen.blit(text, (10, 10))
        
        if self.dead:
            font = pygame.font.SysFont(None, 60)
            text = font.render("YOU HAVE BEEN CAUGHT", True, (255, 20, 20))
            rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(text, rect)