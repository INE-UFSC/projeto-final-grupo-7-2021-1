import pygame
from Canvas import *
import os
import random

class Engine:
    def __init__(self, Player, canvas:Canvas) -> None:
        self.__player = Player
        self.__Tela = canvas
        self.__isPlaying = True
        self.__isPaused = False
    
    def gerar_obstaculos(self):
        pass

    def gerar_poderes(self):
        pass
    
    def gameLoop(self):

        """ seta configuração de tela no objeto Tela com width/height da classe canvas """
        self.__Tela.iniciarTela
        
        """ Configuração básica pygame """
        while self.__isPlaying:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__isPlaying = False
        pygame.quit()
        
        
""" Iniciando o Game """
engine = Engine('Player',Canvas(500,500))
engine.gameLoop()