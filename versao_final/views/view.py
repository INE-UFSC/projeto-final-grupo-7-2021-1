import pygame
from settings.gameFonts import GameFonts
from settings.gameStates import GameStates
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from views.menuView import MenuView
from views.gameView import GameView
from views.instructionView1 import InstructionView1
from views.instructionView2 import InstructionView2
from views.instructionView3 import InstructionView3
from views.rankingView import RankingView
from views.settingsView import SettingsView
from views.endgameView import EndgameView
from views.pauseView import PauseView


class ViewManager:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = pygame.display.set_mode((GameSettings.WIDTH, GameSettings.HEIGHT))
        self.__views = [MenuView(),
                        GameView(),
                        PauseView(),
                        EndgameView(),
                        InstructionView1(),
                        InstructionView2(),
                        InstructionView3(),
                        SettingsView(),
                        None,
                        None,
                        RankingView()]

    def display(self, mouse_pos, mouse_up):
        nextState = None
        currentView = self.__views[self.__controlador.gameState.value]
        if self.__controlador.gameState == GameStates.JOGANDO:
            poderes = self.__controlador.cenario.poderes
            obstaculos = self.__controlador.cenario.obstaculos
            player_color = self.__controlador.player.cor
            player_rect = self.__controlador.player
            score = self.__controlador.get_score()
            highscore = self.__controlador.highscore
            currentView.display(self.__window,
                                poderes=poderes,
                                obstaculos=obstaculos,
                                player_color=player_color,
                                player_rect=player_rect,
                                score=score,
                                highscore=highscore)
            nextState = GameStates.JOGANDO
        elif self.__controlador.gameState == GameStates.ENDGAME:
            final_score = self.__controlador.get_final_score()
            nextState = currentView.display(self.__window,
                                            mouse_pos=mouse_pos,
                                            mouse_up=mouse_up,
                                            final_score=final_score)
        elif self.__controlador.gameState == GameStates.RANKING:
            top_scores = self.__controlador.get_highscores()
            nextState = currentView.display(self.__window,
                                            mouse_pos=mouse_pos,
                                            mouse_up=mouse_up,
                                            top_scores=top_scores)
        else:
            nextState = currentView.display(self.__window, mouse_pos=mouse_pos, mouse_up=mouse_up)
        return nextState

