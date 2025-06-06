from constants import *
import pygame
import random
import circleshape

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
 
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("white"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS
        roid1 = Asteroid(self.position.x, self.position.y, radius)
        roid1.velocity = self.velocity.rotate(angle) * 1.2
        roid2 = Asteroid(self.position.x, self.position.y, radius)
        roid2.velocity = self.velocity.rotate(-angle) * 1.2