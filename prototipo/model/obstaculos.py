from abc import ABC, abstractmethod
from pygame import Rect

class Obstaculo(Rect, ABC):
    @abstractmethod
    def __init__(self, x, y, width, height, margem):
        super().__init__(x, y, width, height)
        self.__margem = margem
    
    @property
    def margem(self):
        return self.__margem
    
    """ update Rect após mudança vel """
    def mover(self,vel):
        self.x -= vel
        self.__atualizar()
    
    def __atualizar(self):
        self.update(self)
