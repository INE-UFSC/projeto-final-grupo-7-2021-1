import os
import pygame
from views.baseView import BaseView
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameStates import GameStates
from settings.gameSettings import GameSettings
from views.buttons import HomeButton, FowardButtonIncrease, BackwardButtonDecrease

AVATAR_PATH = os.path.join(os.getcwd(),'assets','characters')
POWERS_PATH = os.path.join(os.getcwd(),'assets','powers')

class InstructionView(BaseView):
    def __init__(self):
        self.__pos = 0

    def display(self, screen, **kwargs):
        mouse_pos = kwargs['mouse_pos']
        mouse_up = kwargs['mouse_up']
        displays = [self.__display1, self.__display2, self.__display3]
        currentDisplay = displays[self.__pos]
        nextState = currentDisplay(screen, mouse_pos, mouse_up)
        return nextState

    def __display1(self, screen, mouse_pos, mouse_up):
        bHome = HomeButton((70, 50), GameStates.INSTRUCOES)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        b1 = FowardButtonIncrease((GameSettings.WIDTH - 60, GameSettings.HEIGHT/2))
        h1 = b1.hover(mouse_pos)
        self.__pos = b1.click(mouse_pos, mouse_up, self.__pos)

        title_text = GameFonts.SEMIBOLD_LARGE.render('OBJETIVO DO JOGO', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        wrap_text = ["Sobreviva a maior quantidade de",
                     "tempo sem colidir com obstáculos",
                     " ",
                     "Poderes serão gerados durante o",
                     "percurso, e te darão alguma vantagem",
                     "se você capturá-los."]
        
        description_text = []
        for text in wrap_text:
            description_text.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))

        self.cursor_handler(h0, h1)
        nextState = self.state_handler(GameStates.INSTRUCOES, s0)

        screen.fill(GameColors.AZUL)
        screen.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        screen.blit(b1.image, (b1.rect.x, b1.rect.y))
        screen.blit(title_text, title_pos)
        for pos,text_surface in enumerate(description_text[::-1]):
            text_pos = ((GameSettings.WIDTH/2 - 200), GameSettings.HEIGHT/1.5 - (pos*30))
            screen.blit(text_surface, text_pos)

        return nextState

    def __display2(self, screen, mouse_pos, mouse_up):
        bHome = HomeButton((70, 50), GameStates.INSTRUCOES)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        b1 = BackwardButtonDecrease((60, GameSettings.HEIGHT/2))
        h1 = b1.hover(mouse_pos)
        self.__pos = b1.click(mouse_pos, mouse_up, self.__pos)

        b2 = FowardButtonIncrease((GameSettings.WIDTH - 60, GameSettings.HEIGHT/2))
        h2 = b2.hover(mouse_pos)
        self.__pos = b2.click(mouse_pos, mouse_up, self.__pos)

        title_text = GameFonts.SEMIBOLD_LARGE.render('CONTROLES', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)
        
        jump_img = pygame.transform.scale(pygame.image.load(os.path.join(AVATAR_PATH, 'ninja_girl','jump4.png')), (100, 142))
        jump_pos = (GameSettings.WIDTH/2 - 250, GameSettings.HEIGHT/2 - 100)

        jump_txt = GameFonts.REGULAR_SMALL.render('PULAR: Tecla "W" ou seta para cima', False, GameColors.BRANCO)
        jump_txt_pos = (jump_pos[0] + jump_img.get_rect().width + 15, jump_pos[1] + 70)

        slide_img = pygame.transform.scale(pygame.image.load(os.path.join(AVATAR_PATH,'adventurer_boy','slide2.png')), (99, 100))
        slide_pos = (GameSettings.WIDTH/2 - 250, GameSettings.HEIGHT/2 + 50)

        slide_txt = GameFonts.REGULAR_SMALL.render('DESLIZAR: Tecla "S" ou seta para baixo', False, GameColors.BRANCO)
        slide_txt_pos = (slide_pos[0] + slide_img.get_rect().width + 15, slide_pos[1] + 70)

        self.cursor_handler(h0, h1, h2)
        nextState = self.state_handler(GameStates.INSTRUCOES, s0)

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

    def __display3(self, screen, mouse_pos, mouse_up):
        bHome = HomeButton((70, 50), GameStates.INSTRUCOES)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        b1 = BackwardButtonDecrease((60, GameSettings.HEIGHT/2))
        h1 = b1.hover(mouse_pos)
        self.__pos = b1.click(mouse_pos, mouse_up, self.__pos)

        title_text = GameFonts.SEMIBOLD_LARGE.render('PODERES', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        slow_img = pygame.transform.scale(pygame.image.load(os.path.join(POWERS_PATH,'slow.png')), (42, 106))
        slow_pos = (GameSettings.WIDTH/2 - 200, GameSettings.HEIGHT/2 - 90)

        slow_wrap_text = ["LENTIDÃO: Diminui a velocidade",
                          "do jogo por um breve período de",
                          "tempo. A pontuação continua",
                          "contando normalmente."]

        slow_txt = []
        for text in slow_wrap_text:
            slow_txt.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))

        imortal_img = pygame.transform.scale(pygame.image.load(os.path.join(POWERS_PATH,'star.png')), (82, 76))
        imortal_pos = (GameSettings.WIDTH/2 - 230, GameSettings.HEIGHT/2 + 120)

        imortal_wrap_text = ["INVENCIBILIDADE: Desativa as",
                             "colisões e aumenta a pontuação",
                             "por um breve período de tempo"]
        
        imortal_txt = []
        for text in imortal_wrap_text:
            imortal_txt.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))

        self.cursor_handler(h0, h1)
        nextState = self.state_handler(GameStates.INSTRUCOES, s0)

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
