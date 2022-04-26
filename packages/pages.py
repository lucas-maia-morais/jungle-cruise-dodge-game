from codecs import backslashreplace_errors
import pygame
import sys
import random
import time

import packages.aux as aux
import packages.events as events
from packages.elements import Elements
from packages.environment import Environment



def intro_page(env,s,clock):
    background_font_path = "font/quicksilver-fast-font/QuicksilverFastRegular-DO3oE.ttf"
    intro_image = pygame.image.load("images/background.jpg")
    intro_image = pygame.transform.scale(intro_image,s.dimensions)

    s.screen.blit(intro_image,(0,0))
    font = pygame.font.Font(background_font_path, int(50*s.height/600))
    dim = font.size("Jungle Cruise Game")
    print(dim)
    title = font.render("Jungle Cruise Game", True, (192,192,192))
    print((int((s.width-dim[0])/2),int(50*s.height/600)))
    print(s.width)
    s.screen.blit(title,(int((s.width-dim[0])/2),int(50*s.height/600)))

    env.intro_loop(s,clock)


def countdown(env,s,clock):
    countdown = True
    while countdown:
        for event in pygame.event.get():
            events.quit_event(event)
        
        countdown = ['3','2','1','GO!']
        for count in countdown:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    events.quit_event(event)

            s.screen.fill((30,116,187))
            background(s)
            score_card(s, 0, 0, 0)
            largetext = pygame.font.Font("freesansbold.ttf",int(115*s.height/600))
            textSurf,textRect = events.text_object(count,largetext)
            textRect.center = ((s.width/2),(s.height/2))
            s.screen.blit(textSurf,textRect)

            pygame.display.update()
            clock.tick(1)
        
        game_page(env,s,clock)


def game_page(env,s,clock):
    env.game_loop(s,clock)

def background(s):
    s.screen.fill((30,116,187))
    forest = aux.forest
    forest = pygame.transform.scale(forest, (s.width*.15, s.height))
    s.screen.blit(forest, (0,0))
    s.screen.blit(forest, (.85*s.width,0))


# function for score card
def score_card(s, obstacle_passed, score, level):
    font = pygame.font.SysFont(None, 35)
    passed = font.render("Passed: "+str(obstacle_passed), True, (255,255,255))
    score = font.render("Score: "+str(score), True, (255,255,255))
    level = font.render("LEVEL: "+str(level), True, (255,255,255))
    s.screen.blit(passed, (0,int(50*s.height/600)))
    s.screen.blit(score, (0,int(100*s.height/600)))
    s.screen.blit(level, (0,int(150*s.height/600)))

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
        clock.tick(10)
