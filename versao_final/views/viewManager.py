import pygame
from settings.gameStates import GameStates
from settings.gameSettings import GameSettings
from views.menuView import MenuView
from views.gameView import GameView
from views.pauseView import PauseView
from views.endgameView import EndgameView
from views.rankingView import RankingView
from views.settingsView import SettingsView
from views.instructionView import InstructionView
from views.avatarView import AvatarView
from views.backgroundView import BackgroundView


class ViewManager:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = pygame.display.set_mode((GameSettings.WIDTH, GameSettings.HEIGHT))
        self.__views = [MenuView(),
                        GameView(),
                        PauseView(),
                        EndgameView(),
                        InstructionView(),
                        SettingsView(),
                        AvatarView(),
                        BackgroundView(),
                        RankingView()]

    def display(self, mouse_pos, mouse_up):
        nextState = None
        currentView = self.__views[self.__controlador.gameState.value]
        poderes = self.__controlador.cenario.poderes
        obstaculos = self.__controlador.cenario.obstaculos
        player_color = self.__controlador.player.cor
        player_rect = self.__controlador.player
        score = self.__controlador.get_score()
        highscore = self.__controlador.highscore
        final_score = self.__controlador.get_final_score()
        top_scores = self.__controlador.get_highscores()
        nextState = currentView.display(self.__window,
                                        poderes=poderes,
                                        obstaculos=obstaculos,
                                        player_color=player_color,
                                        player_rect=player_rect,
                                        score=score,
                                        highscore=highscore,
                                        final_score=final_score,
                                        top_scores=top_scores,
                                        mouse_pos=mouse_pos,
                                        mouse_up=mouse_up)
        return nextState
