import pygame
from pygame.constants import *
from view import View


#configs
WIDTH = 900
HEIGHT = 500
FPS = 60

class Controller:
    def __init__(self):
        self.__player = None
        self.__cenario = None
        self.__view = View(self, WIDTH, HEIGHT)
        self.__running = True
        self.__paused = False

    def mainloop(self):
        clock = pygame.time.Clock()
        while self.__running:
            clock.tick(FPS)

            self.__view.draw()

            for event in pygame.event.get():
                if event.type == WINDOWCLOSE:
                    self.__running = False

            pygame.display.update()

