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

def paused(env,s,clock):
    pause_image = pygame.image.load("images/jungle-cruise.jpg")
    pause_image = pygame.transform.scale(pause_image,s.dimensions)
    s.screen.blit(pause_image,(0,0))
    
    env.pause_loop(s,clock)
