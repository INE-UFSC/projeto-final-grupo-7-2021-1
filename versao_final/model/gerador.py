import random
from model.bird import Passaro
from model.groundObs import ObsPequeno, ObsGrande
from model.powers import PoderLento, PoderInvulnerabilidade

PODERES = (PoderLento, PoderInvulnerabilidade)
OBSTACULOS = (Passaro, ObsPequeno, ObsGrande)

class Gerador:
    '''Responsável por gerar obstaculos e poderes.'''
    def gerarPoder(self, width, comeco_chao):
        poder_escolhido = random.choice(PODERES)
        poder = poder_escolhido(width, comeco_chao)
        return poder

    def gerarObs(self, width, comeco_chao):
        obs_escolhido = random.choice(OBSTACULOS)
        margin = random.randrange(600,800,10)
        if obs_escolhido == Passaro:
            y = random.randrange(comeco_chao-50, comeco_chao-30)
            obs = obs_escolhido(width, y, margin)
            return obs
        else:
            obs = obs_escolhido(width, comeco_chao, margin)
            return obs