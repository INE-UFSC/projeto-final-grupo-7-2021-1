from abc import ABC, abstractmethod
from pygame import Rect

class Obstacle(ABC,Rect):
    @abstractmethod
    def __init__(self, x, y, width, height, margin):
        super().__init__(x, y, width, height)
        self.__margin = margin
    
    @property
    def margin(self):
        return self.__margin
    
    """ update Rect após mudança vel """
    def move(self,vel):
        self.x -= vel
        self.update(self.x, self.y, self.width, self.height)
