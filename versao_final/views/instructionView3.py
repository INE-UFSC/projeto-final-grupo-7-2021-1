import os
import pygame
from views.baseView import BaseView
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameStates import GameStates
from settings.gameSettings import GameSettings
from views.buttons import HomeButton, BackwardButton


class InstructionView3(BaseView):
    def display(self, screen, **kwargs):
        mouse_pos = kwargs['mouse_pos']
        mouse_up = kwargs['mouse_up']

        bHome = HomeButton((70, 50), GameStates.INSTRUCOES3)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        b1 = BackwardButton((60, GameSettings.HEIGHT/2), GameStates.INSTRUCOES3, GameStates.INSTRUCOES2)
        h1 = b1.hover(mouse_pos)
        s1 = b1.click(mouse_pos, mouse_up)

        title_text = GameFonts.SEMIBOLD_LARGE.render('PODERES', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        slow_img = pygame.transform.scale(pygame.image.load(os.path.join("versao_final\\assets\\powers\\slow.png")), (42, 106))
        slow_pos = (GameSettings.WIDTH/2 - 200, GameSettings.HEIGHT/2 - 90)

        slow_wrap_text = ["LENTIDÃO: Diminui a velocidade",
                          "do jogo por um breve período de",
                          "tempo. A pontuação continua",
                          "contando normalmente."]

        slow_txt = []
        for text in slow_wrap_text:
            slow_txt.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))

        imortal_img = pygame.transform.scale(pygame.image.load(os.path.join("versao_final\\assets\\powers\\star.png")), (82, 76))
        imortal_pos = (GameSettings.WIDTH/2 - 230, GameSettings.HEIGHT/2 + 120)

        imortal_wrap_text = ["INVENCIBILIDADE: Desativa as",
                             "colisões e aumenta a pontuação",
                             "por um breve período de tempo"]
        
        imortal_txt = []
        for text in imortal_wrap_text:
            imortal_txt.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))

        self.cursor_handler(h0, h1)
        nextState = self.state_handler(GameStates.INSTRUCOES3, s0, s1)

        screen.fill(GameColors.AZUL)
        screen.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        screen.blit(b1.image, (b1.rect.x, b1.rect.y))
        screen.blit(title_text, title_pos)

        screen.blit(slow_img, slow_pos)
        for pos, text_surface in enumerate(slow_txt):
            text_pos = (slow_pos[0] + slow_img.get_rect().width + 15, slow_pos[1] + (pos)*30)
            screen.blit(text_surface, text_pos)

        screen.blit(imortal_img, imortal_pos)
        for pos, text_surface in enumerate(imortal_txt):
            text_pos = (slow_pos[0] + slow_img.get_rect().width + 15, imortal_pos[1] + (pos)*30)
            screen.blit(text_surface, text_pos)

        return nextState
