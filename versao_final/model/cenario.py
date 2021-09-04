from model.gerador import Gerador
from pygame import Rect
from versao_final.settings.gameSettings import GameSettings

#variavel auxiliar
tempo_ultimo_poder = 0

#Duas classes auxiliares só pra diferenciar o cenário
class Chao(Rect):
    def __init__(self):
        super().__init__(0, GameSettings.COMECO_CHAO, GameSettings.WIDTH, GameSettings.HEIGHT)

class Ceu(Rect):
    def __init__(self):
        super().__init__(0, 0,GameSettings.WIDTH, GameSettings.HEIGHT)

class Cenario:
    def __init__(self):
        self.__ceu = Ceu()
        self.__chao = Chao()
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
        try:
            ultimo_obs = self.__obstaculos[-1]
            if ultimo_obs.x + ultimo_obs.width < GameSettings.WIDTH - ultimo_obs.margem:
                obs = self.__gerador.gerarObs()
                self.__obstaculos.append(obs)
        except IndexError:
            obs = self.__gerador.gerarObs()
            self.__obstaculos.append(obs)

    def __gerarPoder(self, now):
        global tempo_ultimo_poder
        if now - tempo_ultimo_poder > GameSettings.TEMPO_GERA_PODER:
            tempo_ultimo_poder = now
            poder = self.__gerador.gerarPoder()
            self.__poderes.append(poder)

    #por criterios de legibilidade
    def mover_elementos(self, vel_jogo):
        self.__moverObs(vel_jogo)
        self.__moverPoderes(vel_jogo)

    def __moverObs(self, vel):
        for obs in self.__obstaculos[:]:
            obs.mover(vel)
            if obs.x + obs.width < 0:
                self.__obstaculos.remove(obs)

    def __moverPoderes(self, vel):
        for poder in self.__poderes[:]:
            poder.mover(vel)
            if poder.x + poder.width < 0:
                self.__poderes.remove(poder)

    def removePoder(self, poder):
        self.poderes.remove(poder)
        
    def limpar(self, now):
        global tempo_ultimo_poder
        tempo_ultimo_poder = now
        self.__obstaculos.clear()
        self.__poderes.clear()