import pygame
import os
import random

class Engine:
    def __init__(self, Player, Canvas) -> None:
        self.__player = Player
        self.__Tela = Canvas
        self.__isPlaying = False
        self.__isPaused = False
    
    def gerar_obstaculos(self):
        pass

    def gerar_poderes(self):
        pass