from world.world import World
from entities.player import Player

class PlayState:
    def __init__(self, screen):
        self.screen = screen
        self.world = World()
        self.player = Player(self.world)

    def update(self, dt):
        self.player.handle_input(dt)

    def draw(self):
        self.world.draw(self.screen)
        self.player.draw(self.screen)