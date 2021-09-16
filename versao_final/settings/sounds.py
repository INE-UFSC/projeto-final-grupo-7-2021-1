from pygame.mixer import Sound
import os, pygame

pygame.mixer.init()

PATH = os.path.join(os.getcwd(), 'assets', 'sounds_assets')

class GameMusic(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'music.mp3'))


class ButtonSfxSound(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'music.mp3'))

class GameOverSound(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'game_over.mp3'))

class JumpSfxSound(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'jump_sfx.mp3'),)

class MenuMusic(Sound):
  def __init__(self):
    super().__init__(os.path.join(PATH,'menu.mp3'),)

