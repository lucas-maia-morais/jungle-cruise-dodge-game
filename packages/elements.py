import pygame
import packages.aux as aux

class Elements:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0.10
        self.height = 0.15
    
class Player(Elements):
    def player():
        return True

    def show(self,s):
        # image appearing
        boat = pygame.transform.scale(aux.boat, (s.width*0.1, s.height*0.15))
        s.screen.blit(boat,(self.x,self.y))

class Obstacle(Elements):
    def __init__(self, id, obs_type, x, y):
        self.id = id
        self.obs_type = obs_type
        super().__init__(x, y)

    def player():
        return False

    def show(self,s):
        # image appearing
        if self.obs_type == 0:
            cruise = pygame.transform.rotate(aux.cruise, -90)
            cruise = pygame.transform.scale(cruise, (s.width*0.1, s.height*0.15))
            s.screen.blit(cruise,(self.x,self.y))
        elif self.obs_type == 1:
            stone = pygame.transform.scale(aux.stone, (s.width*0.1, s.height*0.15))
            s.screen.blit(stone,(self.x,self.y))
        elif self.obs_type == 2:
            pirate = pygame.transform.rotate(aux.pirate, -180)
            pirate = pygame.transform.scale(pirate, (s.width*0.1, s.height*0.15))
            s.screen.blit(pirate,(self.x,self.y))
        elif self.obs_type == 3:
            aligator = pygame.transform.rotate(aux.aligator, -180)
            aligator = pygame.transform.scale(aligator, (s.width*0.1, s.height*0.15))
            s.screen.blit(aligator,(self.x,self.y))