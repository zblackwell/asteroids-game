import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=1)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self, asteroids_group):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        spawn_angle = random.uniform(20, 50)
        new_angle1 = self.velocity.rotate(spawn_angle)
        new_angle2 = self.velocity.rotate(-spawn_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_astroid1.velocity = new_angle1 * 1.2
        asteroids_group.add(new_astroid1)

        new_astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_astroid2.velocity = new_angle2 * 1.2
        asteroids_group.add(new_astroid2)

        return 
        
