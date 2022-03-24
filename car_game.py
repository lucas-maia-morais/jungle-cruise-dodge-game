import pygame
pygame.init()

# importing time module
import time

# importing random module
import random

# the screen
width = 800
height = 600
screen = pygame.display.set_mode((width,height))

# loading the image
carimg = pygame.image.load("car1.jpg")

# width of the car
car_width = 56

# loading all images
grass = pygame.image.load("grass.jpg")
yellow_strip = pygame.image.load("yellow_strip.jpg")
strip = pygame.image.load("strip.jpg")

# crashed message
myfont = pygame.font.SysFont("None", 100)
render_text = myfont.render("CAR CRASHED", 1, (0,0,0))


# time module
clock = pygame.time.Clock()
clock.tick(100)

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


# Function for adding the background image
def background():
    screen.blit(grass, (0,0))
    screen.blit(grass, (700,0))
    for i in range(7):
        screen.blit(yellow_strip,(400,100*i))
    screen.blit(strip, (120,0))
    screen.blit(strip, (680,0))


# image appearing
def car(x,y):
    screen.blit(carimg,(x,y))

# The game loop
def game_loop():
    bumped = False
    x_change = 0
    x = 400
    y = 470
    obstacle_speed = 10
    obs = 0
    y_change = 0
    obs_x = random.randrange(200, 650)
    obs_y = -750
    enemy_width = 56
    enemy_height = 125


    #close button
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Clicked")
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

        # background color

        screen.fill((119,119,119))
        background()
        # obs_y -= (obstacle_speed/4)
        obstacle(obs_x,obs_y,obs)
        obs_y += obstacle_speed

        # calling the function
        car(x,y)
        if x > 680 - car_width or x < 110:
            screen.blit(render_text, (100,200))
            pygame.display.update()
            time.sleep(5)
            game_loop()

        #updating the game
        pygame.display.update()
        clock.tick(100)

game_loop()
pygame.quit()
quit()

