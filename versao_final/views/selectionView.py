import os
import pygame
from abc import ABC, abstractmethod
from views.baseView import BaseView
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from views.buttons import LeftArrowButton, RightArrowButton


GAME_SETTINGS = GameSettings()

class SelectionView(BaseView, ABC):
    def __init__(self):
        super().__init__()
        self.__arrow_buttons = [LeftArrowButton(100, 70, (20, GAME_SETTINGS.HEIGHT/2)),
                                RightArrowButton(100, 70, (GAME_SETTINGS.WIDTH - 100 - 30, GAME_SETTINGS.HEIGHT/2)),]
        self.__pos = 0

    @property
    def pos(self):
        return self.__pos

    @abstractmethod
    def display(self, screen):
        return super().display(screen)

    def manage_arrow_buttons(self, screen, mouse_up, lista):
        if self.__pos == 0:
            self.__arrow_buttons[1].draw(screen)
            self.__arrow_buttons[1].hover()
            self.__pos = self.__arrow_buttons[1].click(self.__pos, mouse_up)
        elif self.__pos == len(lista) - 1:
            self.__arrow_buttons[0].draw(screen)
            self.__arrow_buttons[0].hover()
            self.__pos = self.__arrow_buttons[0].click(self.__pos, mouse_up)
        else:
            for btn in self.__arrow_buttons:
                btn.draw(screen)
                btn.hover()
                self.__pos = btn.click(self.__pos, mouse_up)
