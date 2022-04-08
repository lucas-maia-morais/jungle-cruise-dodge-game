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