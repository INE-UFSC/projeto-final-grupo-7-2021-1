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
        self.__fps = 50
    
    def gerar_obstaculos(self):
        pass

    def gerar_poderes(self):
        pass
    
    @property
    def tela(self):
        return self.__Tela
    
    
    
    def gameLoop(self):

        """ controle o FPS """
        pygame.time.Clock().tick(self.__fps)

        """ seta configuração de tela no objeto Tela com width/height da classe canvas """
        self.tela.iniciarTela
        
        """ Configuração básica pygame """
        while self.__isPlaying:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__isPlaying = False
            
            """ Desenhando na Tela """
            """ Passar objetos --> para dentro da função desenhar da Tela ?? """

            self.tela.desenhar_canvas([""" lista de objetos que devem ser desenhados, polimorfismo com a função desenho talvez???"""])

        pygame.quit()
        
        
""" Iniciando o Game """
engine = Engine('Player',Canvas(500,500))
engine.gameLoop()