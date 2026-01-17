import pygame, math
from entities.entity import Entity
from core.constants import WIDTH, HEIGHT, GOBLIN_COLOR, GOBLIN_RADIUS, GOBLIN_SPEED

class Goblin(Entity):
    def __init__(self, world):
        start_angle = 0
        pos = world.center + pygame.Vector2(world.radius, 0)
        super().__init__(pos=pos, radius=GOBLIN_RADIUS, color=GOBLIN_COLOR)
        self.speed = GOBLIN_SPEED
        self.world = world
        self.angle = start_angle

    def update(self, dt):
        self.angle += self.speed * dt

        self.angle %= (2*math.pi)

        self.pos = self.world.center + pygame.Vector2 (
            self.world.radius * math.cos(self.angle),
            self.world.radius * math.sin(self.angle)
        )