from abc import ABC, abstractmethod
from pygame import Rect

#Configurações
SIZE = 10
PURPLE = (155,0,155)
WHITE = (255,255,255)

#Class abstrata de poderes

class Power(Rect, ABC):
    @abstractmethod
    def __init__(self, x, y, color, cooldown):
        self.__color = color
        self.__cooldown = cooldown
        super().__init__(x, y- SIZE, SIZE, SIZE)
    
    @property
    def color(self):
        return self.__color
    
    @property
    def cooldown(self):
        return self.__cooldown
    
    def __update(self):
        self.update(self.x, self.y, self.width, self.height)

    @abstractmethod
    def effect(self, game_speed, jump_speed):
        pass