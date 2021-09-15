from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from views.instruction.content import Content
from settings.gameSettings import GameSettings


GAME_SETTINGS = GameSettings()

class ObjectivesContent(Content):
    def __init__(self):
        super().__init__('OBJETIVO DO JOGO')

    def display(self, screen):
        wrap_text = ["Sobreviva a maior quantidade de",
                     "tempo sem colidir com obstáculos",
                     " ",
                     "Poderes serão gerados durante o",
                     "percurso, e te darão alguma vantagem",
                     "se você capturá-los."]
        
        description_text = []
        for text in wrap_text:
            description_text.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))
        
        screen.blit(self.title, self.title_rect)
        for pos,text_surface in enumerate(description_text[::-1]):
            text_pos = ((GAME_SETTINGS.WIDTH/2 - 200), GAME_SETTINGS.HEIGHT/1.5 - (pos*30))
            screen.blit(text_surface, text_pos)
