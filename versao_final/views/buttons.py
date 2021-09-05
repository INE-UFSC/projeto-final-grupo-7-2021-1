from pygame.transform import scale
from settings.gameStates import GameStates
import pygame
from pygame.sprite import Sprite
from abc import ABC, abstractmethod
import os


MENU_BUTTONS_SCALE = (161, 42)
HOME_BUTTON_SCALE = (77, 61)
ARROW_BUTTONS_SCALE = (87, 58)

class HoverButton(Sprite, ABC):
    @abstractmethod
    def __init__(self, center, filename, current_state, next_state, scale):
        hover_scale = (int(scale[0]*1.2), int(scale[1]*1.2))
        self.__images = [pygame.transform.scale(pygame.image.load(os.path.join(filename)), scale),
                         pygame.transform.scale(pygame.image.load(os.path.join(filename)), hover_scale)]
        
        self.__rects = [self.__images[0].get_rect(center=center), self.__images[1].get_rect(center=center)]
        self.__mouse_over = False
        self.__current_state = current_state
        self.__next_state = next_state

    @property
    def image(self):
        return self.__images[1] if self.__mouse_over else self.__images[0]

    @property
    def rect(self):
        return self.__rects[1] if self.__mouse_over else self.__rects[0]

    def hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.__mouse_over = True
        else:
            self.__mouse_over = False
        return self.__mouse_over

    def click(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos) and mouse_up:
            return self.__next_state
        else:
            return self.__current_state
    
class PlayButton(HoverButton):
    def __init__(self, center, current_state, next_state):
        filename = "versao_final\\assets\\buttons\\button_jogar.png"
        scale = MENU_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class InstructionButton(HoverButton):
    def __init__(self, center, current_state, next_state):
        filename = 'versao_final\\assets\\buttons\\button_instrucoes.png'
        scale = MENU_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class SettingsButton(HoverButton):
    def __init__(self, center, current_state, next_state):
        filename = 'versao_final\\assets\\buttons\\button_configuracoes.png'
        scale = MENU_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class RankingButton(HoverButton):
    def __init__(self, center, current_state, next_state):
        filename = 'versao_final\\assets\\buttons\\button_ranking.png'
        scale = MENU_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class FowardButton(HoverButton):
    def __init__(self, center, current_state, next_state):
        filename = 'versao_final\\assets\\buttons\\button_foward.png'
        scale = ARROW_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class BackwardButton(HoverButton):
    def __init__(self, center, current_state, next_state):
        filename = 'versao_final\\assets\\buttons\\button_backward.png'
        scale = ARROW_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class HomeButton(HoverButton):
    def __init__(self, center, current_state):
        filename = 'versao_final\\assets\\buttons\\button_home.png'
        scale = HOME_BUTTON_SCALE
        next_state = GameStates.MENU
        super().__init__(center, filename, current_state, next_state, scale)

class ResetButton(HoverButton):
    def __init__(self, center, current_state):
        filename = "versao_final\\assets\\buttons\\button_reset.png"
        next_state = GameStates.JOGANDO
        scale = HOME_BUTTON_SCALE
        super().__init__(center, filename, current_state, next_state, scale)
