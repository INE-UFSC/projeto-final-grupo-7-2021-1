from views.baseView import BaseView
from settings.gameFonts import GameFonts
from settings.gameStates import GameStates
from settings.gameColors import  GameColors
from settings.gameSettings import GameSettings
from views.buttons import HomeButton, MusicButton, SFXButton, AvatarButton, BackgroundButton


class SettingsView(BaseView):
    def display(self, screen, **kwargs):
        mouse_pos = kwargs['mouse_pos']
        mouse_up = kwargs['mouse_up']
        
        bHome = HomeButton((70, 50), GameStates.CONFIGURACOES)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        title_text = GameFonts.SEMIBOLD_LARGE.render('CONFIGURAÇÕES', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        b1 = MusicButton((GameSettings.WIDTH/2 - 150, GameSettings.HEIGHT/2 - 50))
        h1 = b1.hover(mouse_pos)
        b1.click(mouse_pos, mouse_up)

        b2 = SFXButton((GameSettings.WIDTH/2 + 150, GameSettings.HEIGHT/2 - 50))
        h2 = b2.hover(mouse_pos)
        b2.click(mouse_pos, mouse_up)

        b3 = AvatarButton((GameSettings.WIDTH/2, GameSettings.HEIGHT/2 + 50))
        h3 = b3.hover(mouse_pos)
        s3 = b3.click(mouse_pos, mouse_up)

        b4 = BackgroundButton((GameSettings.WIDTH/2, GameSettings.HEIGHT/2 + 100))
        h4 = b4.hover(mouse_pos)
        s4 = b4.click(mouse_pos, mouse_up)

        self.cursor_handler(h0, h1, h2, h3, h4)
        nextState = self.state_handler(GameStates.CONFIGURACOES, s0, s3, s4)

        screen.blit(title_text, title_pos)
        screen.fill(GameColors.AZUL)
        screen.blit(title_text, title_pos)
        screen.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        screen.blit(b1.image, (b1.rect.x, b1.rect.y))
        screen.blit(b2.image, (b2.rect.x, b2.rect.y))
        screen.blit(b3.image, (b3.rect.x, b3.rect.y))
        screen.blit(b4.image, (b4.rect.x, b4.rect.y))

        return nextState