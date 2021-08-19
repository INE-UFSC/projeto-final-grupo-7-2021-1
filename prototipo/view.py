import pygame
from pygame.font import SysFont


pygame.font.init()


#configs
AMARELO = (255,255,0)
BRANCO = (255,255,255)
PRETO = (0,0,0)
COR_CHAO = (50,150,50)
COR_CEU = (100,100,255)
MAIN_FONT = SysFont('Helvetica',25)
PAUSED_FONT = SysFont('Helvetica', 40)
END_FONT = SysFont('Helvetica', 40)
BG_ENDGAME = (151,72,247)

class View:
    def __init__(self, controlador, width, height):
        self.__controlador = controlador
        self.__screen_width = width
        self.__screen_height = height
        self.__window = pygame.display.set_mode((self.__screen_width, self.__screen_height))

    def desenhar(self):
        if not self.__controlador.pausado:
            self.__desenhar_cenario()
            self.__desenhar_obstaculos()
            self.__desenhar_poderes()
            self.__desenhar_player()
            self.__desenhar_scores()

    def __desenhar_player(self):
        pygame.draw.rect(self.__window, self.__controlador.player.cor, self.__controlador.player)

    def __desenhar_cenario(self):
        pygame.draw.rect(self.__window, COR_CEU, self.__controlador.cenario.ceu)
        pygame.draw.rect(self.__window, COR_CHAO, self.__controlador.cenario.chao)

    def __desenhar_obstaculos(self):
        for obs in self.__controlador.cenario.obstaculos:
            pygame.draw.rect(self.__window, AMARELO, obs)

    def __desenhar_poderes(self):
        for poder in self.__controlador.cenario.poderes:
            pygame.draw.rect(self.__window, poder.cor, poder)

    def __desenhar_scores(self):
        texto_score = MAIN_FONT.render(f'Score: {self.__controlador.get_score()}', False, BRANCO)
        self.__window.blit(texto_score, (10,10))
        texto_highscore = MAIN_FONT.render(f'High Score: {self.__controlador.highScore}', False, BRANCO)
        self.__window.blit(texto_highscore, (700,10))

    def tela_pause(self):
        texto_pausado = PAUSED_FONT.render('JOGO PAUSADO', False, BRANCO)
        pausado_pos = ((self.__screen_width - texto_pausado.get_rect().width)/2, (self.__screen_height - texto_pausado.get_rect().height)/2)
        texto_sair_pause = MAIN_FONT.render('Aperte ESC para sair do pause', False, BRANCO)
        text_sair_pos = ((self.__screen_width - texto_sair_pause.get_rect().width)/2, (self.__screen_height - texto_sair_pause.get_rect().height)/2 + 70)
        
        background = pygame.Surface((self.__screen_width, self.__screen_height))
        background.set_alpha(100)
        background.fill(PRETO)

        self.__window.blit(background, (0,0))
        self.__window.blit(texto_pausado,pausado_pos)
        self.__window.blit(texto_sair_pause,text_sair_pos)

    def tela_endgame(self):
        endgame = END_FONT.render('Game Over!', False, BRANCO)
        pontuacao = END_FONT.render(f'Pontuação: {self.__controlador.get_score()}', False, BRANCO)
        reiniciar = MAIN_FONT.render('Aperte Enter para reiniciar', False, BRANCO)

        endgame_pos = ((self.__screen_width - endgame.get_rect().width)/2, (self.__screen_height - endgame.get_rect().height)/2 - 80)
        pontuacao_pos = ((self.__screen_width-pontuacao.get_rect().width)/2, (self.__screen_height - pontuacao.get_rect().height)/2)
        reiniciar_pos = ((self.__screen_width- reiniciar.get_rect().width)/2, (self.__screen_height - reiniciar.get_rect().height)/2 + 100)
        
        background = pygame.Rect(0,0,self.__screen_width,self.__screen_height)
        pygame.draw.rect(self.__window, BG_ENDGAME, background)
        
        self.__window.blit(endgame, endgame_pos)
        self.__window.blit(pontuacao, pontuacao_pos)
        self.__window.blit(reiniciar, reiniciar_pos)
