import pygame
import sys
import time
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from game_over import *

def reset_game(player, asteroids, shots, asteroid_field, updatables, drawables):
    global game_over

    player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player.velocity = pygame.Vector2(0, 0)
    player.rotation = 0
    player.rate_limit = 0

    updatables.empty()
    drawables.empty()
    asteroids.empty()
    shots.empty()

    asteroid_field = AsteroidField()

    updatables.add(player)
    drawables.add(player)

def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:  # Restart the game when space is pressed
                reset_game(player, asteroids, shots, asteroid_field, updatables, drawables)  # Reset game state
                game_over = False
            if keys[pygame.K_q]:
                sys.exit()

        if not game_over:
            # Update all objects in the game
            for updatable in updatables:
                updatable.update(dt)

            # Check for collisions
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    player.kill()  # Kill player, trigger game over
                    game_over = True

                for shot in shots:
                    if asteroid.collides_with(shot):
                        shot.kill()
                        asteroid.split()

        screen.fill("black")

        # Draw all sprites
        for drawable in drawables:
            drawable.draw(screen)

        if game_over:
            display_game_over_screen(screen)

        pygame.display.flip()  # Update the display

        # Control the frame rate
        dt = clock.tick(60) / 1000  # 60fps

if __name__ == "__main__":
    main()