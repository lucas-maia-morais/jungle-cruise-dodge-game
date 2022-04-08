import pygame

class Screen:
    def __init__(self, width=800, height=600):
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