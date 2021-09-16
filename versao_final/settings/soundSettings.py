from settings.singleton import Singleton
from settings.sounds import GameMusic, GameOverSound, MenuMusic, ButtonSfxSound, JumpSfxSound


class SoundSettings(Singleton):
  def __init__(self):
    self.__button_sfx = ButtonSfxSound()
    self.__game_over = GameOverSound()
    self.__jump_sfx = JumpSfxSound()
    self.__menu_music = MenuMusic()
    self.__game_music = GameMusic()
  

  @property
  def button_sfx(self):
    return self.__button_sfx
  
  @property
  def game_over(self):
    return self.__game_over
  
  @property
  def jump_sfx(self):
    return self.__jump_sfx

  @property
  def menu_music(self):
    return self.__menu_music
  
  @property
  def game_music(self):
    return self.__game_music

  def music_on(self):
    self.__game_music.set_volume(1)
    self.__menu_music.set_volume(1)


  def music_off(self):
    self.__game_music.set_volume(0)
    self.__menu_music.set_volume(0)

  def sfx_on(self):
    self.__button_sfx.set_volume(1)
    self.__jump_sfx.set_volume(1)
    self.__game_over.set_volume(1)

  def sfx_off(self):
    self.__button_sfx.set_volume(0)
    self.__jump_sfx.set_volume(0)
    self.__game_over.set_volume(0)

  def music_volume(self):
    return self.__game_music.get_volume()

  def sfx_volume(self):
    return self.__button_sfx.get_volume()
