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

# info for buttons
buttons = {
    'start': {'text': 'START', 'dim': (80/800, 500/600, 240/800, 550/600), 'color': green, 'alt_color': light_green, 'fs': ['pages.countdown(self,s,clock)']},
    'instruction': {'text': 'INSTRUCTIONS', 'dim': (320/800, 500/600, 480/800, 550/600), 'color': blue, 'alt_color': light_blue, 'fs': ['print("Instruction")']},
    'quit': {'text': 'QUIT', 'dim': (560/800, 500/600, 720/800, 550/600), 'color':red, 'alt_color':light_red, 'fs': ['pygame.quit()', 'quit()']},
    'pause': {'text': 'PAUSE', 'dim': (640/800, 0/600, 800/800, 50/600), 'color':blue, 'alt_color':red, 'fs': ['pages.paused(s,clock)']}
}