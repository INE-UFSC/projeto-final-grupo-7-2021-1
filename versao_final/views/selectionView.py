import os
import pygame
from views.baseView import BaseView
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from abc import ABC, abstractmethod
from views.buttons import DeclineButton, ConfirmButton, LeftArrowButton, RightArrowButton


class SelectionView(BaseView, ABC):
    def __init__(self):
        super().__init__(GameColors.AZUL)
        self.__arrow_buttons = [LeftArrowButton(100, 70, (20, GameSettings.HEIGHT/2)),
                                RightArrowButton(100, 70, (GameSettings.WIDTH - 100 - 30, GameSettings.HEIGHT/2)),]
        self.__buttons = [DeclineButton(90, 90, (GameSettings.WIDTH/2 - 100 - 45, GameSettings.HEIGHT/2 + 150), 'configuracoes'),
                          ConfirmButton(90, 90, (GameSettings.WIDTH/2 + 100 - 45, GameSettings.HEIGHT/2 + 150))]
        self.__pos = 0

    @property
    def pos(self):
        return self.__pos

    @property
    def buttons(self):
        return self.__buttons

    @abstractmethod
    def display(self, screen, mouse_up):
        screen.fill(self.color)

        states = []
        for btn in self.__buttons:
            btn.draw(screen)
            btn.hover()
            states.append(btn.click(mouse_up))
        
        return states

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
