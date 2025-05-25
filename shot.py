import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        
        #self.radius = radius
        direction_vec = pygame.Vector2(0, 1).rotate(direction)
        offset_distance = PLAYER_RADIUS + SHOT_RADIUS
        self.position = pygame.Vector2(x, y) + direction_vec * offset_distance
        self.velocity = pygame.Vector2(0, 1).rotate(direction) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)