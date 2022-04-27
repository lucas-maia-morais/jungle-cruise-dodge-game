import random
import time
import packages.events as events
import packages.elements as Elements


class Environment:
    def __init__(self):
        self.bumped = False
        self.obstacle_speed = 10
        self.obs = 0
        self.y_change = 0
        self.obstacles_passed = 0
        self.score = 0
        self.level = 0
        self.obstacles = {}
        self.obs_id = -1

    def generate_obstacle(self, s):
        self.obs_id += 1
        obs_type = random.randint(0,3)
        obs = Elements.Obstacle(self.obs_id, obs_type, random.uniform(0.15, 0.75)*s.width, -random.uniform(0, 0.5)*s.width)
        self.obstacles[self.obs_id] = obs
        return obs

    def new_level(self,s):
        self.level += 1
        self.obstacle_speed += self.level
        if self.level % 2:
            self.generate_obstacle(s)

    def destroy_obstacle(self, obs):
        self.obstacles.pop(obs.id)
    
    def inside_check(self,s,clock):
        if self.player.x > (0.85 - self.player.width/2)*s.width or self.player.x < (0.15 + self.player.width/2)*s.width:            
            events.event_message(s,'Encalhou')
            time.sleep(2)
            s.countdown()
    
    def renew_obstacles(self,s,clock):
        to_destroy = []
        new_level = False
        for obs in self.obstacles.values():
            if obs.y > s.height:
                to_destroy.append(obs)
                self.obstacles_passed += 1
                self.score += self.obstacle_speed
                if self.obstacles_passed % 2 == 0:
                    new_level = True

        if new_level:
            self.new_level(s)
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