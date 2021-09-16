import pygame
from pygame.constants import K_ESCAPE
from views.menuView import MenuView
from views.gameView import GameView
from state_logic.state import State
from views.avatarView import AvatarView
from views.endgameView import EndgameView
from views.rankingView import RankingView
from views.settingsView import SettingsView
from views.backgroundView import BackgroundView
from views.instructionView import InstructionView
from views.pauseView import PauseView
from settings.gameSettings import GameSettings


GAME_SETTINGS = GameSettings()


class MenuState(State):
    def __init__(self):
        super().__init__(MenuView(), 'menu')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)

class InstructionState(State):
    def __init__(self):
        super().__init__(InstructionView(), 'instrucoes')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)

class SettingsState(State):
    def __init__(self):
        super().__init__(SettingsView(), 'configuracoes')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)

class RankingState(State):
    def __init__(self):
        super().__init__(RankingView(), 'ranking')
    
    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        top_scores = kwargs['top_scores']
        return self.view.display(screen, mouse_up, top_scores)

class SelAvatarState(State):
    def __init__(self):
        super().__init__(AvatarView(), 'sel_avatar')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)

class SelBgState(State):
    def __init__(self):
        super().__init__(BackgroundView(), 'sel_bg')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)

class PlayingState(State):
    def __init__(self):
        super().__init__(GameView(), 'jogando')
        self.__pause_tempo = 0

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

class EndgameState(State):
    def __init__(self):
        super().__init__(EndgameView(), 'endgame')

    def perform_actions(self, screen, **kwargs):
        final_score = kwargs['final_score']
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, final_score, mouse_up)

class PausedState(State):
    def __init__(self):
        super().__init__(PauseView(), 'pausado')
        self.__pause_tempo = 1000

    def perform_actions(self, screen, **kwargs):
        keydown = kwargs['keydown']
        mouse_up = kwargs['mouse_up']
        next_state0 = self.key_handler(keydown)
        next_state1 = self.view.display(screen, mouse_up)
        if next_state0 != None:
            return next_state0
        else:
            return next_state1

    def key_handler(self, keydown):
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE] and keydown:
            return 'jogando'
