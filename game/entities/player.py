import pygame
from entities.entity import Entity
from core.constants import WIDTH, HEIGHT, PLAYER_SPEED, PLAYER_RADIUS, PLAYER_COLOR

class Player(Entity):
    def __init__(self, world):
        super().__init__(world.center, PLAYER_RADIUS, PLAYER_COLOR)
        self.speed = PLAYER_SPEED
        self.world = world
    
    def handle_input(self, dt):
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            direction = mouse_pos - self.pos

            if direction.length() > 0:
                direction = direction.normalize() * self.speed * dt
                self.pos += direction

        self.pos = self.world.lake_stuck_position(self.pos, buffer = self.radius - PLAYER_RADIUS*2.2)

        """ keys = pygame.key.get_pressed()
        move = pygame.Vector2(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            move.y = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            move.y = 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            move.x = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            move.x = 1

        if move.length() > 0:
            move = move.normalize() * self.speed * dt
            self.pos += move """