import pygame

# color values
green = (0,200,0)
light_green = (0,255,0)
red = (200,0,0)
light_red = (255,0,0)
blue = (0,0,200)
light_blue = (0,0,255)

# loading all images
forest = pygame.image.load("images/forest.jpg")
boat = pygame.image.load("images/boat.jpg")
cruise = pygame.image.load("images/cruise.png")

# text_object_function
def text_object(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def ENCALHOU():
    myfont = pygame.font.SysFont("None", 100)
    game_over = myfont.render("Encalhou", 1, (0,0,0))
    return game_over

def NAUFRAGADO():
    myfont = pygame.font.SysFont("None", 100)
    game_over = myfont.render("Naufragado", 1, (0,0,0))
    return game_over