import os, pygame
from pygame.mixer import Sound
from abc import ABC, abstractmethod


pygame.mixer.init()

PATH = os.path.join(os.getcwd(), 'assets', 'sounds_assets')

class BaseMusic(Sound, ABC):
    @abstractmethod
    def __init__(self, path):
        super().__init__(os.path.join(PATH,path))
        self.set_volume(0.3)
        self.__tocando = False

    def play_sound(self):
        if not self.__tocando:
            self.play(-1)
            self.__tocando = True

    def stop_sound(self):
        if self.__tocando:
            self.stop()
            self.__tocando = False

class GameMusic(BaseMusic):
  def __init__(self):
    super().__init__('music.ogg')

class MenuMusic(BaseMusic):
  def __init__(self):
    super().__init__('menu.ogg')


class ButtonSfx(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'button_sfx.ogg'))
    self.set_volume(0.5)

class GameOverSfx(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'game_over.ogg'))
    self.set_volume(0.5)

class JumpSfx(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'jump_sfx.ogg'))
    self.set_volume(0.5)
