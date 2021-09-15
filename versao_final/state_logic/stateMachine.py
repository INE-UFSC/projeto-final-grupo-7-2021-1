from state_logic.gameStates import *


class StateMachine:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__map = {'menu':MenuState(),
                      'instrucoes':InstructionState(),
                      'configuracoes':SettingsState(),
                      'ranking':RankingState(),
                      'sel_avatar':SelAvatarState(),
                      'sel_bg':SelBgState(),
                      'jogando':PlayingState()}
        self.__currentState = self.__map['menu']

    @property
    def currentState(self):
        return self.__currentState.nome

    def run(self, screen, mouse_up, now):
        next_state = self.__currentState.perform_actions(screen,
                                                         poderes=self.__controlador.cenario.poderes,
                                                         obstaculos=self.__controlador.cenario.obstaculos,
                                                         player_color=self.__controlador.player.cor,
                                                         player_rect=self.__controlador.player,
                                                         score=self.__controlador.get_score(),
                                                         highscore=self.__controlador.highscore,
                                                         final_score=self.__controlador.get_final_score(),
                                                         top_scores=self.__controlador.get_highscores(),
                                                         mouse_up=mouse_up,
                                                         now=now)
        self.next_state_logic(next_state)

    def next_state_logic(self, next_state):
        if next_state != None and next_state != self.__currentState.nome:
            self.__currentState = self.__map[next_state]
