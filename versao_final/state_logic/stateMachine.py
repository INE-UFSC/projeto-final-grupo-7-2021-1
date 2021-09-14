from state_logic.gameStates import MenuState, InstructionState, RankingState, SettingsState


class StateMachine:
    def __init__(self):
        self.__map = {'menu':MenuState(),
                      'instrucoes':InstructionState(),
                      'configuracoes':SettingsState(),
                      'ranking':RankingState()}
        self.__currentState = self.__map['menu']

    def run(self, screen, **kwargs):
        next_state = self.__currentState.perform_actions(screen,
                                                        mouse_up=kwargs['mouse_up'])
        self.next_state_logic(next_state)

    def next_state_logic(self, next_state):
        if next_state != None and next_state != self.__currentState.nome:
            self.__currentState = self.__map[next_state]