from abc import ABC, abstractmethod
from settings.gameColors import GameColors

class BaseView(ABC):
    def __init__(self, color = GameColors.AZUL):
        self.__color = color #cor default do jogo

    @property
    def color(self):
        return self.__color

    @abstractmethod
    def display(self, screen):
        raise NotImplementedError

    def button_states_handler(self, current_state, states):
        nextState = None
        for s in states:
            if s != current_state and s != None:
                nextState = s
        return nextState
