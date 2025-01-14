import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        player.draw(screen) #draw player
        pygame.display.flip()

        dt = clock.tick(60)/1000 #frame rate 60fps

if __name__ == "__main__":
    main()
