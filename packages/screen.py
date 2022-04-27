import pygame
import time
import packages.aux as aux
import packages.events as events
import packages.elements as Elements

from packages.environment import Environment

class Screen:
    def __init__(self, clock, width=800, height=600):
        self._clock = clock
        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode((self.__width, self.__height))

    def change_display(self):
        self.__screen = pygame.display.set_mode((self.__width, self.__height))

    @property
    def screen(self):
        return self.__screen

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    @property
    def dimensions(self):
        return (self.__width, self.__height)

    @width.setter
    def width(self, width):
        self.__width = width
        self.change_display()
    
    @height.setter
    def height(self, height):
        self.__height = height
        self.change_display()

    def intro_page(self):
        background_font_path = "font/quicksilver-fast-font/QuicksilverFastRegular-DO3oE.ttf"
        intro_image = pygame.image.load("images/background.jpg")
        intro_image = pygame.transform.scale(intro_image,self.dimensions)

        self.screen.blit(intro_image,(0,0))
        font = pygame.font.Font(background_font_path, int(50*self.height/600))
        dim = font.size("Jungle Cruise Game")
        title = font.render("Jungle Cruise Game", True, (192,192,192))
        self.screen.blit(title,(int((self.width-dim[0])/2),int(50*self.height/600)))

        self.intro_loop()

    def intro_loop(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                events.quit_event(event)
            self._mouse = 0
            self._click = 0
            self._mouse = pygame.mouse.get_pos()
            self._click = pygame.mouse.get_pressed()

            self.screen_button('start')
            self.screen_button('instruction')
            self.screen_button('quit')

            pygame.display.update()

    def screen_button(self,button):
        button = aux.buttons[button]
        dim = button['dim']
        x0 = self.width*dim[0]
        y0 = self.height*dim[1]
        x1 = self.width*dim[2]
        y1 = self.height*dim[3]
        if self._mouse[0] > x0 and self._mouse[0] < x1 and self._mouse[1] > y0 and self._mouse[1] < y1:
            pygame.draw.rect(self.screen, button['alt_color'], (x0,y0,x1-x0,y1-y0))
            if self._click == (True, False, False):
                for f in button['fs']:
                    exec(f)
        else:
            pygame.draw.rect(self.screen,button['color'],(x0,y0,x1-x0,y1-y0))

        smallText = pygame.font.Font("freesansbold.ttf", int((y1-y0)/3))
        textSurface, textRect = events.text_object(button['text'], smallText)
        textRect.center = ((x0+x1)/2,(y0+y1)/2)
        self.screen.blit(textSurface,textRect)

    def countdown(self):
        countdown = ['3','2','1','GO!']
        self._env = Environment()
        pygame.display.update()
        for count in countdown:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    events.quit_event(event)

            self.screen.fill((30,116,187))
            self.background()
            self.score_card()
            largetext = pygame.font.Font("freesansbold.ttf",int(115*self.height/600))
            textSurf,textRect = events.text_object(count,largetext)
            textRect.center = ((self.width/2),(self.height/2))
            self.screen.blit(textSurf,textRect)

            pygame.display.update()
            self._clock.tick(1)
        
        self.game_page()

    def background(self):
        self.screen.fill((30,116,187))
        forest = aux.forest
        forest = pygame.transform.scale(forest, (self.width*.15, self.height))
        self.screen.blit(forest, (0,0))
        self.screen.blit(forest, (.85*self.width,0))

    # function for score card
    def score_card(self):
        font = pygame.font.SysFont(None, 35)
        passed = font.render("Passed: "+str(self._env.obstacles_passed), True, (255,255,255))
        score = font.render("Score: "+str(self._env.score), True, (255,255,255))
        level = font.render("LEVEL: "+str(self._env.level), True, (255,255,255))
        self.screen.blit(passed, (0,int(50*self.height/600)))
        self.screen.blit(score, (0,int(100*self.height/600)))
        self.screen.blit(level, (0,int(150*self.height/600)))

    def game_page(self):
        self.game_loop()

    def game_loop(self):
        boat = pygame.transform.scale(aux.boat, (self.width*0.1, self.height*0.15))
        x_change = 0
        y_change = 0
        
        self._env.obstacles.clear()
        self._env.player = Elements.Player(self.width*0.45, self.height*0.8)
        obs = self._env.generate_obstacle(self)

        #close button
        while not self._env.bumped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bumped = True

                # moving in x-y coordinates
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -0.05*self.width
                    if event.key == pygame.K_RIGHT:
                        x_change =  0.05*self.width
                    if event.key == pygame.K_UP:
                        y_change = -0.05*self.height
                    if event.key == pygame.K_DOWN:
                        y_change =  0.05*self.height
                    if event.key == pygame.K_s:
                        self._env.obstacle_speed += 2
                    if event.key == pygame.K_b:
                        self._env.obstacle_speed -= 2
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0
            
            self._env.player.x += x_change
            self._env.player.y += y_change
            
            self.background()
            obs.show(self)

            # position of obstacles
            for obs in self._env.obstacles.values():
                obs.y += self._env.obstacle_speed

            # calling to print player
            self._env.player.show(self)

            # calling score_card function
            self.score_card()

            # Possible events
            self._env.inside_check(self, self._clock)
            self._env.renew_obstacles(self, self._clock)
            self._env.check_collisions(self, self._clock)

            self._mouse = pygame.mouse.get_pos()
            self._click = pygame.mouse.get_pressed()
            self.screen_button('pause')

            #updating the game
            pygame.display.update()
            self._clock.tick(20)
    
    def paused(self):
        pause_image = pygame.image.load("images/jungle-cruise.jpg")
        pause_image = pygame.transform.scale(pause_image,self.dimensions)
        self.screen.blit(pause_image,(0,0))
        
        self.pause_loop()
    
    def pause_loop(self):
        self._pause = True
        while self._pause:
            for event in pygame.event.get():
                events.quit_event(event)

            events.event_message(self,'PAUSED')

            self._mouse = pygame.mouse.get_pos()
            self._click = pygame.mouse.get_pressed()
            self.screen_button('continue')
            self.screen_button('restart')
            self.screen_button('menu')

            pygame.display.update()
            self._clock.tick(10)

