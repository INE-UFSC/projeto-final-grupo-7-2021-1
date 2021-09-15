import pygame, os
from views.baseView import BaseView
from views.buttons import MenuButton
from settings.gameSettings import GameSettings


GAME_SETTINGS = GameSettings()

#variavel auxilar
menu_bg_x = 0

class MenuView(BaseView):
    def __init__(self):
        self.__buttons = [
                         MenuButton('JOGAR', (GAME_SETTINGS.WIDTH/2 - 100, GAME_SETTINGS.HEIGHT/2 - 120), 'jogando'),
                         MenuButton('INSTRUÇÕES', (GAME_SETTINGS.WIDTH/2 - 100, GAME_SETTINGS.HEIGHT/2 - 60), 'instrucoes'),
                         MenuButton('CONFIGURAÇÕES', (GAME_SETTINGS.WIDTH/2 - 100, GAME_SETTINGS.HEIGHT/2), 'configuracoes'),
                         MenuButton('RANKING', (GAME_SETTINGS.WIDTH/2 - 100, GAME_SETTINGS.HEIGHT/2 + 60), 'ranking')
                        ]
        self.__bg = None
        super().__init__()

    def display(self, screen, mouse_up):
        global menu_bg_x

        self.__bg = pygame.transform.scale(pygame.image.load(os.path.join(GAME_SETTINGS.background)),
                                          (GAME_SETTINGS.WIDTH, GAME_SETTINGS.HEIGHT))
        #background infinito
        rel_x = menu_bg_x % self.__bg.get_rect().width
        screen.blit(self.__bg, (rel_x - self.__bg.get_rect().width, 0))
        if rel_x < GAME_SETTINGS.WIDTH:
            screen.blit(self.__bg, (rel_x, 0))
        menu_bg_x -= 1

        states = []
        for btn in self.__buttons:
            btn.draw(screen)
            btn.hover()
            states.append(btn.click(mouse_up))
        
        return self.button_states_handler('menu',states)
