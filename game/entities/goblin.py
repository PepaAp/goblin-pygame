import pygame
from entities.entity import Entity
from core.constants import WIDTH, HEIGHT, GOBLIN_COLOR, GOBLIN_RADIUS, GOBLIN_SPEED

class Goblin(Entity):
    def __init__(self, world):
        start_angle = 0
        pos = world.center + pygame.Vector2(world.radius, 0)
        super().__init__(pos=pos, radius=GOBLIN_RADIUS, color=GOBLIN_COLOR)
        self.speed = GOBLIN_SPEED
        self.world = world

    def update(self, dt):
        self.angle += self.speed * dt