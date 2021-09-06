import os
import pygame
from views.baseView import BaseView
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from settings.gameStates import GameStates
from views.buttons import HomeButton, BackwardButton, FowardButton

class InstructionView2(BaseView):
    def display(self, screen, **kwargs):
        mouse_pos = kwargs['mouse_pos']
        mouse_up = kwargs['mouse_up']

        bHome = HomeButton((70, 50), GameStates.INSTRUCOES2)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        b1 = BackwardButton((60, GameSettings.HEIGHT/2), GameStates.INSTRUCOES2, GameStates.INSTRUCOES1)
        h1 = b1.hover(mouse_pos)
        s1 = b1.click(mouse_pos, mouse_up)

        b2 = FowardButton((GameSettings.WIDTH - 60, GameSettings.HEIGHT/2), GameStates.INSTRUCOES2, GameStates.INSTRUCOES3)
        h2 = b2.hover(mouse_pos)
        s2 = b2.click(mouse_pos, mouse_up)

        title_text = GameFonts.SEMIBOLD_LARGE.render('CONTROLES', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        jump_img = pygame.transform.scale(pygame.image.load(os.path.join("versao_final\\assets\\characters\\ninja_girl\\jump4.png")), (100, 142))
        jump_pos = (GameSettings.WIDTH/2 - 250, GameSettings.HEIGHT/2 - 100)

        jump_txt = GameFonts.REGULAR_SMALL.render('PULAR: Tecla "W" ou seta para cima', False, GameColors.BRANCO)
        jump_txt_pos = (jump_pos[0] + jump_img.get_rect().width + 15, jump_pos[1] + 70)

        slide_img = pygame.transform.scale(pygame.image.load(os.path.join("versao_final\\assets\\characters\\adventurer_boy\\slide2.png")), (99, 100))
        slide_pos = (GameSettings.WIDTH/2 - 250, GameSettings.HEIGHT/2 + 50)

        slide_txt = GameFonts.REGULAR_SMALL.render('DESLIZAR: Tecla "S" ou seta para baixo', False, GameColors.BRANCO)
        slide_txt_pos = (slide_pos[0] + slide_img.get_rect().width + 15, slide_pos[1] + 70)

        self.cursor_handler(h0, h1, h2)
        nextState = self.state_handler(GameStates.INSTRUCOES2, s0, s1, s2)

        screen.fill(GameColors.AZUL)
        screen.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        screen.blit(b1.image, (b1.rect.x, b1.rect.y))
        screen.blit(b2.image, (b2.rect.x, b2.rect.y))
        screen.blit(title_text, title_pos)
        screen.blit(jump_img, jump_pos)
        screen.blit(jump_txt, jump_txt_pos)
        screen.blit(slide_img, slide_pos)
        screen.blit(slide_txt, slide_txt_pos)

        return nextState
