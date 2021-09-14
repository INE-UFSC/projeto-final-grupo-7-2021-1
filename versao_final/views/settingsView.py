from views.buttons import TextButton
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from views.backHomeView import ViewWithHomeButton


class SettingsView(ViewWithHomeButton):
    def __init__(self):
        super().__init__(GameColors.AZUL, 'CONFIGURAÇÕES')
        self.__buttons = [TextButton('Volume: ON', 160, 40, (GameSettings.WIDTH/2 - 150, GameSettings.HEIGHT/2 - 50)),
                          TextButton('SFX: OFF', 160, 40, (GameSettings.WIDTH/2 + 150, GameSettings.HEIGHT/2 - 50))]

    def display(self, screen):
        super().display(screen)
        for btn in self.__buttons:
            btn.draw(screen)
            btn.hover()
            btn.click()
