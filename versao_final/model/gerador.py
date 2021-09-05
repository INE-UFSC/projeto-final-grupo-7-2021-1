import random
from model.bird import Passaro
from model.groundObs import ObsPequeno, ObsGrande
from model.powers import PoderLento, PoderInvulnerabilidade
from settings.gameSettings import GameSettings


PODERES = (PoderLento, PoderInvulnerabilidade)
OBSTACULOS = (Passaro, ObsPequeno, ObsGrande)

class Gerador:
    '''Responsável por gerar obstaculos e poderes.'''
    def gerarPoder(self):
        poder_escolhido = random.choice(PODERES)
        poder = poder_escolhido(GameSettings.WIDTH, GameSettings.COMECO_CHAO)
        return poder

    def gerarObs(self):
        obs_escolhido = random.choice(OBSTACULOS)
        margin = random.randrange(600,800,10)
        if obs_escolhido == Passaro:
            y = random.randrange(GameSettings.COMECO_CHAO-50, GameSettings.COMECO_CHAO-30)
            obs = obs_escolhido(GameSettings.WIDTH, y, margin)
            return obs
        else:
            obs = obs_escolhido(GameSettings.WIDTH, GameSettings.COMECO_CHAO, margin)
            return obs