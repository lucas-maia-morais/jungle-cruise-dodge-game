from codecs import backslashreplace_errors
import pygame
import sys
import random
import time

import packages.aux as aux
import packages.environment as environment
import packages.elements as elements

def intro_page(s,clock):
    intro = True
    background_font_path = "font/quicksilver-fast-font/QuicksilverFastRegular-DO3oE.ttf"
    intro_image = pygame.image.load("images/background.jpg")
    intro_image = pygame.transform.scale(intro_image,s.dimensions)

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        s.screen.blit(intro_image,(0,0))
        font = pygame.font.Font(background_font_path, 50)
        title = font.render("Jungle Cruise Game", True, (192,192,192))
        s.screen.blit(title,(50,50))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mouse[0] > 80 and mouse[0] < 230 and mouse[1] > 500 and mouse[1] < 550:
            pygame.draw.rect(s.screen, aux.light_green, (80,500,150,50))
            if click == (True, False, False):
                countdown(s,clock)
        else:
            pygame.draw.rect(s.screen,aux.green,(80,500,150,50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = aux.text_object("START", smallText)
        textRect.center = ((80 + (150/2)),(500+(50/2)))
        s.screen.blit(textSurface,textRect)
        
        if 470 > mouse[0] > 320 and 550 > mouse[1] > 500:
            pygame.draw.rect(s.screen,aux.light_blue,(320,500,150,50))
        else:
            pygame.draw.rect(s.screen,aux.blue,(320,500,150,50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = aux.text_object("INSTRUCTIONS", smallText)
        textRect.center = ((320 + (150/2)),(500+(50/2)))
        s.screen.blit(textSurface,textRect)

        if 580 + 150 > mouse[0] > 580 and 500 + 50 > mouse[1] > 500:
            pygame.draw.rect(s.screen,aux.light_red,(580,500,150,50))
            if click == (1,0,0):
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(s.screen,aux.red,(580,500,150,50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = aux.text_object("QUIT", smallText)
        textRect.center = ((580 + (150/2)),(500+(50/2)))
        s.screen.blit(textSurface,textRect)

        pygame.display.update()


def countdown(s,clock):
    countdown = True
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        
        countdown = ['3','2','1','GO!']
        for count in countdown:
            s.screen.fill((30,116,187))
            countdown_background(s)
            largetext = pygame.font.Font("freesansbold.ttf",115)
            textSurf,textRect = aux.text_object(count,largetext)
            textRect.center = ((s.width/2),(s.height/2))
            s.screen.blit(textSurf,textRect)

            pygame.display.update()
            clock.tick(1)
        
        game_loop(s,clock)

def countdown_background(s):
    background(s)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.quit()
    x = (s.width*0.45)
    y = (s.height*0.8)

    boat = pygame.transform.scale(aux.boat, (s.width*0.1, s.height*0.15))
    s.screen.blit(boat,(x,y))
    score_card(s, 0, 0)


def game_loop(s,clock):

    env = environment.Environment()
    boat = pygame.transform.scale(aux.boat, (s.width*0.1, s.height*0.15))
    player = elements.Player(s.width*0.45, s.height*0.8)
    x_change = 0
    y_change = 0
    obs = elements.Obstacle(random.uniform(0.15, 0.75)*s.width, 0)
    type = random.randint(1,3)
    obs2 = elements.Obstacle(random.uniform(0.15, 0.75)*s.width, -random.uniform(0, 0.3)*s.width)

    #close button
    while not env.bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Clicked")
                env.bumped = True

            # moving in x-y coordinates
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -0.05*s.width
                if event.key == pygame.K_RIGHT:
                    x_change =  0.05*s.width
                if event.key == pygame.K_UP:
                    y_change = -0.05*s.height
                if event.key == pygame.K_DOWN:
                    y_change =  0.05*s.height
                if event.key == pygame.K_s:
                    env.obstacle_speed += 2
                if event.key == pygame.K_b:
                    env.obstacle_speed -= 2
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        
        player.x += x_change
        player.y += y_change

        
        background(s)
        obs.show(s)
        obs2.show(s, type)

        # position of obstacle
        obs.y += env.obstacle_speed
        obs2.y += env.obstacle_speed

        # calling to print player
        player.show(s)

        # calling score_card function
        score_card(s, env.car_passed, env.score)


        if player.x > (0.85 - player.width/2)*s.width or player.x < (0.15 + player.width/2)*s.width:            
            s.screen.blit(aux.ENCALHOU(), (s.width*0.1,s.height*0.5))
            pygame.display.update()
            time.sleep(5)
            game_loop(s,clock)

        print(obs.y)

        if obs.y > s.height:
            obs_y = 0 - 0.15*s.height
            obs_x = random.uniform(0.15, 0.75)*s.width
            obs = elements.Obstacle(obs_x, obs_y)
            env.car_passed += 1
            env.score = env.car_passed * 10
            if int(env.car_passed) % 10 == 0:
                env.level += 1
                env.obstacle_speed += 2
                myfont = pygame.font.SysFont(None,100)
                level_text = myfont.render("Level "+str(env.level), 1, (0,0,0))
                s.screen.blit(level_text,(s.width*0.1,s.height*0.5))
                pygame.display.update()
                time.sleep(3)

        if obs2.y > s.height:
            type = random.randint(1,3)
            obs_y = 0 - random.uniform(0.15, 0.5)*s.height
            obs_x = random.uniform(0.15, 0.75)*s.width
            obs2 = elements.Obstacle(obs_x, obs_y)

        if ((player.y < obs.y + 0.15*s.height) and (player.y + 0.15*s.height > obs.y)):
            # if player.x > obs.y  and player.x < obs.x + 0.1*s.width or player.x + 0.1*s.width > obs.x and player.x + 0.1*s.width < obs.x + 0.1*s.width:
            if (player.x < obs.x + 0.1*s.width) and (player.x + 0.1*s.width > obs.x):
                # print(x,obs_x,enemy_width)
                s.screen.blit(aux.NAUFRAGADO(),(100,200))
                pygame.display.update()
                time.sleep(5)
                game_loop(s, clock)
            # right side
            # if x > obs_x or car_width + x > obs_x:

            # left side:
            # if x < obs_x + obs_width or x+car_width < obs_x + enemy_width

        pygame.draw.rect(s.screen,aux.blue,(0.9*s.width,0,0.1*s.width,0.1*s.height))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if mouse[0] > 0.9*s.width and mouse[0] < s.width and mouse[1] > 0 and mouse[1] < 0.1*s.height:
            pygame.draw.rect(s.screen,aux.light_blue,(0.9*s.width,0,0.1*s.width,0.1*s.height))
            if click == (1,0,0):
                paused(s,clock)
        else:
            pygame.draw.rect(s.screen,aux.blue,(0.9*s.width,0,0.1*s.width,0.1*s.height))

        smalltext = pygame.font.Font("freesansbold.ttf",30)
        textSurf, textRect = aux.text_object("PAUSE",smalltext)
        textRect.center = ((0.9+0.1/2)*s.width,(0+(0.1/2)*s.height))
        s.screen.blit(textSurf, textRect)

        #updating the game
        pygame.display.update()
        clock.tick(10)


def background(s):
    s.screen.fill((30,116,187))
    forest = aux.forest
    forest = pygame.transform.scale(forest, (s.width*.15, s.height))
    s.screen.blit(forest, (0,0))
    s.screen.blit(forest, (.85*s.width,0))


# function for score card
def score_card(s, obstacle_passed, score):
    font = pygame.font.SysFont(None, 35)
    passed = font.render("Passed: "+str(obstacle_passed), True, (255,255,255))
    score = font.render("Score: "+str(score), True, (0,0,0))
    s.screen.blit(passed, (0,50))
    s.screen.blit(score, (0,100))

def paused(s, clock):
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        pause_image = pygame.image.load("images/jungle-cruise.jpg")
        pause_image = pygame.transform.scale(pause_image,s.dimensions)
        s.screen.blit(pause_image,(0,0))

        largetext = pygame.font.Font("freesansbold.ttf",115)
        textSurf,textRect = aux.text_object("PAUSED", largetext)
        textRect.center = ((s.width/2),(s.height/8))
        s.screen.blit(textSurf,textRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # for continue
        if mouse[0] > 100 and mouse[0] < 250 and mouse[1] > 450 and mouse[1] < 500:
            pygame.draw.rect(s.screen,aux.light_green,(100,450,150,50))
            if click == (1,0,0):
                pause = False
        else:
            pygame.draw.rect(s.screen,aux.green,(100,450,150,50))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf,textRect = aux.text_object("CONTINUE", smallText)
        textRect.center = ((100+(150/2)),(450+(50/2)))
        s.screen.blit(textSurf, textRect)

        # for restart
        if mouse[0] > 350 and mouse[0] < 500 and mouse[1] > 450 and mouse[1] < 500:
            pygame.draw.rect(s.screen,aux.light_blue,(350,450,150,50))
            if click == (1,0,0):
                game_loop()
        else:
            pygame.draw.rect(s.screen,aux.blue,(350,450,150,50))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf,textRect = aux.text_object("RESTART", smallText)
        textRect.center = ((350+(150/2)),(450+(50/2)))
        s.screen.blit(textSurf, textRect)

        # for main menu
        if mouse[0] > 600 and mouse[0] < 750 and mouse[1] > 450 and mouse[1] < 500:
            pygame.draw.rect(s.screen,aux.light_red,(600,450,150,50))
            if click == (1,0,0):
                intro_page()
        else:
            pygame.draw.rect(s.screen,aux.red,(600,450,150,50))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf,textRect = aux.text_object("MAIN MENU", smallText)
        textRect.center = ((600+(150/2)),(450+(50/2)))
        s.screen.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(30)
