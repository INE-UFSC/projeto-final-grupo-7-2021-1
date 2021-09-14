import os
import pygame
from views.instruction.content import Content
from settings.gameSettings import GameSettings
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors


SLOW_PATH = os.path.join(os.getcwd(), 'assets', 'powers', 'slow.png')
STAR_PATH = os.path.join(os.getcwd(), 'assets', 'powers', 'star.png')

class PowersContent(Content):
    def __init__(self):
        super().__init__('PODERES')

    def display(self, screen):
        slow_img = pygame.transform.scale(pygame.image.load(SLOW_PATH), (42, 106))
        slow_pos = (GameSettings.WIDTH/2 - 200, GameSettings.HEIGHT/2 - 90)

        slow_wrap_text = ["LENTIDÃO: Diminui a velocidade",
                          "do jogo por um breve período de",
                          "tempo. A pontuação continua",
                          "contando normalmente."]
        
        slow_txt = []
        for text in slow_wrap_text:
            slow_txt.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))
        
        star_img = pygame.transform.scale(pygame.image.load(STAR_PATH), (82, 76))
        star_pos = (GameSettings.WIDTH/2 - 230, GameSettings.HEIGHT/2 + 120)

        star_wrap_text = ["INVENCIBILIDADE: Desativa as",
                          "colisões e aumenta a pontuação",
                          "por um breve período de tempo"]
        
        star_txt = []
        for text in star_wrap_text:
            star_txt.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))
        
        screen.blit(self.title, self.title_rect)

        screen.blit(slow_img, slow_pos)
        for pos, text_surf in enumerate(slow_txt):
            text_pos = (slow_pos[0] + slow_img.get_rect().width + 15, slow_pos[1] + (pos)*30)
            screen.blit(text_surf, text_pos)
        
        screen.blit(star_img, star_pos)
        for pos, text_surf in enumerate(star_txt):
            text_pos = (slow_pos[0] + slow_img.get_rect().width + 15, star_pos[1] + (pos)*30)
            screen.blit(text_surf, text_pos)
