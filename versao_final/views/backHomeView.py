from abc import ABC, abstractmethod
from views.baseView import BaseView
from views.buttons import HomeButton
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings


GAME_SETTINGS = GameSettings()

class ViewWithHomeButton(BaseView, ABC):
    def __init__(self, title=' '):
        super().__init__()
        self.__homeButton = HomeButton(100, 80, (30,30))
        self.__title = GameFonts.SEMIBOLD_LARGE.render(title, False, GameColors.BRANCO)
        pos = (GAME_SETTINGS.WIDTH/2, GAME_SETTINGS.HEIGHT/2 - 170)
        self.__title_rect = self.__title.get_rect(center=pos)

    @abstractmethod
    def display(self, screen, mouse_up):
        screen.fill(self.color)
        screen.blit(self.__title, self.__title_rect)
        self.__homeButton.draw(screen)
        self.__homeButton.hover()
        return self.__homeButton.click(mouse_up)
