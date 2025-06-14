from constants import *
import sys
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    initialized = pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    roids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, roids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color(0,0,0))
        updateable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for roid in roids:
            if (player.collide(roid)):
                print("Game over!")
                sys.exit(0)
            for shot in shots:
                if (roid.collide(shot)):
                    shot.kill()
                    roid.split()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    
if __name__ == "__main__":
    main()
