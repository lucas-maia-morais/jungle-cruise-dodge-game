import pygame

# text_object_function
def text_object(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def ENCALHOU():
    myfont = pygame.font.SysFont("None", 100)
    game_over = myfont.render("Encalhou", 1, (0,0,0))
    return game_over

def NAUFRAGADO():
    myfont = pygame.font.SysFont("None", 100)
    game_over = myfont.render("Naufragado", 1, (0,0,0))
    return game_over

def quit_event(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()
        sys.exit()