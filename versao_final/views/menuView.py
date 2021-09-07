import os
import pygame
from views.baseView import BaseView
from settings.gameStates import GameStates
from settings.gameSettings import GameSettings
from views.buttons import PlayButton, InstructionButton, SettingsButton, RankingButton


#variavel auxiliar
menu_bg_x = 0

class MenuView(BaseView):
    def display(self, screen, **kwargs):
        global menu_bg_x
        mouse_pos = kwargs['mouse_pos']
        mouse_up = kwargs['mouse_up']

        bg = pygame.transform.scale(pygame.image.load(os.path.join("versao_final\\assets\\backgrounds\\background4.png")),
                                    (GameSettings.WIDTH, GameSettings.HEIGHT))
        
        #background infinito
        rel_x = menu_bg_x % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < GameSettings.WIDTH:
            screen.blit(bg, (rel_x,0))
        menu_bg_x -= 1

        b0 = PlayButton((GameSettings.WIDTH/2, (GameSettings.HEIGHT/2) - 80), GameStates.MENU, GameStates.JOGANDO)
        h0 = b0.hover(mouse_pos)
        s0 = b0.click(mouse_pos, mouse_up)

        b1 = InstructionButton((GameSettings.WIDTH/2, (GameSettings.HEIGHT/2) - 20), GameStates.MENU, GameStates.INSTRUCOES1)
        h1 = b1.hover(mouse_pos)
        s1 = b1.click(mouse_pos, mouse_up)

        b2 = SettingsButton((GameSettings.WIDTH/2, (GameSettings.HEIGHT/2) + 40), GameStates.MENU, GameStates.CONFIGURACOES)
        h2 = b2.hover(mouse_pos)
        s2 = b2.click(mouse_pos, mouse_up)

        b3 = RankingButton((GameSettings.WIDTH/2, (GameSettings.HEIGHT/2) + 100), GameStates.MENU, GameStates.RANKING)
        h3 = b3.hover(mouse_pos)
        s3 = b3.click(mouse_pos, mouse_up)

        self.cursor_handler(h0, h1, h2, h3)
        nextState = self.state_handler(GameStates.MENU, s0, s1, s2, s3)

        screen.blit(b0.image, (b0.rect.x, b0.rect.y))
        screen.blit(b1.image, (b1.rect.x, b1.rect.y))
        screen.blit(b2.image, (b2.rect.x, b2.rect.y))
        screen.blit(b3.image, (b3.rect.x, b3.rect.y))

        return nextState
