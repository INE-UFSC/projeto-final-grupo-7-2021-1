from gerador import Gerador
from pygame import Rect


#configs
TEMPO_GERA_PODER = 20000

#variavel auxiliar
tempo_ultimo_poder = 0

#Duas classes auxiliares só pra diferenciar o cenário
class Chao(Rect):
    def __init__(self, width, height, chao):
        super().__init__(0, chao, width, height)

class Ceu(Rect):
    def __init__(self, width, heigth):
        super().__init__(0, 0, width, heigth)

class Cenario:
    def __init__(self, width, height, chao):
        self.__screen_width = width
        self.__screen_height = height
        self.__comeco_chao = chao
        self.__ceu = Ceu(self.__screen_width, self.__screen_height)
        self.__chao = Chao(self.__screen_width, self.__screen_height, self.__comeco_chao)
        self.__gerador = Gerador()
        self.__obstaculos = []
        self.__poderes = []

    @property
    def ceu(self):
        return self.__ceu

    @property
    def chao(self):
        return self.__chao

    @property
    def obstaculos(self):
        return self.__obstaculos

    @property
    def poderes(self):
        return self.__poderes

    #por criterios de legibilidade
    def gerar_elementos(self, now):
        self.__gerarObs()
        self.__gerarPoder(now)

    def __gerarObs(self):
        if len(self.__obstaculos) == 0:
            obs = self.__gerador.gerarObs(self.__screen_width, self.__comeco_chao)
            self.__obstaculos.append(obs)
        else:
            ultimo_obs = self.__obstaculos[-1]
            if ultimo_obs.x + ultimo_obs.width < self.__screen_width - ultimo_obs.margem:
                obs = self.__gerador.gerarObs(self.__screen_width, self.__comeco_chao)
                self.__obstaculos.append(obs)

    def __gerarPoder(self, now):
        global tempo_ultimo_poder
        if now - tempo_ultimo_poder > TEMPO_GERA_PODER:
            tempo_ultimo_poder = now
            poder = self.__gerador.gerarPoder(self.__screen_width, self.__comeco_chao)
            self.__poderes.append(poder)

    #por criterios de legibilidade
    def mover_elementos(self, vel_jogo):
        self.__moverObs(vel_jogo)
        self.__moverPoderes(vel_jogo)

    def __moverObs(self, vel):
        for obs in self.__obstaculos[:]:
            obs.mover(vel)
            if obs.x < 0:
                self.__obstaculos.remove(obs)

    def __moverPoderes(self, vel):
        for poder in self.__poderes[:]:
            poder.mover(vel)
            if poder.x < 0:
                self.__poderes.remove(poder)

    def removePoder(self, poder):
        self.poderes.remove(poder)
        
