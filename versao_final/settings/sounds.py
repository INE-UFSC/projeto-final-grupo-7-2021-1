from pygame.mixer import Sound
import os, pygame

pygame.mixer.init()

PATH = os.path.join(os.getcwd(), 'assets', 'sounds_assets')

class GameMusic(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'music.ogg'))


class ButtonSfxSound(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'button_sfx.ogg'))

class GameOverSound(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'game_over.ogg'))

class JumpSfxSound(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'jump_sfx.ogg'),)

class MenuMusic(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'menu.ogg'),)

