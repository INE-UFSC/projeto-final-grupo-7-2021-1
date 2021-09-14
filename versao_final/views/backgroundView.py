import os
import pygame
from views.selectionView import SelectionView
from settings.gameSettings import GameSettings

PATH = os.path.join(os.getcwd(), 'assets','backgrounds')

class BackgroundView(SelectionView):
    def __init__(self):
        super().__init__()
        self.__backgrounds = []
        for rPath in os.listdir(PATH):
            self.__backgrounds.append(os.path.join(PATH, rPath))

    def display(self, screen, mouse_up):
        states = super().display(screen, mouse_up)

        bg_img = pygame.transform.scale(pygame.image.load(self.__backgrounds[self.pos]), (576,324))
        bg_pos = (GameSettings.WIDTH/2 - bg_img.get_rect().width/2,
                  GameSettings.HEIGHT/2 - bg_img.get_rect().height/2 - 50)
        
        self.manage_arrow_buttons(screen, mouse_up, self.__backgrounds)

        screen.blit(bg_img, bg_pos)

        return self.button_states_handler('self_bg',states)
        