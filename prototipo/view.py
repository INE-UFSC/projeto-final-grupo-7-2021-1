import pygame


#configs
BLACK = (0,0,0)


class View:
    def __init__(self, controlador, width, height):
        self.__controlador = controlador
        self.__screen_width = width
        self.__screen_height = height
        self.__window = pygame.display.set_mode((self.__screen_width, self.__screen_height))

    def draw(self):
        self.__window.fill(BLACK)


