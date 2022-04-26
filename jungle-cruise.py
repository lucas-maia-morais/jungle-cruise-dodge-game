import pygame
import packages.pages as pages
import packages.screen as screen
from packages.environment import Environment

if __name__ == '__main__':

    
    pygame.init()

    # time module
    clock = pygame.time.Clock()
    clock.tick(20)

    # Inicializar tela

    s = screen.Screen()
    env = Environment()
    pages.intro_page(env, s,clock)

    pygame.quit()
    quit()
