from views.buttons import MusicButton, SfxButton, TextButton
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from views.backHomeView import ViewWithHomeButton


GAME_SETTINGS = GameSettings()

class SettingsView(ViewWithHomeButton):
    def __init__(self):
        super().__init__(GameColors.AZUL, 'CONFIGURAÇÕES')
        self.__buttons = [MusicButton(160, 40, (GAME_SETTINGS.WIDTH/2 - 150 - 80, GAME_SETTINGS.HEIGHT/2 - 50)),
                          SfxButton(160, 40, (GAME_SETTINGS.WIDTH/2 + 150 - 80, GAME_SETTINGS.HEIGHT/2 - 50)),
                          TextButton('Selecionar Avatar', 220, 40, (GAME_SETTINGS.WIDTH/2 - 110, GAME_SETTINGS.HEIGHT/2 + 50), 'sel_avatar'),
                          TextButton('Selecionar Cenário', 220, 40, (GAME_SETTINGS.WIDTH/2 - 110, GAME_SETTINGS.HEIGHT/2 + 110), 'sel_bg')]

    def display(self, screen, mouse_up):
        s0 = super().display(screen, mouse_up)
        states = [s0]
        for btn in self.__buttons:
            btn.draw(screen)
            btn.hover()
            states.append(btn.click(mouse_up))
        
        return self.button_states_handler('configuracoes',states)
