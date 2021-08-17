from pygame import Rect


#configs
TAMANHO = 40 #quadrado
X_POS = 300
RED = (255,0,0)

class Player(Rect):
    def __init__(self, comeco_chao):
        super().__init__(X_POS, comeco_chao-TAMANHO, TAMANHO, TAMANHO)
        self.__cor = RED
        self.__pulando = False
        self.__agachando = False
        self.__direcao_pulo = 'UP'
        self.__score = 0

    @property
    def cor(self):
        return self.__cor

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

    def pular(self):
        pass

    def agachar(self):
        pass

    def __update(self):
        self.update(self.x, self.y, self.width, self.height)

