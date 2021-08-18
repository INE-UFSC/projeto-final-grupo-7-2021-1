import pygame


#configs
BLACK = (0,0,0)
COR_CHAO = (50,150,50)
COR_CEU = (100,100,255)
AMARELO = (255,255,0)


class View:
    def __init__(self, controlador, width, height):
        self.__controlador = controlador
        self.__screen_width = width
        self.__screen_height = height
        self.__window = pygame.display.set_mode((self.__screen_width, self.__screen_height))

    def desenhar(self):
        self.__desenhar_cenario()
        self.__desenhar_player()
        self.__desenhar_obstaculos()

    def __desenhar_player(self):
        pygame.draw.rect(self.__window, self.__controlador.player.cor, self.__controlador.player)

    def __desenhar_cenario(self):
        pygame.draw.rect(self.__window, COR_CEU, self.__controlador.cenario.ceu)
        pygame.draw.rect(self.__window, COR_CHAO, self.__controlador.cenario.chao)

    def __desenhar_obstaculos(self):
        for obs in self.__controlador.cenario.obstaculos:
            pygame.draw.rect(self.__window, AMARELO, obs)


