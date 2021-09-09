import os
import pygame
from views.baseView import BaseView
from settings.gameFonts import GameFonts
from settings.gameStates import GameStates
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from views.buttons import ButtonDecline, ButtonConfirm
from views.buttons import BackwardButtonDecrease, FowardButtonIncrease


class BackgroundView(BaseView):
    def __init__(self):
        self.__pos = 0
        source = os.path.join(os.getcwd(),'assets', 'backgrounds')
        backgrounds_path = os.listdir(source)
        self.__backgrounds = []
        for bg in backgrounds_path:
            self.__backgrounds.append(source + bg)

    def display(self, screen, **kwargs):
        mouse_pos = kwargs['mouse_pos']
        mouse_up = kwargs['mouse_up']

        b0 = BackwardButtonDecrease((60, GameSettings.HEIGHT/2))
        h0 = b0.hover(mouse_pos)
        self.__pos = b0.click(mouse_pos, mouse_up, self.__pos)

        b1 = FowardButtonIncrease((GameSettings.WIDTH - 60, GameSettings.HEIGHT/2))
        h1 = b1.hover(mouse_pos)
        self.__pos = b1.click(mouse_pos, mouse_up, self.__pos)

        self.__pos_handler()

        b2 = ButtonDecline((GameSettings.WIDTH/2 - 100, GameSettings.HEIGHT/2 + 150), GameStates.SEL_BG)
        h2 = b2.hover(mouse_pos)
        s2 = b2.click(mouse_pos, mouse_up)

        b3 = ButtonConfirm((GameSettings.WIDTH/2 + 100, GameSettings.HEIGHT/2 + 150), GameStates.SEL_BG)
        h3 = b3.hover(mouse_pos)
        s3 = b3.click(mouse_pos, mouse_up)

        title_text = GameFonts.SEMIBOLD_LARGE.render('SELECIONE UM CENÁRIO', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        filename = self.__backgrounds[self.__pos]
        bg = pygame.image.load(os.path.join(filename))
        size = bg.get_size()
        bg_scale = (int(size[0]*0.3), int(size[1]*0.3))
        bg_img = pygame.transform.scale(bg, bg_scale)
        bg_pos = ((GameSettings.WIDTH/2 - bg_img.get_rect().width/2,
                   GameSettings.HEIGHT/2 - bg_img.get_rect().height/2 - 50))
        
        self.cursor_handler(h0, h1, h2, h3)
        nextState = self.state_handler(GameStates.SEL_BG, s2, s3)

        screen.fill(GameColors.AZUL)
        screen.blit(b0.image, (b0.rect.x, b0.rect.y))
        screen.blit(b1.image, (b1.rect.x, b1.rect.y))
        screen.blit(b2.image, (b2.rect.x, b2.rect.y))
        screen.blit(b3.image, (b3.rect.x, b3.rect.y))
        screen.blit(bg_img, bg_pos)

        return nextState
        
    def __pos_handler(self):
        if self.__pos > len(self.__backgrounds) - 1:
            self.__pos = 0
        elif self.__pos < 0:
            self.__pos = len(self.__backgrounds) - 1
