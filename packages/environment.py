import pygame
import packages.aux as aux
import packages.pages as pages


class Environment:
    def __init__(self):
        self.__bumped = False
        self.__obstacle_speed = 10
        self.obs = 0
        self.y_change = 0
        self.__car_passed = 0
        self.__score = 0
        self.__level = 0

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
        textSurface, textRect = aux.text_object(button['text'], smallText)
        textRect.center = ((x0+x1)/2,(y0+y1)/2)
        s.screen.blit(textSurface,textRect)

    def intro_loop(self,s,clock):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            self._mouse = pygame.mouse.get_pos()
            self._click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            self.screen_button(s, clock, 'start')
            self.screen_button(s, clock, 'instruction')
            self.screen_button(s, clock, 'quit')

            pygame.display.update()