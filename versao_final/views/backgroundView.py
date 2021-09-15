import os
import pygame
from views.selectionView import SelectionView
from settings.gameSettings import GameSettings
from views.buttons import DeclineButtonBg, ConfirmButtonBg


GAME_SETTINGS = GameSettings()
PATH = os.path.join(os.getcwd(), 'assets','backgrounds')

class BackgroundView(SelectionView):
    def __init__(self):
        super().__init__()
        self.__backgrounds = []

        for rPath in os.listdir(PATH):
            self.__backgrounds.append(os.path.join(PATH, rPath))
        self.__bg_path = None

        self.__buttons = [DeclineButtonBg(90, 90, (GAME_SETTINGS.WIDTH/2 - 100 - 45, GAME_SETTINGS.HEIGHT/2 + 150), 'configuracoes'),
                          ConfirmButtonBg(90, 90, (GAME_SETTINGS.WIDTH/2 + 100 - 45, GAME_SETTINGS.HEIGHT/2 + 150), 'configuracoes')]


    def display(self, screen, mouse_up):
        screen.fill(self.color)
        self.__bg_path = self.__backgrounds[self.pos]
        bg_img = pygame.transform.scale(pygame.image.load(self.__bg_path), (576,324))
        bg_pos = (GAME_SETTINGS.WIDTH/2 - bg_img.get_rect().width/2,
                  GAME_SETTINGS.HEIGHT/2 - bg_img.get_rect().height/2 - 50)

        self.manage_arrow_buttons(screen, mouse_up, self.__backgrounds)

        states = []
        for btn in self.__buttons:
            btn.draw(screen)
            btn.hover()
            states.append(btn.click(self.__bg_path, mouse_up))

        screen.blit(bg_img, bg_pos)

        return self.button_states_handler('self_bg',states)
        