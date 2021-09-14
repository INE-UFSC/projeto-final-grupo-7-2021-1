import os
import pygame
from views.selectionView import SelectionView
from settings.gameSettings import GameSettings

PATH = os.path.join(os.getcwd(), 'assets', 'characters')
DIRECTORIES = os.listdir(PATH)

class AvatarView(SelectionView):
    def __init__(self):
        super().__init__()
        self.__characters = []
        for rPath in DIRECTORIES:
            self.__characters.append(os.path.join(PATH, rPath, 'idle.png'))

    def display(self, screen, mouse_up):
        states = super().display(screen, mouse_up)

        avatar = pygame.image.load(self.__characters[self.pos])
        size = avatar.get_size()
        avatar_scale = (int(size[0]*0.4), int(size[1]*0.4))
        avatar_img = pygame.transform.scale(avatar, avatar_scale)
        avatar_pos = ((GameSettings.WIDTH/2 - avatar_img.get_rect().width/2,
                       GameSettings.HEIGHT/2 - avatar_img.get_rect().height/2 - 50))

        self.manage_arrow_buttons(screen, mouse_up, self.__characters)

        screen.blit(avatar_img, avatar_pos)
        
        return self.button_states_handler('sel_avatar',states)
