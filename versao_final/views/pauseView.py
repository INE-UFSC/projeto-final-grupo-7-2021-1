import pygame
from views.baseView import BaseView
from views.buttons import HomeButton
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings


GAME_SETTINGS = GameSettings()

class PauseView(BaseView):
    def __init__(self):
        super().__init__(GameColors.LILAS)
        self.__bHome = HomeButton(100, 80, (GAME_SETTINGS.WIDTH/2 - 50, GAME_SETTINGS.HEIGHT/2 + 150))

    def display(self, screen, mouse_up):
        screen.fill(self.color)

        pygame.mouse.set_visible(True)
        self.__bHome.draw(screen)
        self.__bHome.hover()
        s0 = self.__bHome.click(mouse_up)

        texto_pausado = GameFonts.SEMIBOLD_LARGE.render('JOGO PAUSADO', False, GameColors.BRANCO)
        pausado_pos = ((GAME_SETTINGS.WIDTH - texto_pausado.get_rect().width)/2, (GAME_SETTINGS.HEIGHT - texto_pausado.get_rect().height)/2)
        
        texto_sair_pause = GameFonts.REGULAR_SMALL.render('Aperte ESC para sair do pause', False, GameColors.BRANCO)
        sair_pos = ((GAME_SETTINGS.WIDTH- texto_sair_pause.get_rect().width)/2,
                         (GAME_SETTINGS.HEIGHT - texto_sair_pause.get_rect().height)/2 + 70)
        
        screen.blit(texto_pausado, pausado_pos)
        screen.blit(texto_sair_pause, sair_pos)

        return self.button_states_handler('pausado', [s0])
