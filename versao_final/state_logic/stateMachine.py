from state_logic.states.menuState import MenuState
from state_logic.states.instructionState import InstructionState
from state_logic.states.endgameState import EndgameState
from state_logic.states.rankingState import RankingState
from state_logic.states.settingsState import SettingsState
from state_logic.states.gameState import GameState
from state_logic.states.selBgState import SelBgState
from state_logic.states.selAvatarState import SelAvatarState
from state_logic.states.pauseState import PauseState


class StateMachine:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__map = {'menu':MenuState(),
                      'instrucoes':InstructionState(),
                      'configuracoes':SettingsState(),
                      'ranking':RankingState(),
                      'sel_avatar':SelAvatarState(),
                      'sel_bg':SelBgState(),
                      'jogando':GameState(),
                      'endgame':EndgameState(),
                      'pausado':PauseState()}

        self.__currentState = self.__map['menu']
        

    @property
    def currentState(self):
        return self.__currentState.nome

    def run(self, screen, mouse_up, keydown, colidiu):
        next_state = self.__currentState.perform_actions(screen,
                                                         poderes=self.__controlador.cenario.poderes,
                                                         obstaculos=self.__controlador.cenario.obstaculos,
                                                         player_image=self.__controlador.player.image,
                                                         player_rect=self.__controlador.player.rect,
                                                         score=self.__controlador.get_score(),
                                                         highscore=self.__controlador.highscore,
                                                         final_score=self.__controlador.get_final_score(),
                                                         top_scores=self.__controlador.get_highscores(),
                                                         mouse_up=mouse_up,
                                                         keydown=keydown)
        self.next_state_logic(next_state, colidiu)

    def next_state_logic(self, next_state, colidiu):
        if colidiu:
            self.__currentState = self.__map['endgame']
        elif next_state != None and next_state != self.__currentState.nome:
            self.__currentState = self.__map[next_state]
