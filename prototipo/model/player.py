from pygame import Rect


#configs
TAMANHO = 40 #quadrado
X_POS = 300
VERMELHO = (255,0,0)

class Player(Rect):
    def __init__(self, comeco_chao):
        super().__init__(X_POS, comeco_chao-TAMANHO, TAMANHO, TAMANHO)
        self.__cor = VERMELHO
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

    def pular(self, vel_pulo, pulo_max, chao):
        self.__pulando = True
        if self.__direcao_pulo == 'UP':
            self.y -= vel_pulo
            if self.y + self.height <= pulo_max:
                self.__direcao_pulo = 'DOWN'
        else:
            self.y += vel_pulo
            if self.y + self.height >= chao:
                self.__direcao_pulo = 'UP'
                self.__pulando = False
        self.__atualizar()

    def agachar(self):
        self.__agachando = True
        self.height -= TAMANHO/2
        self.y += TAMANHO/2
        self.__atualizar()

    def soltar(self):
        self.__agachando = False
        self.height = TAMANHO
        self.y -= TAMANHO/2
        self.__atualizar()
    
    def resetarCor(self):
        self.cor = VERMELHO

    def resetar(self, comeco_chao):
        self.resetarCor()
        self.x = X_POS
        self.y = comeco_chao-TAMANHO
        self.__score = 0
        self.__pulando = False
        self.__agachando = False
        self.__atualizar()

    def __atualizar(self):
        self.update(self)

