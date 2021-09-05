import pygame
import os
from views.buttons import *
from settings.gameFonts import GameFonts
from settings.gameStates import GameStates
from settings.gameColors import GameColors
from settings.gameSettings import GameSettings

#variavel auxiliar
menu_bg_x = 0

class View:
    def __init__(self, controlador):
        self.__controlador = controlador
        self.__window = pygame.display.set_mode((GameSettings.WIDTH, GameSettings.HEIGHT))

    def tela_menu(self, mouse_pos, mouse_up):
        global menu_bg_x
        bg = pygame.transform.scale(pygame.image.load(os.path.join("versao_final\\assets\\backgrounds\\cyberpunk-street.png")),
                                    (GameSettings.WIDTH, GameSettings.HEIGHT))
        
        #background infinito
        rel_x = menu_bg_x % bg.get_rect().width
        self.__window.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < GameSettings.WIDTH:
            self.__window.blit(bg, (rel_x,0))
        menu_bg_x -= 1

        b0 = PlayButton((GameSettings.WIDTH/2, (GameSettings.HEIGHT/2) - 80), GameStates.MENU, GameStates.JOGANDO)
        h0 = b0.hover(mouse_pos)
        s0 = b0.click(mouse_pos, mouse_up)

        b1 = InstructionButton((GameSettings.WIDTH/2, (GameSettings.HEIGHT/2) - 20), GameStates.MENU, GameStates.INSTRUCOES1)
        h1 = b1.hover(mouse_pos)
        s1 = b1.click(mouse_pos, mouse_up)

        b2 = SettingsButton((GameSettings.WIDTH/2, (GameSettings.HEIGHT/2) + 40), GameStates.MENU, GameStates.CONFIGURACOES)
        h2 = b2.hover(mouse_pos)
        s2 = b2.click(mouse_pos, mouse_up)

        b3 = RankingButton((GameSettings.WIDTH/2, (GameSettings.HEIGHT/2) + 100), GameStates.MENU, GameStates.RANKING)
        h3 = b3.hover(mouse_pos)
        s3 = b3.click(mouse_pos, mouse_up)

        self.cursor_handler(h0, h1, h2, h3)
        nextState = self.state_handler(GameStates.MENU, s0, s1, s2, s3)

        self.__window.blit(b0.image, (b0.rect.x, b0.rect.y))
        self.__window.blit(b1.image, (b1.rect.x, b1.rect.y))
        self.__window.blit(b2.image, (b2.rect.x, b2.rect.y))
        self.__window.blit(b3.image, (b3.rect.x, b3.rect.y))

        return nextState

    def tela_jogo(self):
        self.__desenhar_cenario()
        self.__desenhar_obstaculos()
        self.__desenhar_poderes()
        self.__desenhar_player()
        self.__desenhar_scores()

    def __desenhar_player(self):
        pygame.draw.rect(self.__window, self.__controlador.player.cor, self.__controlador.player)

    def __desenhar_cenario(self):
        pygame.draw.rect(self.__window, GameColors.AZUL, self.__controlador.cenario.ceu)
        pygame.draw.rect(self.__window, GameColors.VERDE, self.__controlador.cenario.chao)

    def __desenhar_obstaculos(self):
        for obs in self.__controlador.cenario.obstaculos:
            pygame.draw.rect(self.__window, GameColors.AMARELO, obs)

    def __desenhar_poderes(self):
        for poder in self.__controlador.cenario.poderes:
            pygame.draw.rect(self.__window, poder.cor, poder)

    def __desenhar_scores(self):
        texto_score = GameFonts.SEMIBOLD_LARGE.render(f'Score: {self.__controlador.get_score()}', False, GameColors.BRANCO)
        self.__window.blit(texto_score, (10,10))
        texto_highscore = GameFonts.SEMIBOLD_LARGE.render(f'High Score: {self.__controlador.highscore}', False, GameColors.BRANCO)
        self.__window.blit(texto_highscore, ((self.__screen_width - texto_highscore.get_rect().width - 10),10))

    def tela_pause(self):
        texto_pausado = GameFonts.SEMIBOLD_LARGE.render('JOGO PAUSADO', False, GameColors.BRANCO)
        pausado_pos = ((self.__screen_width - texto_pausado.get_rect().width)/2, (self.__screen_height - texto_pausado.get_rect().height)/2)
        texto_sair_pause = GameFonts.REGULAR_SMALL.render('Aperte ESC para sair do pause', False, GameColors.BRANCO)
        text_sair_pos = ((self.__screen_width - texto_sair_pause.get_rect().width)/2, (self.__screen_height - texto_sair_pause.get_rect().height)/2 + 70)
        
        background = pygame.Surface((self.__screen_width, self.__screen_height))
        background.set_alpha(100)
        background.fill(GameColors.PRETO)

        self.__window.blit(background, (0,0))
        self.__window.blit(texto_pausado,pausado_pos)
        self.__window.blit(texto_sair_pause,text_sair_pos)

    def tela_endgame(self):
        endgame = GameFonts.SEMIBOLD_LARGE.render('Game Over!', False, GameColors.BRANCO)
        pontuacao = GameFonts.SEMIBOLD_LARGE.render(f'Pontuação: {self.__controlador.get_score()}', False, GameColors.BRANCO)
        reiniciar = GameFonts.LIGHT_SMALL.render('Aperte Enter para reiniciar', False, GameColors.BRANCO)

        endgame_pos = ((self.__screen_width - endgame.get_rect().width)/2, (self.__screen_height - endgame.get_rect().height)/2 - 80)
        pontuacao_pos = ((self.__screen_width-pontuacao.get_rect().width)/2, (self.__screen_height - pontuacao.get_rect().height)/2)
        reiniciar_pos = ((self.__screen_width- reiniciar.get_rect().width)/2, (self.__screen_height - reiniciar.get_rect().height)/2 + 100)
        
        background = pygame.Rect(0,0,self.__screen_width,self.__screen_height)
        pygame.draw.rect(self.__window, GameColors.PRETO, background)
        
        self.__window.blit(endgame, endgame_pos)
        self.__window.blit(pontuacao, pontuacao_pos)
        self.__window.blit(reiniciar, reiniciar_pos)

    def cursor_handler(self, *args):
        for btn in args:
            if btn:
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_HAND)
                break
            else:
                pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def state_handler(self, currentState, *args):
        for state in args:
            if state != currentState:
                return state
        return currentState