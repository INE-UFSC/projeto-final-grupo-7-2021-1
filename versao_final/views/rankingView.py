from views.baseView import BaseView
from views.buttons import HomeButton
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from settings.gameFonts import GameFonts
from settings.gameStates import GameStates


class RankingView(BaseView):
    def display(self, screen, **kwargs):
        mouse_pos = kwargs['mouse_pos']
        mouse_up = kwargs['mouse_up']
        top_scores = kwargs['top_scores']

        bHome = HomeButton((70, 50), GameStates.RANKING)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        title_text = GameFonts.SEMIBOLD_LARGE.render('RANKING', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        highscores_txt = []
        for pos, value in enumerate(top_scores):
            highscores_txt.append(GameFonts.REGULAR_LARGE.render(f'{pos+1}. {value}', False, GameColors.BRANCO))

        self.cursor_handler(h0)
        nextState = self.state_handler(GameStates.RANKING, s0)

        screen.fill(GameColors.AZUL)
        screen.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        screen.blit(title_text, title_pos)
        for pos, text_surface in enumerate(highscores_txt):
            text_pos  = (GameSettings.WIDTH/2 - 50, GameSettings.HEIGHT/3 + (pos*40))
            screen.blit(text_surface, text_pos)

        return nextState
