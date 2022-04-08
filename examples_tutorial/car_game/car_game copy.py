from cgitb import small
from genericpath import samestat
import pygame
pygame.init()

# importing time module
import time

# importing random module
import random

# loading the image
carimg = pygame.image.load("car1.jpg")

instruction_background = pygame.image.load("background2.jpg")

# width of the car
car_width = 56

# crashed message
myfont = pygame.font.SysFont("None", 100)
render_text = myfont.render("CAR CRASHED", 1, (0,0,0))

# For the caption
pygame.display.set_caption("Racing")

# Function for the obstacle
def obstacle(obs_x, obs_y, obs):
    if obs == 0:
        obs_pic = pygame.image.load("car2.jpg")
    elif obs == 1:
        obs_pic = pygame.image.load("car3.jpg")
    elif obs == 2:
        obs_pic = pygame.image.load("car4.jpg")
    elif obs == 3:
        obs_pic = pygame.image.load("car5.jpg")
    elif obs == 4:
        obs_pic = pygame.image.load("car6.jpg")
    elif obs == 5:
        obs_pic = pygame.image.load("car7.jpg")

    # screen.blit(obs_pic, (obs_x,obs_y))
    screen.blit(obs_pic, (obs_x,obs_y))


## text_button()
intro_loop()
game_loop()
pygame.quit()
quit()