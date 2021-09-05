from pygame import Rect
from settings.playerSettings import PlayerSettings
from settings.gameSettings import GameSettings

class Player(Rect):
    def __init__(self):
        super().__init__(PlayerSettings.DEFAULT_X_POS,
                         GameSettings.COMECO_CHAO-PlayerSettings.SIZE,
                         PlayerSettings.SIZE,
                         PlayerSettings.SIZE)
        self.__cor = PlayerSettings.DEFAULT_COLOR
        self.__pulando = False
        self.__agachando = False
        self.__direcao_pulo = 'UP'
        self.__score = 0

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self,cor):
        self.__cor = cor

    @property
    def pulando(self):
        return self.__pulando

    @property
    def agachando(self):
        return self.__agachando

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, novo_score):
        self.__score = novo_score

    def pular(self, vel_pulo):
        self.__pulando = True
        if self.__direcao_pulo == 'UP':
            self.y -= vel_pulo
            if self.y + self.height <= GameSettings.PULO_MAX:
                self.__direcao_pulo = 'DOWN'
        else:
            self.y += vel_pulo
            if self.y + self.height >= GameSettings.COMECO_CHAO:
                self.__direcao_pulo = 'UP'
                self.__pulando = False
        self.__atualizar()

    def agachar(self):
        self.__agachando = True
        self.height -= PlayerSettings.SIZE/2
        self.y += PlayerSettings.SIZE/2
        self.__atualizar()

    def soltar(self):
        self.__agachando = False
        self.height = PlayerSettings.SIZE
        self.y -= PlayerSettings.SIZE/2
        self.__atualizar()
    
    def resetarCor(self):
        self.cor = PlayerSettings.DEFAULT_COLOR

    def resetar(self):
        self.resetarCor()
        self.x = PlayerSettings.DEFAULT_X_POS
        self.y = GameSettings.COMECO_CHAO - PlayerSettings.SIZE
        self.__score = 0
        self.__pulando = False
        self.__agachando = False
        self.__atualizar()

    def __atualizar(self):
        self.update(self)

