from pygame.transform import scale
from settings.gameStates import GameStates
import pygame
from pygame.sprite import Sprite
from abc import ABC, abstractmethod
import os


MEDIUM_BUTTONS_SCALE = (161, 42)
LARGE_BUTTONS_SCALE = (224, 42)
SQUARE_BUTTON_SCALE = (77, 61)
ARROW_BUTTONS_SCALE = (87, 58)

class HoverButton(Sprite, ABC):
    def __init__(self, center, filename, scale):
        hover_scale = (int(scale[0]*1.2), int(scale[1]*1.2))
        self.__images = [pygame.transform.scale(pygame.image.load(os.path.join(filename)), scale),
                         pygame.transform.scale(pygame.image.load(os.path.join(filename)), hover_scale)]
        
        self.__rects = [self.__images[0].get_rect(center=center), self.__images[1].get_rect(center=center)]
        self.__mouse_over = False

    @property
    def image(self):
        return self.__images[1] if self.__mouse_over else self.__images[0]

    @property
    def images(self):
        return self.__images

    @property
    def rect(self):
        return self.__rects[1] if self.__mouse_over else self.__rects[0]

    @property
    def mouse_over(self):
        return self.__mouse_over

    def hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.__mouse_over = True
        else:
            self.__mouse_over = False
        return self.__mouse_over

    @abstractmethod
    def click(self, mouse_pos, mouse_up):
        raise NotImplementedError
    
class StateButton(HoverButton, ABC):
    @abstractmethod
    def __init__(self, center, filename, current_state, next_state, scale):
        self.__current_state = current_state
        self.__next_state = next_state
        super().__init__(center, filename, scale)

    def click(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos) and mouse_up:
            return self.__next_state
        else:
            return self.__current_state

class ConfigButton(HoverButton, ABC):
    @abstractmethod
    def __init__(self, center, filename1, filename2, scale):
        super().__init__(center, filename1, scale)
        hover_scale = (int(scale[0]*1.2), int(scale[1]*1.2))
        self.__images_off = [pygame.transform.scale(pygame.image.load(os.path.join(filename2)), scale),
                             pygame.transform.scale(pygame.image.load(os.path.join(filename2)), hover_scale)]
        self.__on = True
    
    @property
    def image(self):
        if self.__on:
            return self.images[1] if self.mouse_over else self.images[0]
        else:
            return self.__images_off[1] if self.mouse_over else self.__images_off[0]

    def click(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos) and mouse_up:
            if self.__on:
                self.__on = False
            else:
                self.__on = True

class PlayButton(StateButton):
    def __init__(self, center, current_state, next_state):
        filename = "versao_final\\assets\\buttons\\button_jogar.png"
        scale = MEDIUM_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class InstructionButton(StateButton):
    def __init__(self, center, current_state, next_state):
        filename = 'versao_final\\assets\\buttons\\button_instrucoes.png'
        scale = MEDIUM_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class SettingsButton(StateButton):
    def __init__(self, center, current_state, next_state):
        filename = 'versao_final\\assets\\buttons\\button_configuracoes.png'
        scale = MEDIUM_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class RankingButton(StateButton):
    def __init__(self, center, current_state, next_state):
        filename = 'versao_final\\assets\\buttons\\button_ranking.png'
        scale = MEDIUM_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class FowardButton(StateButton):
    def __init__(self, center, current_state, next_state):
        filename = 'versao_final\\assets\\buttons\\button_foward.png'
        scale = ARROW_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class BackwardButton(StateButton):
    def __init__(self, center, current_state, next_state):
        filename = 'versao_final\\assets\\buttons\\button_backward.png'
        scale = ARROW_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class HomeButton(StateButton):
    def __init__(self, center, current_state):
        filename = 'versao_final\\assets\\buttons\\button_home.png'
        scale = SQUARE_BUTTON_SCALE
        next_state = GameStates.MENU
        super().__init__(center, filename, current_state, next_state, scale)

class ResetButton(StateButton):
    def __init__(self, center, current_state):
        filename = "versao_final\\assets\\buttons\\button_reset.png"
        next_state = GameStates.JOGANDO
        scale = SQUARE_BUTTON_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class AvatarButton(StateButton):
    def __init__(self, center):
        filename = "versao_final\\assets\\buttons\\button_character.png"
        current_state = GameStates.CONFIGURACOES
        next_state = GameStates.SEL_AVATAR
        scale = LARGE_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class BackgroundButton(StateButton):
    def __init__(self, center):
        filename = "versao_final\\assets\\buttons\\button_cenario.png"
        current_state = GameStates.CONFIGURACOES
        next_state = GameStates.SEL_BG
        scale = LARGE_BUTTONS_SCALE
        super().__init__(center, filename, current_state, next_state, scale)

class SFXButton(ConfigButton):
    def __init__(self, center):
       filename1 = "versao_final\\assets\\buttons\\button_sfx_on.png"
       filename2 = "versao_final\\assets\\buttons\\button_sfx_off.png"
       scale = MEDIUM_BUTTONS_SCALE
       super().__init__(center, filename1, filename2, scale)

class MusicButton(ConfigButton):
    def __init__(self, center):
        filename1 = "versao_final\\assets\\buttons\\button_music_on.png"
        filename2 = "versao_final\\assets\\buttons\\button_music_off.png"
        scale = MEDIUM_BUTTONS_SCALE
        super().__init__(center, filename1, filename2, scale)

class FowardButtonIncrease(HoverButton):
    def __init__(self, center):
        filename = 'versao_final\\assets\\buttons\\button_foward.png'
        scale = ARROW_BUTTONS_SCALE
        super().__init__(center, filename, scale)

    def click(self, mouse_pos, mouse_up, pos):
        if self.rect.collidepoint(mouse_pos) and mouse_up:
            return (pos+1)
        else:
            return pos

class BackwardButtonDecrease(HoverButton):
    def __init__(self, center):
        filename = 'versao_final\\assets\\buttons\\button_backward.png'
        scale = ARROW_BUTTONS_SCALE
        super().__init__(center, filename, scale)

    def click(self, mouse_pos, mouse_up, pos):
        if self.rect.collidepoint(mouse_pos):
            return (pos - 1)
        else:
            return pos

class ButtonConfirm(StateButton):
    def __init__(self, center, current_state):
        filename = "versao_final\\assets\\buttons\\button_check.png"
        scale = SQUARE_BUTTON_SCALE
        next_state = GameStates.CONFIGURACOES
        super().__init__(center, filename, current_state, next_state, scale)

class ButtonDecline(StateButton):
    def __init__(self, center, current_state):
        filename = "versao_final\\assets\\buttons\\button_decline.png"
        scale = SQUARE_BUTTON_SCALE
        next_state = GameStates.CONFIGURACOES
        super().__init__(center, filename, current_state, next_state, scale)
