import os
import pygame
from pygame.sprite import Sprite
from abc import ABC, abstractmethod


TAMANHO = 10
SLOW = (34, 55)
STAR = (47, 45) 

#Class abstrata de poderes

class Poder(Sprite,ABC):
    @abstractmethod
    def __init__(self, x, y, tempo, filename, scale):
        self.__tempo = tempo
        self.image = pygame.transform.scale(pygame.image.load(os.path.join('assets','powers',filename)), scale)
        self.rect = self.image.get_rect(center = (x,y))
        
        
    
    # Tempo que o poder permanece ativado
    @property
    def tempo(self):
        return self.__tempo

    def mover(self, vel):
        self.rect.x -= vel + 2
        self.__atualizar()

    # Atualiza o Rect 
    def __atualizar(self):
        self.update(self)

    #Efeito gerado pelo poder
    @abstractmethod
    def efeito(self, game_speed, jump_speed):
        #error caso não seja implementado
        raise NotImplementedError

class PoderLento(Poder):
    def __init__(self, x, y):
        filename = 'slow.png'
        y -= SLOW[1]
        super().__init__(x, y, 5000, filename,SLOW)

    
    def efeito(self, velocidadeJogo, velocidadePulo):
        return True, 2, 2 


class PoderInvulnerabilidade(Poder):
    def __init__(self, x, y):
        filename = 'star.png'
        y -= STAR[1]
        super().__init__(x, y, 4000, filename, STAR)
    
    def efeito(self, velocidadeJogo, velocidadePulo):
        return False, velocidadeJogo + 20 , velocidadePulo
