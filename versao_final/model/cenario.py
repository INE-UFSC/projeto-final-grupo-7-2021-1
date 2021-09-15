from model.gerador import Gerador
from settings.gameSettings import GameSettings


GAME_SETTINGS = GameSettings()

#variavel auxiliar
tempo_ultimo_poder = 0

class Cenario:
    def __init__(self):
        self.__gerador = Gerador()
        self.__obstaculos = []
        self.__poderes = []

    @property
    def obstaculos(self):
        return self.__obstaculos

    @property
    def poderes(self):
        return self.__poderes

    #por criterios de legibilidade
    def gerar_elementos(self, now):
        self.__gerarObs(now)
        self.__gerarPoder(now)

    def __gerarObs(self, now):
        global tempo_ultimo_poder
        try:
            ultimo_obs = self.__obstaculos[-1]
            if ultimo_obs.x + ultimo_obs.width < GAME_SETTINGS.WIDTH - ultimo_obs.margem:
                obs = self.__gerador.gerarObs()
                self.__obstaculos.append(obs)
        except IndexError:
            obs = self.__gerador.gerarObs()
            self.__obstaculos.append(obs)
            tempo_ultimo_poder = now    #se chegou até aqui significa que o jogo acabou de começar
                                        #então faz-se o setup do tempo relativo de geração

    def __gerarPoder(self, now):
        global tempo_ultimo_poder
        if now - tempo_ultimo_poder > GAME_SETTINGS.TEMPO_GERA_PODER:
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
            if poder.rect.x + poder.rect.width < 0:
                self.__poderes.remove(poder)

    def removePoder(self, poder):
        self.poderes.remove(poder)
        
    def limpar(self):
        self.__obstaculos.clear()
        self.__poderes.clear()