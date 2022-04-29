import pygame
import time
import packages.aux as aux
import packages.events as events
import packages.elements as Elements

from packages.environment import Environment

class Screen:
    def __init__(self, clock, width=800, height=600):
        self.clock = clock
        self.__width = width
        self.__height = height
        self.__screen = pygame.display.set_mode((self.width, self.height))

    def change_display(self):
        self.screen = pygame.display.set_mode((self.width, self.height))

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
        background_font_path = "font/kahlil-font/Kahlil-YzP9L.ttf"
        intro_image = pygame.image.load("images/background.jpg")
        intro_image = pygame.transform.scale(intro_image,self.dimensions)

        self.screen.blit(intro_image,(0,0))
        font = pygame.font.Font(background_font_path, int(50*self.height/600))
        dim = font.size("Jungle Cruise Game")
        title = font.render("Jungle Cruise Game", True, (255,200,0))
        self.screen.blit(title,(int((self.width-dim[0])/2),int(50*self.height/600)))

        self.intro_loop()

    def intro_loop(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                events.quit_event(event)
            self.mouse = 0
            self.click = 0
            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()

            self.screen_button('start')
            #self.screen_button('instruction')
            self.screen_button('quit')

            pygame.display.update()

    def screen_button(self,button):
        button = aux.buttons[button]
        dim = button['dim']
        x0 = self.width*dim[0]
        y0 = self.height*dim[1]
        x1 = self.width*dim[2]
        y1 = self.height*dim[3]
        if self.mouse[0] > x0 and self.mouse[0] < x1 and self.mouse[1] > y0 and self.mouse[1] < y1:
            pygame.draw.rect(self.screen, button['alt_color'], (x0,y0,x1-x0,y1-y0))
            if self.click == (True, False, False):
                for f in button['fs']:
                    exec(f)
        else:
            pygame.draw.rect(self.screen,button['color'],(x0,y0,x1-x0,y1-y0))

        smallText = pygame.font.Font("font/kahlil-font/Kahlil-YzP9L.ttf", int((y1-y0)/3))
        textSurface, textRect = events.text_object(button['text'], smallText)
        textRect.center = ((x0+x1)/2,(y0+y1)/2)
        self.screen.blit(textSurface,textRect)

    def countdown(self):
        countdown = ['3','2','1','GO!']
        self.env = Environment()
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
            self.clock.tick(1)
        
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
        passed = font.render("Passed: "+str(self.env.obstacles_passed), True, (255,255,255))
        score = font.render("Score: "+str(self.env.score), True, (255,255,255))
        level = font.render("LEVEL: "+str(self.env.level), True, (255,255,255))
        self.screen.blit(passed, (0,int(50*self.height/600)))
        self.screen.blit(score, (0,int(100*self.height/600)))
        self.screen.blit(level, (0,int(150*self.height/600)))

    def game_page(self):
        ship_horn_sound = pygame.mixer.Sound('soundtrack/BARCO APITANDO.mp3')
        ship_horn_sound.play()
        self.game_loop()

    def game_loop(self):
        x_change = 0
        y_change = 0
        
        self.env.obstacles.clear()
        self.env.player = Elements.Player(self.width*0.45, self.height*0.8)
        self.env.generate_obstacle(self)

        #close button
        while not self.env.bumped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.env.bumped = True

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
                        self.env.obstacle_speed += 2
                    if event.key == pygame.K_b:
                        self.env.obstacle_speed -= 2
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0
            
            self.env.player.x += x_change
            self.env.player.y += y_change

            self.background()

            # position of obstacles
            for obs in self.env.obstacles.values():
                obs.y += self.env.obstacle_speed
                obs.show(self)

            # calling to print player
            self.env.player.show(self)

            # calling score_card function
            self.score_card()

            # Possible events
            self.env.inside_check(self, self.clock)
            self.env.renew_obstacles(self, self.clock)
            self.env.check_collisions(self, self.clock)

            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()
            self.screen_button('pause')


            #updating the game
            pygame.display.update()
            self.clock.tick(20)

        pygame.quit()
        quit()
    
    def paused(self):
        pause_image = pygame.image.load("images/jungle-cruise.jpg")
        pause_image = pygame.transform.scale(pause_image,self.dimensions)
        self.screen.blit(pause_image,(0,0))
        
        self.pause_loop()
    
    def pause_loop(self):
        self.pause = True
        while self.pause:
            for event in pygame.event.get():
                events.quit_event(event)

            # events.event_message(self,'PAUSED')
            font = pygame.font.Font("font/kahlil-font/Kahlil-YzP9L.ttf", int(75*self.height/600))
            dim = font.size("PAUSED")
            title = font.render("PAUSED", True, (255,200,0))
            self.screen.blit(title,(int((self.width-dim[0])/2),int(50*self.height/600)))


            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()
            self.screen_button('continue')
            self.screen_button('restart')
            self.screen_button('menu')

            pygame.display.update()
            self.clock.tick(10)

    def win_page(self):

        self.win_loop()
    
    def win_loop(self):
        self.pause = True
        while self.pause:
            for event in pygame.event.get():
                events.quit_event(event)

            events.event_message(self,'YOU WON!')

            self.mouse = pygame.mouse.get_pos()
            self.click = pygame.mouse.get_pressed()
            self.screen_button('continue')
            self.screen_button('restart')
            self.screen_button('menu')

            pygame.display.update()
            self.clock.tick(10)