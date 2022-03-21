from turtle import width
import pygame
pygame.init()

# the screen
width = 800
height = 600
screen = pygame.display.set_mode((width,height))

# loading the image
carimg = pygame.image.load("car1.jpg")

# time module
clock = pygame.time.Clock()
clock.tick(100)

# For the caption
pygame.display.set_caption("Racing")

# image appearing
def car(x,y):
    screen.blit(carimg,(x,y))

# The game loop
def game_loop():
    bumped = False
    x_change = 0
    x = 400
    y = 470

    #close button
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True

        # moving in x-y coordinates
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        
        x += x_change

        # For the background color
        screen.fill((119,119,119))

        # calling the function
        car(x,y)

        #updating the game
        pygame.display.update()
        clock.tick(100)

game_loop()
pygame.quit()
quit()

