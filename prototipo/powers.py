from abc import ABC, abstractmethod
from pygame import Rect

#Configurações
TAMANHO = 10
ROXO = (155,0,155)
BRANCO = (255,255,255)

#Class abstrata de poderes

class Poderes(Rect, ABC):
    @abstractmethod
    def __init__(self, x, y, cor, recarga):
        self.__cor = cor
        self.__recarga = recarga
        super().__init__(x, y- TAMANHO, TAMANHO, TAMANHO)
    
    @property
    def cor(self):
        return self.__cor
    
    @property
    def recarga(self):
        return self.__recarga
    
    def __atualizar(self):
        self.atualizar(self.x, self.y, self.width, self.height)

    @abstractmethod
    def effect(self, game_speed, jump_speed):
        pass


