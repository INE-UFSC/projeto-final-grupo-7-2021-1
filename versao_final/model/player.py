import pygame
import os
from pygame.sprite import Sprite
from settings.gameSettings import GameSettings
from settings.playerSettings import PlayerSettings


GAME_SETTINGS = GameSettings()
PLAYER_SETTINGS = PlayerSettings()
#variável auxiliar animação
temporizador_animacao = 0

class Player(Sprite):
    def __init__(self):
        self.__pulando = False
        self.__agachando = False
        self.__direcao_pulo = 'UP'
        self.__score = 0
        self.__images = []
        self.__scale = PLAYER_SETTINGS.RUN_SCALE
        for image in PLAYER_SETTINGS.run_images:
            img = pygame.transform.scale(pygame.image.load(os.path.join(PLAYER_SETTINGS.path,'run',image)), self.__scale)
            self.__images.append(img)

        self.image = None
        self.rect = None
        self.__posImgs = 0


    @property
    def pulando(self):
        return self.__pulando

    @property
    def agachando(self):
        return self.__agachando

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, novo_score):
        self.__score = novo_score

    def pular(self, vel_pulo):
        self.__pulando = True
        self.__images = PLAYER_SETTINGS.jump_images
        self.__scale = PLAYER_SETTINGS.JUMP_SCALE

        if self.__direcao_pulo == 'UP':
            self.rect.y -= vel_pulo
            if self.rect.y + self.rect.height <= GAME_SETTINGS.PULO_MAX:
                self.__direcao_pulo = 'DOWN'
        else:
            self.rect.y += vel_pulo
            if self.rect.y + self.rect.height >= GAME_SETTINGS.COMECO_CHAO:
                self.__direcao_pulo = 'UP'
                self.__pulando = False
                self.__images = PLAYER_SETTINGS.run_images
                self.__scale = PLAYER_SETTINGS.RUN_SCALE

    def agachar(self):
        self.__agachando = True
        self.__images = PLAYER_SETTINGS.slide_images
        self.__scale = PLAYER_SETTINGS.SLIDE_SCALE


    def soltar(self):
        self.__agachando = False
        self.__images = PLAYER_SETTINGS.run_images
        self.__scale = PLAYER_SETTINGS.RUN_SCALE


    def resetar(self):
        self.__score = 0
        self.__pulando = False
        self.__agachando = False

    # função animação player
    def animaPlayer(self, now):
        global temporizador_animacao
        if now - temporizador_animacao >=  PLAYER_SETTINGS.ANIMACAOTEMPO:
            temporizador_animacao = now
            #self.image = pygame.transform.scale(pygame.image.load(os.path.join(PLAYER_SETTINGS.path,'run',self.__images[self.__posImgs])), self.__scale)
            self.image = self.__images[self.__posImgs]
            self.rect = self.image.get_rect()
            self.rect.x = PLAYER_SETTINGS.DEFAULT_X_POS
            self.rect.y = GAME_SETTINGS.COMECO_CHAO - self.__scale[1]


            if self.__posImgs >= len(self.__images) -1:
                self.__posImgs = 0
            else:
                self.__posImgs += 1


