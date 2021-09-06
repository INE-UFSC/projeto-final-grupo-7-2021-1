import pygame
from abc import ABC, abstractmethod

class BaseView(ABC):
    @abstractmethod
    def display(self, screen, **kwargs):
        raise NotImplementedError

    def cursor_handler(self, *args):
        for btn in args:
            if btn:
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                break
            else:
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def state_handler(self, currentState, *args):
        for state in args:
            if state != currentState:
                return state
        return currentState
