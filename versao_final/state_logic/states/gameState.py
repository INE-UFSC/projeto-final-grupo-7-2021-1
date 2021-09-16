import pygame
from pygame.constants import K_ESCAPE
from views.gameView import GameView
from state_logic.states.state import State
from settings.soundSettings import SoundSettings;


SOUND_SETTINGS = SoundSettings()

class GameState(State):
    def __init__(self):
        super().__init__(GameView(), 'jogando')


    def perform_actions(self, screen, **kwargs):
        score = kwargs['score']
        highscore = kwargs['highscore']
        poderes = kwargs['poderes']
        obstaculos = kwargs['obstaculos']
        player_rect = kwargs['player_rect']
        player_image = kwargs['player_image']
        self.view.display(screen, score, highscore, poderes, obstaculos, player_rect, player_image)

        keydown = kwargs['keydown']
        next_state = self.key_handler(keydown)

        return next_state

    def key_handler(self, keydown):
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE] and keydown:
            return 'pausado'
