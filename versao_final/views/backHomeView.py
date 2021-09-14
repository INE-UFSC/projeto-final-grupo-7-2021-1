from abc import ABC, abstractmethod
from views.baseView import BaseView
from views.buttons import HomeButton
from settings.gameColors import GameColors
from settings.gameFonts import GameFonts
from settings.gameSettings import GameSettings

class ViewWithHomeButton(BaseView, ABC):
    def __init__(self, color, title=' '):
        super().__init__(color)
        self.__homeButton = HomeButton(100, 100, (50,50))
        self.__title = GameFonts.SEMIBOLD_LARGE.render(title, False, GameColors.BRANCO)
        pos = (GameSettings.WIDTH/2, GameSettings.HEIGHT/2 - 170)
        self.__title_rect = self.__title.get_rect(center=pos)

    @abstractmethod
    def display(self, screen, mouse_up):
        screen.fill(self.color)
        screen.blit(self.__title, self.__title_rect)
        self.__homeButton.draw(screen)
        self.__homeButton.hover()
        return self.__homeButton.click(mouse_up)
