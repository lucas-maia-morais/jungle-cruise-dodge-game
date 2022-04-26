import pygame
import random
import time
import packages.aux as aux
import packages.pages as pages
import packages.events as events
import packages.elements as Elements


class Environment:
    def __init__(self):
        self.__bumped = False
        self.__obstacle_speed = 10
        self.obs = 0
        self.y_change = 0
        self.__car_passed = 0
        self.__score = 0
        self.__level = 0
        self.obstacles = {}
        self._obs_id = -1

    @property
    def bumped(self):
        return self.__bumped

    @bumped.setter
    def bumped(self, bumped):
        self.__bumped = bumped

    @property
    def obstacle_speed(self):
        return self.__obstacle_speed

    @obstacle_speed.setter
    def obstacle_speed(self, obstacle_speed):
        self.__obstacle_speed = obstacle_speed

    @property
    def car_passed(self):
        return self.__car_passed

    @car_passed.setter
    def car_passed(self, car_passed):
        self.__car_passed = car_passed

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    def generate_obstacle(self, s):
        self._obs_id += 1
        obs_type = random.randint(0,3)
        obs = Elements.Obstacle(self._obs_id, obs_type, random.uniform(0.15, 0.75)*s.width, -random.uniform(0, 0.3)*s.width)
        self.obstacles[self._obs_id] = obs
        return obs

    def destroy_obstacle(self, obs):
        self.obstacles.pop(obs.id)
    
    def inside_check(self,s,clock):
        if self.player.x > (0.85 - self.player.width/2)*s.width or self.player.x < (0.15 + self.player.width/2)*s.width:            
            s.screen.blit(events.ENCALHOU(), (s.width*0.1,s.height*0.5))
            pygame.display.update()
            time.sleep(5)
            self.game_loop(s,clock)
    
    def renew_obstacles(self,s,clock):
        to_destroy = []
        for obs in self.obstacles.values():
            if obs.y > s.height:
                to_destroy.append(obs)
                self.car_passed += 1
                self.score = self.car_passed * 10
                if int(self.car_passed) % 10 == 0:
                    self.level += 1
                    self.obstacle_speed += 2
                    myfont = pygame.font.SysFont(None,100)
                    level_text = myfont.render("Level "+str(self.level), 1, (0,0,0))
                    s.screen.blit(level_text,(s.width*0.1,s.height*0.5))
                    pygame.display.update()
                    time.sleep(3)

        for obs in to_destroy: 
            self.destroy_obstacle(obs)
            self.generate_obstacle(s)
    
    def check_collisions(self,s,clock):
        for obs in self.obstacles.values():
            if ((self.player.y < obs.y + 0.15*s.height) and (self.player.y + 0.15*s.height > obs.y)):
                    if (self.player.x < obs.x + 0.1*s.width) and (self.player.x + 0.1*s.width > obs.x):
                        s.screen.blit(events.NAUFRAGADO(),(100,200))
                        pygame.display.update()
                        time.sleep(5)
                        self.game_loop(s, clock)


    def screen_button(self,s,clock,button):
        button = aux.buttons[button]
        dim = button['dim']
        x0 = s.width*dim[0]
        y0 = s.height*dim[1]
        x1 = s.width*dim[2]
        y1 = s.height*dim[3]
        if self._mouse[0] > x0 and self._mouse[0] < x1 and self._mouse[1] > y0 and self._mouse[1] < y1:
            pygame.draw.rect(s.screen, button['alt_color'], (x0,y0,x1-x0,y1-y0))
            if self._click == (True, False, False):
                for f in button['fs']:
                    eval(f)
        else:
            pygame.draw.rect(s.screen,button['color'],(x0,y0,x1-x0,y1-y0))

        smallText = pygame.font.Font("freesansbold.ttf", int((y1-y0)/3))
        textSurface, textRect = events.text_object(button['text'], smallText)
        textRect.center = ((x0+x1)/2,(y0+y1)/2)
        s.screen.blit(textSurface,textRect)

    def intro_loop(self,s,clock):
        intro = True
        while intro:
            for event in pygame.event.get():
                events.quit_event(event)
            self._mouse = pygame.mouse.get_pos()
            self._click = pygame.mouse.get_pressed()

            self.screen_button(s, clock, 'start')
            self.screen_button(s, clock, 'instruction')
            self.screen_button(s, clock, 'quit')

            pygame.display.update()
    
    def game_loop(self,s,clock):
        boat = pygame.transform.scale(aux.boat, (s.width*0.1, s.height*0.15))
        # player = Elements.Player(s.width*0.45, s.height*0.8)
        x_change = 0
        y_change = 0
        
        self.obstacles.clear()
        self.player = Elements.Player(s.width*0.45, s.height*0.8)
        obs = self.generate_obstacle(s)

        #close button
        while not self.bumped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bumped = True

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
                        self.obstacle_speed += 2
                    if event.key == pygame.K_b:
                        self.obstacle_speed -= 2
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0
            
            self.player.x += x_change
            self.player.y += y_change

            
            pages.background(s)
            obs.show(s)

            # position of obstacle
            for obs in self.obstacles.values():
                obs.y += self.obstacle_speed

            # calling to print player
            self.player.show(s)

            # calling score_card function
            pages.score_card(s, self.car_passed, self.score, self.level)

            # Possible events
            self.inside_check(s,clock)
            self.renew_obstacles(s, clock)
            self.check_collisions(s,clock)

            self._mouse = pygame.mouse.get_pos()
            self._click = pygame.mouse.get_pressed()
            self.screen_button(s, clock, 'pause')

            #updating the game
            pygame.display.update()
            clock.tick(20)