from abc import abstractmethod, ABC
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings


GAME_SETTINGS = GameSettings()

class Content(ABC):
    def __init__(self, title):
        self.__title = GameFonts.SEMIBOLD_LARGE.render(title, False, GameColors.BRANCO)
        pos = (GAME_SETTINGS.WIDTH/2, GAME_SETTINGS.HEIGHT/2 - 170)
        self.__title_rect = self.__title.get_rect(center=pos)

    @property
    def title(self):
        return self.__title

    @property
    def title_rect(self):
        return self.__title_rect

    @abstractmethod
    def display(self, screen):
        raise NotImplementedError
