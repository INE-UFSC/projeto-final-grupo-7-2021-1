import pygame, os
from views.baseView import BaseView
from views.buttons import MenuButton
from settings.gameSettings import GameSettings

#variavel auxilar
menu_bg_x = 0

class MenuView(BaseView):
    def __init__(self):
        self.__buttons = [
                         MenuButton('JOGAR', (GameSettings.WIDTH/2, GameSettings.HEIGHT/2 - 120), 'jogando'),
                         MenuButton('INSTRUÇÕES', (GameSettings.WIDTH/2, GameSettings.HEIGHT/2 - 60), 'instrucoes'),
                         MenuButton('CONFIGURAÇÕES', (GameSettings.WIDTH/2, GameSettings.HEIGHT/2), 'configuracoes'),
                         MenuButton('RANKING', (GameSettings.WIDTH/2, GameSettings.HEIGHT/2 + 60), 'ranking')
                        ]
        self.__bg = pygame.transform.scale(pygame.image.load(os.path.join(os.getcwd(),'assets\\backgrounds\\background4.png')),
                                          (GameSettings.WIDTH, GameSettings.HEIGHT))
        super().__init__()

    def display(self, screen, mouse_up):
        global menu_bg_x

        #background infinito
        rel_x = menu_bg_x % self.__bg.get_rect().width
        screen.blit(self.__bg, (rel_x - self.__bg.get_rect().width, 0))
        if rel_x < GameSettings.WIDTH:
            screen.blit(self.__bg, (rel_x, 0))
        menu_bg_x -= 1

        states = []
        for btn in self.__buttons:
            btn.draw(screen)
            btn.hover()
            states.append(btn.click(mouse_up))
        
        return self.button_states_handler('menu',states)
