import os
import pygame
from abc import ABC, abstractmethod
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from settings.playerSettings import PlayerSettings
from settings.soundSettings import SoundSettings


PLAYER_SETTINGS = PlayerSettings()
GAME_SETTINGS = GameSettings()
SOUND_SETTINGS = SoundSettings()
PATH = os.path.join(os.getcwd(),'assets','buttons')

class Button(ABC):
    def __init__(self, width, height, pos, next_state=None, elevation=6):
        self.__top_rect = pygame.Rect((pos),(width, height))
        self.__top_color = GameColors.AMARELO

        self.__hover_color = GameColors.ROXO
        self.__display_color = self.__top_color

        self.__elevation = elevation
        self.__dynamic_elevation = elevation
        self.__default_y_pos = pos[1]

        self.__bottom_rect = pygame.Rect(pos, (width, height))
        self.__bottom_color = GameColors.AMARELO_ESCURO

        self.__next_state = next_state

    @property
    def top_rect(self):
        return self.__top_rect

    @property
    def elevation(self):
        return self.__elevation

    @property
    def dynamic_elevation(self):
        return self.__dynamic_elevation

    @dynamic_elevation.setter
    def dynamic_elevation(self, new_value):
        self.__dynamic_elevation = new_value

    @property
    def next_state(self):
        return self.__next_state

    @abstractmethod
    def draw(self, screen):
        self.__top_rect.y = self.__default_y_pos - self.__dynamic_elevation

        self.__bottom_rect.midtop = self.__top_rect.midtop
        self.__bottom_rect.height = self.__top_rect.height + self.__dynamic_elevation

        pygame.draw.rect(screen, self.__bottom_color, self.__bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.__display_color, self.__top_rect, border_radius=12)

    def hover(self):
        if self.__top_rect.collidepoint(pygame.mouse.get_pos()):
            self.__display_color = self.__hover_color
        else:
            self.__display_color =  self.__top_color

    @abstractmethod
    def click(self):
        raise NotImplementedError

class TextButton(Button):
    def __init__(self, text, width, height, pos, next_state=None, elevation=6):
        super().__init__(width, height, pos, next_state, elevation)
        self.__text = GameFonts.SEMIBOLD_SMALL.render(text, True, GameColors.BRANCO)
        self.__text_rect = self.__text.get_rect(center=self.top_rect.center)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, textValue):
        self.__text = textValue

    def draw(self, screen):
        super().draw(screen)
        self.__text_rect.center = self.top_rect.center
        screen.blit(self.__text, self.__text_rect)

    def click(self, mouse_up):
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
            if mouse_up:
                return self.next_state
        else:
            self.dynamic_elevation = self.elevation

class ImageButton(Button):
    def __init__(self, width, height, pos, filename, scale, next_state=None, elevation=6):
        super().__init__(width, height, pos, next_state, elevation)
        self.__image = pygame.transform.scale(pygame.image.load(os.path.join(PATH, filename)), scale)
        self.__image_rect = self.__image.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        super().draw(screen)
        self.__image_rect.center = self.top_rect.center
        screen.blit(self.__image, self.__image_rect)

    def click(self, mouse_up):
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
            if mouse_up:
                return self.next_state
        else:
            self.dynamic_elevation = self.elevation

class MenuButton(TextButton):
    def __init__(self, text, pos, next_state):
        width = 200
        height = 40
        super().__init__(text, width, height, pos, next_state=next_state)

class HomeButton(ImageButton):
    def __init__(self, width, height, pos, next_state='menu', elevation=6):
        filename = 'home.png'
        scale = (60, 60)
        super().__init__(width, height, pos, filename, scale, next_state, elevation)

class LeftArrowButton(ImageButton):
    def __init__(self, width, height, pos, next_state=None, elevation=6):
        filename = 'arrow_left.png'
        scale = (60, 60)
        super().__init__(width, height, pos, filename, scale, next_state, elevation)

    def click(self, pos, mouse_up):
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
            if mouse_up:
                return pos - 1
        else:
            self.dynamic_elevation = self.elevation
        return pos

