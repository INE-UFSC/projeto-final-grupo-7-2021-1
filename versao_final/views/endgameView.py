import pygame
from views.baseView import BaseView
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from settings.gameFonts import GameFonts
from views.buttons import HomeButton, RestartButton


GAME_SETTINGS = GameSettings()

class EndgameView(BaseView):
    def __init__(self):
        super().__init__(GameColors.LILAS)
        self.__buttons = [HomeButton(100, 80, (GAME_SETTINGS.WIDTH/2 - 100 - 50, GAME_SETTINGS.HEIGHT/2+150)),
                          RestartButton(100, 80, (GAME_SETTINGS.WIDTH/2 + 100 - 50, GAME_SETTINGS.HEIGHT/2 + 150))]

    def display(self, screen, final_score, mouse_up):
        screen.fill(self.color)
        pygame.mouse.set_visible(True)

        endgame = GameFonts.SEMIBOLD_LARGE.render('Game Over!', False, GameColors.BRANCO)
        endgame_pos = ((GAME_SETTINGS.WIDTH - endgame.get_rect().width)/2, (GAME_SETTINGS.HEIGHT - endgame.get_rect().height)/2 - 80)

        pontuacao = GameFonts.SEMIBOLD_LARGE.render(f'Pontuação: {final_score}', False, GameColors.BRANCO)
        pontuacao_pos = ((GAME_SETTINGS.WIDTH - pontuacao.get_rect().width)/2, (GAME_SETTINGS.HEIGHT - pontuacao.get_rect().height)/2)

        screen.blit(endgame, endgame_pos)
        screen.blit(pontuacao, pontuacao_pos)

        states = []
        for btn in self.__buttons:
            btn.draw(screen)
            btn.hover()
            states.append(btn.click(mouse_up))
        
        return self.button_states_handler('endgame',states)

