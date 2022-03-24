from cgitb import small
from genericpath import samestat
import pygame
pygame.init()

# importing time module
import time

# importing random module
import random

# color values
green = (0,200,0)
light_green = (0,255,0)
red = (200,0,0)
light_red = (255,0,0)
blue = (0,0,200)
light_blue = (0,0,255)

# the screen
width = 800
height = 600
screen = pygame.display.set_mode((width,height))

# text_object_function
def text_object(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

# loading the image
carimg = pygame.image.load("car1.jpg")

intro_image = pygame.image.load("background.jpg")

def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(intro_image,(0,0))
        font = pygame.font.SysFont(None, 190)
        title = font.render("CAR GAME", True, (0,0,0))
        screen.blit(title,(50,50))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] > 80 and mouse[0] < 230 and mouse[1] > 500 and mouse[1] < 550:
            pygame.draw.rect(screen, light_green, (80,500,150,50))
            if click == (True, False, False):
                game_loop()
        else:
            pygame.draw.rect(screen,green,(80,500,150,50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = text_object("START", smallText)
        textRect.center = ((80 + (150/2)),(500+(50/2)))
        screen.blit(textSurface,textRect)
        
        if 470 > mouse[0] > 320 and 550 > mouse[1] > 500:
            pygame.draw.rect(screen,light_blue,(320,500,150,50))
        else:
            pygame.draw.rect(screen,blue,(320,500,150,50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = text_object("INSTRUCTIONS", smallText)
        textRect.center = ((320 + (150/2)),(500+(50/2)))
        screen.blit(textSurface,textRect)

        if 580 + 150 > mouse[0] > 580 and 500 + 50 > mouse[1] > 500:
            pygame.draw.rect(screen,light_red,(580,500,150,50))
            if click == (1,0,0):
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen,red,(580,500,150,50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = text_object("QUIT", smallText)
        textRect.center = ((580 + (150/2)),(500+(50/2)))
        screen.blit(textSurface,textRect)

        pygame.display.update()

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

# function for score card
def score_card(car_passed, score):
    font = pygame.font.SysFont(None, 35)
    passed = font.render("Passed: "+str(car_passed), True, (255,255,255))
    score = font.render("Score: "+str(score), True, (0,0,0))
    screen.blit(passed, (0,50))
    screen.blit(score, (0,100))


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
    car_passed = 0
    score = 0
    level = 0



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
                if event.key == pygame.K_s:
                    obstacle_speed += 2
                if event.key == pygame.K_b:
                    obstacle_speed -= 2
            
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

        # calling car function
        car(x,y)

        # calling score_card function
        score_card(car_passed, score)



        if x > 680 - car_width or x < 110:
            screen.blit(render_text, (100,200))
            pygame.display.update()
            time.sleep(5)
            game_loop()


        if obs_y > height:
            obs_y = 0 - enemy_height
            obs_x = random.randrange(170, width-170)
            obs = random.randrange(0,6)
            car_passed += 1
            score = car_passed * 10
            if int(car_passed) % 10 == 0:
                level += 1
                obstacle_speed += 2
                myfont = pygame.font.SysFont(None,100)
                level_text = myfont.render("Level "+str(level), 1, (0,0,0))
                screen.blit(level_text,(100,200))
                pygame.display.update()
                time.sleep(3)

        if y < obs_y + enemy_height:
            if x > obs_x  and x < obs_x + enemy_width or x + car_width > obs_x and x + car_width < obs_x + enemy_width:
                # print(x,obs_x,enemy_width)
                screen.blit(render_text,(100,200))
                pygame.display.update()
                time.sleep(5)
                game_loop()
            # right side
            # if x > obs_x or car_width + x > obs_x:

            # left side:
            # if x < obs_x + obs_width or x+car_width < obs_x + enemy_width

        #updating the game
        pygame.display.update()
        clock.tick(100)

## text_button()
intro_loop()
game_loop()
pygame.quit()
quit()

