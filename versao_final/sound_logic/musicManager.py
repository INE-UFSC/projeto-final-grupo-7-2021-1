from settings.singleton import Singleton
from sound_logic.sounds import GameMusic, MenuMusic


class MusicManager(Singleton):
    def __init__(self):
        self.__menu_music = MenuMusic()
        self.__game_music = GameMusic()

    @property
    def menu_music(self):
        return self.__menu_music

    @property
    def game_music(self):
        return self.__game_music

    def music_on(self):
        self.__menu_music.set_volume(0.3)
        self.__game_music.set_volume(0.3)

    def music_off(self):
        self.__menu_music.set_volume(0)
        self.__game_music.set_volume(0)