import pygame
from abc import ABC, abstractmethod

class BaseView(ABC):
    def __init__(self, color=None):
        self.__color = color

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
