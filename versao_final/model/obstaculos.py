from abc import ABC, abstractmethod
from pygame.sprite import Sprite
import os, pygame
from settings.gameSettings import GameSettings

GAME_SETTINGS = GameSettings()

class Obstaculo( Sprite, ABC):
    @abstractmethod
    def __init__(self, x, y, margem, filename, scale):
        super().__init__()
        self.__margem = margem
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(GAME_SETTINGS.obstacle_path, filename)), scale)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.height
        self.mask = pygame.mask.from_surface(self.image)

    @property
    def margem(self):
        return self.__margem
    
    def mover(self,vel):
        self.rect.x -= vel

