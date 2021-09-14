import os
import pygame
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings
from views.instruction.content import Content


JUMP_PATH = os.path.join(os.getcwd(), 'assets', 'characters', 'ninja_girl', 'jump2.png')
SLIDE_PATH = os.path.join(os.getcwd(), 'assets', 'characters', 'robot', 'slide3.png')

class ControlsContent(Content):
    def __init__(self):
        super().__init__('CONTROLES')

    def display(self, screen):
        jump_img = pygame.transform.scale(pygame.image.load(JUMP_PATH), (100, 142))
        jump_pos = (GameSettings.WIDTH/2 - 250, GameSettings.HEIGHT/2 - 100)

        jump_txt = GameFonts.REGULAR_SMALL.render('PULAR: Tecla "W" ou seta para cima', False, GameColors.BRANCO)
        jump_txt_pos = (jump_pos[0] + jump_img.get_rect().width + 15, jump_pos[1] + 70)

        slide_img = pygame.transform.scale(pygame.image.load(SLIDE_PATH), (99, 100))
        slide_pos = (GameSettings.WIDTH/2 - 250, GameSettings.HEIGHT/2 + 50)

        slide_txt = GameFonts.REGULAR_SMALL.render('DESLIZAR: Tecla "S" ou seta para baixo', False, GameColors.BRANCO)
        slide_txt_pos = (slide_pos[0] + slide_img.get_rect().width + 15, slide_pos[1] + 70)

        screen.blit(self.title, self.title_rect)
        screen.blit(jump_img, jump_pos)
        screen.blit(jump_txt, jump_txt_pos)
        screen.blit(slide_img, slide_pos)
        screen.blit(slide_txt, slide_txt_pos)
