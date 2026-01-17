from world.world import World
from entities.player import Player
from entities.goblin import Goblin

class PlayState:
    def __init__(self, screen):
        self.screen = screen
        self.world = World()
        self.player = Player(self.world)
        self.goblin = Goblin(self.world)

    def update(self, dt):
        self.player.handle_input(dt)
        self.goblin.update(dt)

    def draw(self):
        self.world.draw(self.screen)
        self.player.draw(self.screen)
        self.goblin.draw(self.screen)