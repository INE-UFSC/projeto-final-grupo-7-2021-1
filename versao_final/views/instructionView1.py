from views.baseView import BaseView
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameStates import GameStates
from settings.gameSettings import GameSettings
from views.buttons import HomeButton, FowardButton


class InstructionView1(BaseView):
    def display(self, screen, **kwargs):
        mouse_pos = kwargs['mouse_pos']
        mouse_up = kwargs['mouse_up']
        bHome = HomeButton((70, 50), GameStates.INSTRUCOES1)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        b1 = FowardButton((GameSettings.WIDTH - 60, GameSettings.HEIGHT/2), GameStates.INSTRUCOES1, GameStates.INSTRUCOES2)
        h1 = b1.hover(mouse_pos)
        s1 = b1.click(mouse_pos, mouse_up)

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
        nextState = self.state_handler(GameStates.INSTRUCOES1, s0, s1)

        screen.fill(GameColors.AZUL)
        screen.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        screen.blit(b1.image, (b1.rect.x, b1.rect.y))
        screen.blit(title_text, title_pos)
        for pos,text_surface in enumerate(description_text[::-1]):
            text_pos = ((GameSettings.WIDTH/2 - 200), GameSettings.HEIGHT/1.5 - (pos*30))
            screen.blit(text_surface, text_pos)

        return nextState
