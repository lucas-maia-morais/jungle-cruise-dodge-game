import pygame
import packages.screen as screen

if __name__ == '__main__':

    
    pygame.init()

    # time module
    clock = pygame.time.Clock()
    clock.tick(20)

    # Inicializar tela

    s = screen.Screen(clock)
    s.intro_page()

    pygame.quit()
    quit()
