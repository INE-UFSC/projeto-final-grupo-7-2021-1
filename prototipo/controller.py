import pygame
from pygame.constants import *
from view import View
from player import Player
from cenario import Cenario


#configs
WIDTH = 900
HEIGHT = 500
FPS = 60
COMECO_CHAO = 380
PULO_MAX = COMECO_CHAO - 120 #pulo de 120 px

#variaveis auxiliares
vel_pulo = 5

class Controller:
    def __init__(self):
        self.__player = Player(COMECO_CHAO)
        self.__cenario = Cenario(WIDTH, HEIGHT, COMECO_CHAO)
        self.__view = View(self, WIDTH, HEIGHT)
        self.__running = True
        self.__paused = False

    @property
    def player(self):
        return self.__player

    @property
    def cenario(self):
        return self.__cenario

    def mainloop(self):
        clock = pygame.time.Clock()
        while self.__running:
            clock.tick(FPS)

            self.__view.desenhar()
            self.key_handler()
            self.checar_pulando()

            for event in pygame.event.get():
                if event.type == WINDOWCLOSE:
                    self.__running = False

            pygame.display.update()

    def key_handler(self):
        keys = pygame.key.get_pressed()
        if keys[K_w] or keys[K_UP]:
            if not self.__player.pulando:
                self.__player.pular(vel_pulo, PULO_MAX, COMECO_CHAO)

    def checar_pulando(self):
        if self.__player.pulando:
            self.__player.pular(vel_pulo, PULO_MAX, COMECO_CHAO)

