import sys
import pygame
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    Player.containers = (updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updatable in updatables:
            updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit()

        screen.fill("black")

        for drawable in drawables:
            drawable.draw(screen) #draw player

        pygame.display.flip()

        dt = clock.tick(60)/1000 #frame rate 60fps

if __name__ == "__main__":
    main()