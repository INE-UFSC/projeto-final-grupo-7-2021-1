import pygame
from views.baseView import BaseView
from settings.gameStates import GameStates
from settings.gameSettings import GameSettings
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from views.buttons import HomeButton, ResetButton


class PauseView(BaseView):
    def __init__(self):
        self.__isPaused = False #para manter o alpha

    def display(self, screen, **kwargs):
        mouse_pos = kwargs['mouse_pos']
        mouse_up = kwargs['mouse_up']

        bHome = HomeButton((GameSettings.WIDTH/2, GameSettings.HEIGHT/2 + 150), GameStates.PAUSADO)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        if not self.__isPaused:
            self.__display_content(screen, bHome)

        pygame.mouse.set_visible(True)
        self.cursor_handler(h0)
        nextState = self.state_handler(GameStates.ENDGAME, s0)

        return nextState

    def __display_content(self, screen, bHome):
        texto_pausado = GameFonts.SEMIBOLD_LARGE.render('JOGO PAUSADO', False, GameColors.BRANCO)
        pausado_pos = ((GameSettings.WIDTH - texto_pausado.get_rect().width)/2, (GameSettings.HEIGHT - texto_pausado.get_rect().height)/2)
        texto_sair_pause = GameFonts.REGULAR_SMALL.render('Aperte ESC para sair do pause', False, GameColors.BRANCO)
        text_sair_pos = ((GameSettings.WIDTH- texto_sair_pause.get_rect().width)/2,
                         (GameSettings.HEIGHT - texto_sair_pause.get_rect().height)/2 + 70)
        
        background = pygame.Surface((GameSettings.WIDTH, GameSettings.HEIGHT))
        background.set_alpha(100)
        background.fill(GameColors.PRETO)

        screen.blit(background, (0,0))
        screen.blit(texto_pausado,pausado_pos)
        screen.blit(texto_sair_pause,text_sair_pos)
        screen.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        self.__isPaused = True