import pygame
from pygame.constants import K_ESCAPE
from state_logic.states.state import State
from views.pauseView import PauseView


class PauseState(State):
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
