import pygame
from pygame.constants import K_ESCAPE
from views.gameView import GameView
from state_logic.states.state import State
from sound_logic.musicManager import MusicManager


MUSIC_MANAGER = MusicManager()

class GameState(State):
    def __init__(self):
        super().__init__(GameView(), 'jogando')


    def perform_actions(self, screen, **kwargs):
        MUSIC_MANAGER.menu_music.stop_sound()
        MUSIC_MANAGER.game_music.play_sound()
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
