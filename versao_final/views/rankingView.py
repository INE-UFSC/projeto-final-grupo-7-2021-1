from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from views.backHomeView import ViewWithHomeButton


GAME_SETTINGS = GameSettings()

class RankingView(ViewWithHomeButton):
    def __init__(self):
        super().__init__(GameColors.AZUL, 'RANKING')

    def display(self, screen, mouse_up, top_scores):
        s0 = super().display(screen, mouse_up)

        highscores_txt = []
        for pos, value in enumerate(top_scores):
            highscores_txt.append(GameFonts.REGULAR_LARGE.render(f'{pos+1}. {value}', False, GameColors.BRANCO))
    
        for pos, text_surface in enumerate(highscores_txt):
            text_pos  = (GAME_SETTINGS.WIDTH/2 - 50, GAME_SETTINGS.HEIGHT/3 + (pos*40))
            screen.blit(text_surface, text_pos)
        
        return self.button_states_handler('ranking', [s0])