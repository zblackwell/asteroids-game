import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt, direction):
            self.rotation += PLAYER_TURN_SPEED * dt * direction

    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * direction
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, -1)
        if keys[pygame.K_d]:
            self.rotate(dt, 1)

        if keys[pygame.K_w]:
            self.move(dt, 1)
        if keys[pygame.K_s]:
            self.move(dt, -1)

        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN

    def shoot(self):
        bullet = Shot(self.position.x, self.position.y , self.rotation)
        #bullet.velocity *= PLAYER_SHOOT_SPEED
    


    