import pygame
from views.baseView import BaseView
from settings.gameFonts import GameFonts
from settings.gameSettings import GameSettings
from settings.gameColors import GameColors
from settings.gameStates import GameStates
from views.buttons import HomeButton, ResetButton


class EndgameView(BaseView):
    def display(self, screen, **kwargs):
        mouse_pos = kwargs['mouse_pos']
        mouse_up = kwargs['mouse_up']
        final_score = kwargs['final_score']

        endgame = GameFonts.SEMIBOLD_LARGE.render('Game Over!', False, GameColors.BRANCO)
        endgame_pos = ((GameSettings.WIDTH - endgame.get_rect().width)/2, (GameSettings.HEIGHT - endgame.get_rect().height)/2 - 80)

        pontuacao = GameFonts.SEMIBOLD_LARGE.render(f'Pontuação: {final_score}', False, GameColors.BRANCO)
        pontuacao_pos = ((GameSettings.WIDTH - pontuacao.get_rect().width)/2, (GameSettings.HEIGHT - pontuacao.get_rect().height)/2)

        bHome = HomeButton((GameSettings.WIDTH/2 - 100, GameSettings.HEIGHT/2 + 150), GameStates.ENDGAME)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        bReset = ResetButton((GameSettings.WIDTH/2 + 100, GameSettings.HEIGHT/2 + 150), GameStates.ENDGAME)
        h1 = bReset.hover(mouse_pos)
        s1 = bReset.click(mouse_pos, mouse_up)

        pygame.mouse.set_visible(True)
        self.cursor_handler(h0, h1)
        nextState = self.state_handler(GameStates.ENDGAME, s0, s1)

        screen.fill(GameColors.LILAS)
        screen.blit(endgame, endgame_pos)
        screen.blit(pontuacao, pontuacao_pos)
        screen.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        screen.blit(bReset.image, (bReset.rect.x, bReset.rect.y))

        return nextState
