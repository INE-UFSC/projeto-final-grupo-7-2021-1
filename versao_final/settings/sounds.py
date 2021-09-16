from pygame.mixer import Sound
import os, pygame

pygame.mixer.init()

PATH = os.path.join(os.getcwd(), 'assets', 'sounds_assets')

class GameMusic(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'music.ogg'))
    self.set_volume(0.3)


class ButtonSfxSound(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'button_sfx.ogg'))
    self.set_volume(0.3)

class GameOverSound(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'game_over.ogg'))
    self.set_volume(0.3)

class JumpSfxSound(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'jump_sfx.ogg'))
    self.set_volume(0.3)

class MenuMusic(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'menu.ogg'))
    self.set_volume(0.3)

