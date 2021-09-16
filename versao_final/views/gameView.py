import pygame
from views.baseView import BaseView
from settings.gameFonts import GameFonts
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings


GAME_SETTINGS = GameSettings()

#variavel auxiliar
bg_x = 0

class GameView(BaseView):
    def __init__(self):
        super().__init__()

    def display(self, screen, score, highscore, poderes, obstaculos, player_rect, player_image):
        pygame.mouse.set_visible(False)
        self.__desenhar_cenario(screen)
        self.__desenhar_obstaculos(screen, obstaculos)
        self.__desenhar_player(screen, player_rect, player_image)
        self.__desenhar_poderes(screen, poderes)
        self.__desenhar_scores(screen, score, highscore)
    
    def __desenhar_cenario(self, screen):
        global bg_x
        
        bg = pygame.transform.scale(pygame.image.load(GAME_SETTINGS.background), (GAME_SETTINGS.WIDTH, GAME_SETTINGS.HEIGHT))
        #background infinito
        rel_x = bg_x % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < GAME_SETTINGS.WIDTH:
            screen.blit(bg, (rel_x, 0))
        bg_x -= 2


    def __desenhar_obstaculos(self, screen, obstaculos):
        for obs in obstaculos:
            pygame.draw.rect(screen, GameColors.AMARELO, obs)

    def __desenhar_poderes(self, screen, poderes):
        for poder in poderes:
            screen.blit(poder.image, (poder.rect.x, poder.rect.y))
    
    def __desenhar_player(self, screen, player_rect, player_image):
        screen.blit(player_image, player_rect)

    def __desenhar_scores(self, screen, score, highscore):
        texto_score = GameFonts.SEMIBOLD_SMALL.render(f'Score: {score}', False, GameColors.BRANCO)
        texto_highscore = GameFonts.SEMIBOLD_SMALL.render(f'High Score: {highscore}', False, GameColors.BRANCO)
        screen.blit(texto_score, (10,10))
        screen.blit(texto_highscore, ((GAME_SETTINGS.WIDTH - texto_highscore.get_rect().width - 10),10))
