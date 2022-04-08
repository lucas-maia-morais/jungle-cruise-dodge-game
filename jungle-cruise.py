import pygame
import packages.pages as pages
import packages.screen as screen

if __name__ == '__main__':

    
    pygame.init()

    # time module
    clock = pygame.time.Clock()
    clock.tick(100)

    # Inicializar tela

    s = screen.Screen()
    pages.intro_page(s,clock)
