import random
from model.bird import Passaro
from settings.gameSettings import GameSettings
from model.groundObs import ObsPequeno, ObsGrande
from model.powers import PoderLento, PoderInvulnerabilidade


GAME_SETTINGS = GameSettings()
PODERES = (PoderLento, PoderInvulnerabilidade)
OBSTACULOS = (Passaro, ObsPequeno, ObsGrande)

class Gerador:
    '''Responsável por gerar obstaculos e poderes.'''
    def gerarPoder(self):
        poder_escolhido = random.choice(PODERES)
        poder = poder_escolhido(GAME_SETTINGS.WIDTH, GAME_SETTINGS.COMECO_CHAO)
        return poder

    def gerarObs(self):
        obs_escolhido = random.choice(OBSTACULOS)
        margin = random.randrange(600,800,10)
        if obs_escolhido == Passaro:
            y = random.randrange(GAME_SETTINGS.COMECO_CHAO-50, GAME_SETTINGS.COMECO_CHAO-30)
            obs = obs_escolhido(GAME_SETTINGS.WIDTH, y, margin)
            return obs
        else:
            obs = obs_escolhido(GAME_SETTINGS.WIDTH, GAME_SETTINGS.COMECO_CHAO, margin)
            return obs