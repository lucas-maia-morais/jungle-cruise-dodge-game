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
stone = pygame.image.load("images/stone.png")
pirate = pygame.image.load("images/pirate.png")
aligator = pygame.image.load("images/aligator.jpg")

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

buttons = {
    'start': {'text': 'START', 'dim': (80/800, 500/600, 230/800, 550/600), 'color': green, 'alt_color': light_green, 'fs': ['pages.countdown(s,clock)']},
    'instruction': {'text': 'INSTRUCTIONS', 'dim': (320/800, 500/600, 470/800, 550/600), 'color': blue, 'alt_color': light_blue, 'fs': ['print("Instruction")']},
    'quit': {'text': 'QUIT', 'dim': (580/800, 500/600, 730/800, 550/600), 'color':red, 'alt_color':light_red, 'fs': ['pygame.quit()', 'quit()']}
}