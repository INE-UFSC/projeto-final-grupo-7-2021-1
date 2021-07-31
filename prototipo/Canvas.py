import pygame
import os
import random

class Canvas:
    def __init__(self,width,height):
        """ Tamanho da Tela """
        self.__width = width
        self.__height = height
        self.__display = pygame.display.set_mode((self.__width,self.__height))

    
    @property
    def display(self):
      return self.__display
    
    @property
    def iniciarTela(self):
      self.display

    def desenhar_canvas(self,objetos_desenhar:list):
      """ fundo  """
      self.display.fill((155,255,165))
      "Desenhar objetos aqui..."




      """ Update da tela <-- final da função ---> """
      pygame.display.update()
        