class RightArrowButton(ImageButton):
    def __init__(self, width, height, pos, next_state=None, elevation=6):
        filename = 'arrow_right.png'
        scale = (60, 60)
        super().__init__(width, height, pos, filename, scale, next_state, elevation)

    def click(self, pos, mouse_up):
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
            if mouse_up:
                return pos + 1
        else:
            self.dynamic_elevation = self.elevation
        return pos

class RestartButton(ImageButton):
    def __init__(self, width, height, pos, next_state='jogando', elevation=6):
        filename = 'replay.png'
        scale = (60, 60)
        super().__init__(width, height, pos, filename, scale, next_state, elevation)

class ConfirmButtonBg(ImageButton):
    def __init__(self, width, height, pos, next_state=None, elevation=6):
        filename = 'confirm.png'
        scale = (60, 60)
        super().__init__(width, height, pos, filename, scale, next_state, elevation)

    def click(self, filepath, mouse_up):
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
            if mouse_up:
                GAME_SETTINGS.set_bg(filepath)
                return self.next_state
        else:
            self.dynamic_elevation = self.elevation

class DeclineButtonBg(ImageButton):
    def __init__(self, width, height, pos, next_state=None, elevation=6):
        filename = 'decline.png'
        scale = (60, 60)
        super().__init__(width, height, pos, filename, scale, next_state, elevation)

    def click(self, filepath, mouse_up):
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
            if mouse_up:
                return self.next_state
        else:
            self.dynamic_elevation = self.elevation

class ConfirmButtonAvatar(ImageButton):
    def __init__(self, width, height, pos, next_state=None, elevation=6):
        filename = 'confirm.png'
        scale = (60, 60)
        super().__init__(width, height, pos, filename, scale, next_state, elevation)

    def click(self, filepath, mouse_up):
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
            if mouse_up:
                PLAYER_SETTINGS.set_new_avatar(filepath)
                return self.next_state
        else:
            self.dynamic_elevation = self.elevation

class DeclineButtonAvatar(ImageButton):
    def __init__(self, width, height, pos, next_state=None, elevation=6):
        filename = 'decline.png'
        scale = (60, 60)
        super().__init__(width, height, pos, filename, scale, next_state, elevation)

    def click(self, filepath, mouse_up):
        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
            if mouse_up:
                return self.next_state
        else:
            self.dynamic_elevation = self.elevation

class MusicButton(TextButton):
    def __init__(self, width, height, pos, next_state = None, elevation = 6):
        self.__state = 'on'
        text = 'Musica: ' + self.__state
        super().__init__(text, width, height, pos, next_state, elevation)

    
    def click(self, mouse_up):

        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
            if mouse_up:
                self.__action()
                return self.next_state
        else:
            self.dynamic_elevation = self.elevation

    def __action(self):
        if self.__state == 'ON':
            self.__state = 'OFF'
            SOUND_SETTINGS.music_off()
            self.text = GameFonts.SEMIBOLD_SMALL.render('Musica: ' + self.__state, True, GameColors.BRANCO)

        else:
            self.__state = 'ON'
            SOUND_SETTINGS.music_on()
            self.text = GameFonts.SEMIBOLD_SMALL.render('Musica: ' + self.__state, True, GameColors.BRANCO)   

class SfxButton(TextButton):
    def __init__(self, width, height, pos, next_state = None, elevation = 6):
        self.__state = 'ON'
        text = 'SFX: ' + self.__state
        super().__init__(text, width, height, pos, next_state, elevation)

    
    def click(self, mouse_up):

        if self.top_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
            else:
                self.dynamic_elevation = self.elevation
            if mouse_up:
                self.__action()
                return self.next_state
        else:
            self.dynamic_elevation = self.elevation

    def __action(self):
        if self.__state == 'ON':
            self.__state = 'OFF'
            SOUND_SETTINGS.sfx_off()
            self.text = GameFonts.SEMIBOLD_SMALL.render('SFX: ' + self.__state, True, GameColors.BRANCO)

        else:
            self.__state = 'ON'
            SOUND_SETTINGS.sfx_on()
            self.text = GameFonts.SEMIBOLD_SMALL.render('SFX: ' + self.__state, True, GameColors.BRANCO)   
