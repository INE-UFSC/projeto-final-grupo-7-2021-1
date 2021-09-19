import random
from model.skyObs import ObsVoa
from settings.gameSettings import GameSettings
from model.groundObs import ObsPequeno, ObsGrande
from model.powers import PoderLento, PoderInvulnerabilidade


GAME_SETTINGS = GameSettings()
PODERES = (PoderLento, PoderInvulnerabilidade)
OBSTACULOS = (ObsVoa, ObsPequeno, ObsGrande)

class Gerador:
    '''Responsável por gerar obstaculos e poderes.'''
    def gerarPoder(self):
        poder_escolhido = random.choice(PODERES)
        poder = poder_escolhido(GAME_SETTINGS.WIDTH, GAME_SETTINGS.COMECO_CHAO)
        return poder

    def gerarObs(self):
        obs_escolhido = random.choice(OBSTACULOS)
        margin = random.randrange(600,800,10)
        if obs_escolhido == ObsVoa:
            y = random.randrange(GAME_SETTINGS.COMECO_CHAO-130, GAME_SETTINGS.COMECO_CHAO-100)
            obs = obs_escolhido(GAME_SETTINGS.WIDTH, y, margin)
            return obs
        else:
            obs = obs_escolhido(GAME_SETTINGS.WIDTH, GAME_SETTINGS.COMECO_CHAO, margin)
            return obs