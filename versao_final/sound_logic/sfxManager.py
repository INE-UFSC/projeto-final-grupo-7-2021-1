from settings.singleton import Singleton
from sound_logic.sounds import JumpSfx, ButtonSfx, GameOverSfx


class SFXManager(Singleton):
    def __init__(self):
        self.__button_sfx = ButtonSfx()
        self.__jump_sfx = JumpSfx()
        self.__game_over_sfx = GameOverSfx()

    @property
    def button_sfx(self):
        return self.__button_sfx

    @property
    def jump_sfx(self):
        return self.__jump_sfx

    @property
    def game_over_sfx(self):
        return self.__game_over_sfx

    def sfx_on(self):
        self.__button_sfx.set_volume(0.5)
        self.__jump_sfx.set_volume(0.5)
        self.__game_over_sfx.set_volume(0.5)

    def sfx_off(self):
        self.__button_sfx.set_volume(0)
        self.__jump_sfx.set_volume(0)
        self.__game_over_sfx.set_volume(0)
