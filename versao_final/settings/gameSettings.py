import os
from settings.singleton import Singleton

class GameSettings(Singleton):
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 500
        self.FPS = 60
        self.COMECO_CHAO = 455
        self.PULO_MAX = self.COMECO_CHAO - 120 #pulo de 120 px
        self.TEMPO_PAUSE = 500 #esc deve ficar pressionado por 500 ms para entrar na tela de pause
        self.TEMPO_ACRES_SCORE = 100 #a cada 100 ms o score aumenta 1
        self.TEMPO_GERA_PODER = 20000
        self.__background = os.path.join(os.getcwd(), 'assets', 'backgrounds', 'background1.png')

    @property
    def background(self):
        return self.__background

    def set_bg(self, new_bg):
        self.__background = new_bg
