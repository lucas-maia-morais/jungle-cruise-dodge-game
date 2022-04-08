import pygame
import packages.aux as aux

class Elements:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.width = 0.10
        self.height = 0.15
        # self.img = img

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self,x):
        self._x = x
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self,y):
        self._y = y

    
class Player(Elements):
    def player():
        return True

    def show(self,s):
        # image appearing
        boat = pygame.transform.scale(aux.boat, (s.width*0.1, s.height*0.15))
        s.screen.blit(boat,(self.x,self.y))

class Obstacle(Elements):
    def player():
        return False

    def show(self,s):
        # image appearing
        cruise = pygame.transform.rotate(aux.cruise, -90)
        cruise = pygame.transform.scale(cruise, (s.width*0.1, s.height*0.15))
        s.screen.blit(cruise,(self.x,self.y))
