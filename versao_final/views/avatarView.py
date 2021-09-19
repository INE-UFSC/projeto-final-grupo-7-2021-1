import os
import pygame
from views.selectionView import SelectionView
from settings.gameSettings import GameSettings
from views.buttons import ConfirmButtonAvatar, DeclineButtonAvatar


GAME_SETTINGS = GameSettings()
PATH = os.path.join(os.getcwd(), 'assets', 'characters')
DIRECTORIES = os.listdir(PATH)

class AvatarView(SelectionView):
    def __init__(self):
        super().__init__()

        self.__characters = []
        for rPath in DIRECTORIES:
            self.__characters.append(os.path.join(PATH, rPath))
        
        self.__buttons = [DeclineButtonAvatar(90, 90, (GAME_SETTINGS.WIDTH/2 - 100 - 45, GAME_SETTINGS.HEIGHT/2 + 150), 'configuracoes'),
                          ConfirmButtonAvatar(90, 90, (GAME_SETTINGS.WIDTH/2 + 100 - 45, GAME_SETTINGS.HEIGHT/2 + 150), 'configuracoes')]
        
        self.__avatar_path = None

    def display(self, screen, mouse_up):
        screen.fill(self.color)

        self.__avatar_path = self.__characters[self.pos]
        avatar = pygame.image.load(os.path.join(self.__avatar_path, 'idle.png'))
        size = avatar.get_size()
        avatar_scale = (int(size[0]*0.4), int(size[1]*0.4))
        avatar_img = pygame.transform.scale(avatar, avatar_scale)
        avatar_pos = ((GAME_SETTINGS.WIDTH/2 - avatar_img.get_rect().width/2,
                       GAME_SETTINGS.HEIGHT/2 - avatar_img.get_rect().height/2 - 50))

        self.manage_arrow_buttons(screen, mouse_up, self.__characters)

        states = []
        for btn in self.__buttons:
            btn.draw(screen)
            btn.hover()
            states.append(btn.click(self.__avatar_path, mouse_up))

        screen.blit(avatar_img, avatar_pos)
        
        return self.button_states_handler('sel_avatar',states)
