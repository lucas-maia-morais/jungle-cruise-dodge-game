import pygame
import random
import time
import packages.aux as aux
import packages.events as events
import packages.elements as Elements


class Environment:
    def __init__(self):
        self.__bumped = False
        self.__obstacle_speed = 10
        self.obs = 0
        self.y_change = 0
        self.__obstacles_passed = 0
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
    def obstacles_passed(self):
        return self.__obstacles_passed

    @obstacles_passed.setter
    def obstacles_passed(self, obstacles_passed):
        self.__obstacles_passed = obstacles_passed

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
            events.event_message(s,'Encalhou')
            time.sleep(2)
            s.countdown()
    
    def renew_obstacles(self,s,clock):
        to_destroy = []
        for obs in self.obstacles.values():
            if obs.y > s.height:
                to_destroy.append(obs)
                self.obstacles_passed += 1
                self.score = self.obstacles_passed * 10
                if int(self.obstacles_passed) % 10 == 0:
                    self.level += 1
                    self.obstacle_speed += 2
                    events.event_message(s,"Level "+str(self.level))
                    time.sleep(3)

        for obs in to_destroy: 
            self.destroy_obstacle(obs)
            self.generate_obstacle(s)
    
    def check_collisions(self,s,clock):
        for obs in self.obstacles.values():
            if ((self.player.y < obs.y + 0.15*s.height) and (self.player.y + 0.15*s.height > obs.y)):
                    if (self.player.x < obs.x + 0.1*s.width) and (self.player.x + 0.1*s.width > obs.x):
                        events.event_message(s,'Naufragado')
                        time.sleep(5)
                        s.countdown()