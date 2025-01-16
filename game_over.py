import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def display_game_over_screen(screen):
    font = pygame.font.Font(None, 74)
    font2 = pygame.font.Font(None, 45)

    text = font.render("GAME OVER", True, (255, 255, 255))
    text2 = font2.render("press R to restart", True, (150, 150, 150))

    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 
    SCREEN_HEIGHT // 2 - text.get_height() // 2))

    screen.blit(text2, (SCREEN_WIDTH // 2 - text2.get_width() // 2, SCREEN_HEIGHT // 2 - (text2.get_height() //2) + text.get_height()))
    pygame.display.flip()