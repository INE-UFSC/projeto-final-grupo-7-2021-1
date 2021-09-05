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

    def tela_instrucoes1(self, mouse_pos, mouse_up):
        bHome = HomeButton((70, 50), GameStates.INSTRUCOES1)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        b1 = FowardButton((GameSettings.WIDTH - 60, GameSettings.HEIGHT/2), GameStates.INSTRUCOES1, GameStates.INSTRUCOES2)
        h1 = b1.hover(mouse_pos)
        s1 = b1.click(mouse_pos, mouse_up)

        title_text = GameFonts.SEMIBOLD_LARGE.render('OBJETIVO DO JOGO', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        wrap_text = ["Sobreviva a maior quantidade de",
                     "tempo sem colidir com obstáculos",
                     " ",
                     "Poderes serão gerados durante o",
                     "percurso, e te darão alguma vantagem",
                     "se você capturá-los."]
        
        description_text = []
        for text in wrap_text:
            description_text.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))

        self.cursor_handler(h0, h1)
        nextState = self.state_handler(GameStates.INSTRUCOES1, s0, s1)

        self.__window.fill(GameColors.AZUL)
        self.__window.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        self.__window.blit(b1.image, (b1.rect.x, b1.rect.y))
        self.__window.blit(title_text, title_pos)
        for pos,text_surface in enumerate(description_text[::-1]):
            text_pos = ((GameSettings.WIDTH/2 - 200), GameSettings.HEIGHT/1.5 - (pos*30))
            self.__window.blit(text_surface, text_pos)

        return nextState

    def tela_instrucoes2(self, mouse_pos, mouse_up):
        bHome = HomeButton((70, 50), GameStates.INSTRUCOES2)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        b1 = BackwardButton((60, GameSettings.HEIGHT/2), GameStates.INSTRUCOES2, GameStates.INSTRUCOES1)
        h1 = b1.hover(mouse_pos)
        s1 = b1.click(mouse_pos, mouse_up)

        b2 = FowardButton((GameSettings.WIDTH - 60, GameSettings.HEIGHT/2), GameStates.INSTRUCOES2, GameStates.INSTRUCOES3)
        h2 = b2.hover(mouse_pos)
        s2 = b2.click(mouse_pos, mouse_up)

        title_text = GameFonts.SEMIBOLD_LARGE.render('CONTROLES', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        jump_img = pygame.transform.scale(pygame.image.load(os.path.join("versao_final\\assets\\characters\\ninja_girl\\jump4.png")), (100, 142))
        jump_pos = (GameSettings.WIDTH/2 - 250, GameSettings.HEIGHT/2 - 100)

        jump_txt = GameFonts.REGULAR_SMALL.render('PULAR: Tecla "W" ou seta para cima', False, GameColors.BRANCO)
        jump_txt_pos = (jump_pos[0] + jump_img.get_rect().width + 15, jump_pos[1] + 70)

        slide_img = pygame.transform.scale(pygame.image.load(os.path.join("versao_final\\assets\\characters\\adventurer_boy\\slide2.png")), (99, 100))
        slide_pos = (GameSettings.WIDTH/2 - 250, GameSettings.HEIGHT/2 + 50)

        slide_txt = GameFonts.REGULAR_SMALL.render('DESLIZAR: Tecla "S" ou seta para baixo', False, GameColors.BRANCO)
        slide_txt_pos = (slide_pos[0] + slide_img.get_rect().width + 15, slide_pos[1] + 70)

        self.cursor_handler(h0, h1, h2)
        nextState = self.state_handler(GameStates.INSTRUCOES2, s0, s1, s2)

        self.__window.fill(GameColors.AZUL)
        self.__window.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        self.__window.blit(b1.image, (b1.rect.x, b1.rect.y))
        self.__window.blit(b2.image, (b2.rect.x, b2.rect.y))
        self.__window.blit(title_text, title_pos)
        self.__window.blit(jump_img, jump_pos)
        self.__window.blit(jump_txt, jump_txt_pos)
        self.__window.blit(slide_img, slide_pos)
        self.__window.blit(slide_txt, slide_txt_pos)

        return nextState

    def tela_instrucoes3(self, mouse_pos, mouse_up):
        bHome = HomeButton((70, 50), GameStates.INSTRUCOES3)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        b1 = BackwardButton((60, GameSettings.HEIGHT/2), GameStates.INSTRUCOES3, GameStates.INSTRUCOES2)
        h1 = b1.hover(mouse_pos)
        s1 = b1.click(mouse_pos, mouse_up)

        title_text = GameFonts.SEMIBOLD_LARGE.render('PODERES', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        slow_img = pygame.transform.scale(pygame.image.load(os.path.join("versao_final\\assets\\powers\\slow.png")), (42, 106))
        slow_pos = (GameSettings.WIDTH/2 - 200, GameSettings.HEIGHT/2 - 90)

        slow_wrap_text = ["LENTIDÃO: Diminui a velocidade",
                          "do jogo por um breve período de",
                          "tempo. A pontuação continua",
                          "contando normalmente."]

        slow_txt = []
        for text in slow_wrap_text:
            slow_txt.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))

        imortal_img = pygame.transform.scale(pygame.image.load(os.path.join("versao_final\\assets\\powers\\star.png")), (82, 76))
        imortal_pos = (GameSettings.WIDTH/2 - 230, GameSettings.HEIGHT/2 + 120)

        imortal_wrap_text = ["INVENCIBILIDADE: Desativa as",
                             "colisões e aumenta a pontuação",
                             "por um breve período de tempo"]
        
        imortal_txt = []
        for text in imortal_wrap_text:
            imortal_txt.append(GameFonts.REGULAR_SMALL.render(text, False, GameColors.BRANCO))

        self.cursor_handler(h0, h1)
        nextState = self.state_handler(GameStates.INSTRUCOES3, s0, s1)

        self.__window.fill(GameColors.AZUL)
        self.__window.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        self.__window.blit(b1.image, (b1.rect.x, b1.rect.y))
        self.__window.blit(title_text, title_pos)

        self.__window.blit(slow_img, slow_pos)
        for pos, text_surface in enumerate(slow_txt):
            text_pos = (slow_pos[0] + slow_img.get_rect().width + 15, slow_pos[1] + (pos)*30)
            self.__window.blit(text_surface, text_pos)

        self.__window.blit(imortal_img, imortal_pos)
        for pos, text_surface in enumerate(imortal_txt):
            text_pos = (slow_pos[0] + slow_img.get_rect().width + 15, imortal_pos[1] + (pos)*30)
            self.__window.blit(text_surface, text_pos)

        return nextState

    def tela_ranking(self, mouse_pos, mouse_up):
        bHome = HomeButton((70, 50), GameStates.RANKING)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        title_text = GameFonts.SEMIBOLD_LARGE.render('RANKING', False, GameColors.BRANCO)
        title_pos = ((GameSettings.WIDTH/2 - title_text.get_rect().width/2), GameSettings.HEIGHT/2 - 170)

        top_scores = self.__controlador.get_highscores()
        highscores_txt = []
        for pos, value in enumerate(top_scores):
            highscores_txt.append(GameFonts.REGULAR_LARGE.render(f'{pos+1}. {value}', False, GameColors.BRANCO))

        self.cursor_handler(h0)
        nextState = self.state_handler(GameStates.RANKING, s0)

        self.__window.fill(GameColors.AZUL)
        self.__window.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        self.__window.blit(title_text, title_pos)
        for pos, text_surface in enumerate(highscores_txt):
            text_pos  = (GameSettings.WIDTH/2 - 50, GameSettings.HEIGHT/3 + (pos*40))
            self.__window.blit(text_surface, text_pos)

        return nextState

    def tela_jogo(self):
        pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)
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
        texto_score = GameFonts.SEMIBOLD_SMALL.render(f'Score: {self.__controlador.get_score()}', False, GameColors.BRANCO)
        self.__window.blit(texto_score, (10,10))
        texto_highscore = GameFonts.SEMIBOLD_SMALL.render(f'High Score: {self.__controlador.highscore}', False, GameColors.BRANCO)
        self.__window.blit(texto_highscore, ((GameSettings.WIDTH - texto_highscore.get_rect().width - 10),10))

    def tela_pause(self):
        texto_pausado = GameFonts.SEMIBOLD_LARGE.render('JOGO PAUSADO', False, GameColors.BRANCO)
        pausado_pos = ((GameSettings.WIDTH - texto_pausado.get_rect().width)/2, (GameSettings.HEIGHT - texto_pausado.get_rect().height)/2)
        texto_sair_pause = GameFonts.REGULAR_SMALL.render('Aperte ESC para sair do pause', False, GameColors.BRANCO)
        text_sair_pos = ((GameSettings.WIDTH- texto_sair_pause.get_rect().width)/2,
                         (GameSettings.HEIGHT - texto_sair_pause.get_rect().height)/2 + 70)
        
        background = pygame.Surface((GameSettings.WIDTH, GameSettings.HEIGHT))
        background.set_alpha(100)
        background.fill(GameColors.PRETO)

        self.__window.blit(background, (0,0))
        self.__window.blit(texto_pausado,pausado_pos)
        self.__window.blit(texto_sair_pause,text_sair_pos)

    def tela_endgame(self, mouse_pos, mouse_up):
        endgame = GameFonts.SEMIBOLD_LARGE.render('Game Over!', False, GameColors.BRANCO)
        endgame_pos = ((GameSettings.WIDTH - endgame.get_rect().width)/2, (GameSettings.HEIGHT - endgame.get_rect().height)/2 - 80)

        pontuacao = GameFonts.SEMIBOLD_LARGE.render(f'Pontuação: {self.__controlador.get_final_score()}', False, GameColors.BRANCO)
        pontuacao_pos = ((GameSettings.WIDTH - pontuacao.get_rect().width)/2, (GameSettings.HEIGHT - pontuacao.get_rect().height)/2)

        bHome = HomeButton((GameSettings.WIDTH/2 - 100, GameSettings.HEIGHT/2 + 150), GameStates.ENDGAME)
        h0 = bHome.hover(mouse_pos)
        s0 = bHome.click(mouse_pos, mouse_up)

        bReset = ResetButton((GameSettings.WIDTH/2 + 100, GameSettings.HEIGHT/2 + 150), GameStates.ENDGAME)
        h1 = bReset.hover(mouse_pos)
        s1 = bReset.click(mouse_pos, mouse_up)

        self.cursor_handler(h0, h1)
        nextState = self.state_handler(GameStates.ENDGAME, s0, s1)

        self.__window.fill(GameColors.LILAS)
        self.__window.blit(endgame, endgame_pos)
        self.__window.blit(pontuacao, pontuacao_pos)
        self.__window.blit(bHome.image, (bHome.rect.x, bHome.rect.y))
        self.__window.blit(bReset.image, (bReset.rect.x, bReset.rect.y))

        return nextState

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
