import pygame
from views.baseView import BaseView
from settings.gameFonts import GameFonts
from settings.gameStates import GameStates
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings


class GameView(BaseView):
    def display(self, screen, **kwargs):
        score = kwargs['score']
        highscore = kwargs['highscore']
        poderes = kwargs['poderes']
        obstaculos = kwargs['obstaculos']
        player_rect = kwargs['player_rect']
        player_color = kwargs['player_color']
        pygame.mouse.set_visible(False)
        self.__desenhar_cenario(screen)
        self.__desenhar_obstaculos(screen, obstaculos)
        self.__desenhar_poderes(screen, poderes)
        self.__desenhar_player(screen, player_color, player_rect)
        self.__desenhar_scores(screen, score, highscore)
        return GameStates.JOGANDO

    def __desenhar_player(self, screen, player_color, player_rect):
        pygame.draw.rect(screen, player_color, player_rect)

    def __desenhar_cenario(self, screen):
        ceu = pygame.Rect(0, 0, GameSettings.WIDTH, GameSettings.HEIGHT)
        chao = pygame.Rect(0, GameSettings.COMECO_CHAO, GameSettings.WIDTH, GameSettings.HEIGHT)
        pygame.draw.rect(screen, GameColors.AZUL, ceu)
        pygame.draw.rect(screen, GameColors.VERDE, chao)

    def __desenhar_obstaculos(self, screen, obstaculos):
        for obs in obstaculos:
            pygame.draw.rect(screen, GameColors.AMARELO, obs)

    def __desenhar_poderes(self, screen, poderes):
        for poder in poderes:
            screen.blit(poder.image, (poder.rect.x, poder.rect.y))

    def __desenhar_scores(self, screen, score, highscore):
        texto_score = GameFonts.SEMIBOLD_SMALL.render(f'Score: {score}', False, GameColors.BRANCO)
        texto_highscore = GameFonts.SEMIBOLD_SMALL.render(f'High Score: {highscore}', False, GameColors.BRANCO)
        screen.blit(texto_score, (10,10))
        screen.blit(texto_highscore, ((GameSettings.WIDTH - texto_highscore.get_rect().width - 10),10))
