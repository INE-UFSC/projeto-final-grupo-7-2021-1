import pygame
import os
import random

class Canvas:
    def __init__(self,width,height):
        """ Tamanho da Tela """
        self.__width = width
        self.__height = height
    
    @property
    def iniciarTela(self):
        pygame.display.set_mode((self.__width,self.__height))

    @property
    def desenhar_canvas(self):
        pass
