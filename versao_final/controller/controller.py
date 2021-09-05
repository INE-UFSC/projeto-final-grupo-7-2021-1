import pygame
from pygame.constants import *
from views.view import View
from model.player import Player
from model.cenario import Cenario
from controller.highScore import HighScoreDAO
from settings.gameSettings import GameSettings
from settings.gameStates import GameStates


#variaveis auxiliares
vel_jogo = 4
vel_jogo_salvo = vel_jogo
vel_pulo = 5
poder_usado = None
poder_tempo = 0 #registra o tempo que o player colidiu com o poder
pause_tempo = 0 #registra o tempo que a tecla de pause foi pressionada (para evitar bugs)
ultimo_acres_score = 0
ultimo_acres_vel = 0 #a cada 100 pontos a velocidade aumenta em 0.5


class Controller:
    def __init__(self):
        self.__player = Player()
        self.__cenario = Cenario()
        self.__view = View(self)
        self.__hsDAO = HighScoreDAO('highScores.pkl')
        self.__highscore = self.__hsDAO.getHighScore()
        #ponteiros que controlam o jogo
        self.__gameState = GameStates.MENU
        self.__habilitaColisao = True
        self.__mouse_pressed = False

    @property
    def player(self):
        return self.__player

    @property
    def cenario(self):
        return self.__cenario

    @property
    def gameState(self):
        return self.__gameState

    @property
    def highscore(self):
        return self.__highscore

    def mainloop(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(GameSettings.FPS)

            mouse_pos = pygame.mouse.get_pos()
            now = pygame.time.get_ticks() #conta o numero de ticks desde que o programa começou

            self.perform_actions(now, mouse_pos, self.__mouse_pressed)

            self.__mouse_pressed = False

            for event in pygame.event.get():
                if event.type == WINDOWCLOSE:
                    running = False
                elif event.type == MOUSEBUTTONUP:
                    self.__mouse_pressed = True

            pygame.display.update()

    #apenas para criterios de legibilidade
    def perform_actions(self, now, mouse_pos, mouse_up):
        self.key_handler(now)
        if self.__gameState == GameStates.MENU:
            self.__gameState = self.__view.tela_menu(mouse_pos, mouse_up)
        elif self.__gameState == GameStates.INSTRUCOES1:
            self.__gameState = self.__view.tela_instrucoes1(mouse_pos, mouse_up)
        elif self.__gameState == GameStates.INSTRUCOES2:
            self.__gameState = self.__view.tela_instrucoes2(mouse_pos, mouse_up)
        elif self.__gameState == GameStates.INSTRUCOES3:
            self.__gameState = self.__view.tela_instrucoes3(mouse_pos, mouse_up)
        elif self.__gameState == GameStates.RANKING:
            self.__gameState = self.__view.tela_ranking(mouse_pos, mouse_up)
        elif self.__gameState == GameStates.JOGANDO:
            self.checar_pulando()
            self.__cenario.gerar_elementos(now)
            self.__cenario.mover_elementos(vel_jogo)
            self.contador_score(now)
            self.terminar_efeito(now)
            self.update_highscore()
            if self.__habilitaColisao:
                self.checar_colissoes(now)
            self.__view.tela_jogo()
        elif self.__gameState == GameStates.ENDGAME:
            self.__nextState = self.__view.tela_endgame()

    def key_handler(self, now):
        keys = pygame.key.get_pressed()
        self.__keys_player(keys)
        self.__key_escape(keys, now)
        self.__key_return(keys, now)
        
    def __keys_player(self, keys):
        if keys[K_w] or keys[K_UP]:
            if not self.__player.pulando:
                self.__player.pular(vel_pulo)
        if keys[K_s] or keys[K_DOWN]:
            if not self.__player.pulando and not self.__player.agachando:
                self.__player.agachar()
        else:
            if self.__player.agachando:
                self.__player.soltar()
    
    def __key_escape(self, keys, now):
        if keys[K_ESCAPE] and self.__pauseTimer(now):
            if self.__gameState == GameStates.JOGANDO:
                self.__gameState = GameStates.PAUSADO
                self.__view.tela_pause()
            elif self.__gameState == GameStates.PAUSADO:
                self.__gameState = GameStates.JOGANDO

    def __key_return(self, keys, now):
        if self.__gameState == GameStates.ENDGAME and keys[K_RETURN]:
            self.reiniciar(now)

    def __pauseTimer(self,now):
        global pause_tempo
        if now - pause_tempo >= GameSettings.TEMPO_PAUSE:
            pause_tempo = now
            return True

    def checar_pulando(self):
        if self.__player.pulando:
            self.__player.pular(vel_pulo)
    
    #colisões player x obstaculo/poder
    def checar_colissoes(self, now):
        self.__checar_obstaculo_colide()
        self.__checar_poder_colide(now)
    
    # colisão para obstaculos x player    
    def __checar_obstaculo_colide(self):
        for obstaculo in self.__cenario.obstaculos:
            if self.__player.colliderect(obstaculo):
                self.end_game()

    # colisão entre player x poder
    def __checar_poder_colide(self, now):
        global vel_jogo, poder_usado, poder_tempo, vel_pulo
        for poder in self.__cenario.poderes:
            if self.__player.colliderect(poder):
                poder_usado = poder
                poder_tempo = now
                self.__player.cor = poder.cor
                self.__habilitaColisao, vel_jogo, vel_pulo = poder.efeito(vel_jogo, vel_pulo)
                self.__cenario.removePoder(poder)

    #Encerra efeito do poder
    def terminar_efeito(self, now):
        global game_speed, vel_jogo, vel_jogo_salvo, poder_usado, poder_tempo, vel_pulo
        if poder_usado != None:
            if now - poder_tempo >= poder_usado.tempo:
                vel_jogo = vel_jogo_salvo
                poder_usado = None
                poder_tempo = now
                vel_pulo = 4
                self.__habilitaColisao = True
                self.__player.resetarCor()

    def contador_score(self, now):
        global ultimo_acres_score, poder_usado
        if now - ultimo_acres_score > GameSettings.TEMPO_ACRES_SCORE:
            self.__player.score += 1
            ultimo_acres_score = now
            if poder_usado == None:
                #como alguns poderes mexem com a velocidade do jogo
                #não podemos afetar essa velocidade durante o tempo de uso do poder
                self.incrementar_vel()

    def get_score(self):
        return self.__player.score

    def incrementar_vel(self):
        global vel_jogo, vel_jogo_salvo, ultimo_acres_vel
        if self.__player.score - ultimo_acres_vel >= 100:
            ultimo_acres_vel = self.__player.score
            vel_jogo += 0.5
            vel_jogo_salvo = vel_jogo


    def end_game(self):
        self.__gameState = GameStates.ENDGAME
        self.__hsDAO.add(self.__player.score)
        self.__highscore = self.__hsDAO.getHighScore()

    def reiniciar(self, now):
        global vel_jogo, vel_jogo_salvo
        vel_jogo = 4
        vel_jogo_salvo = vel_jogo
        self.__player.resetar()
        self.__cenario.limpar(now)
        self.__gameState = GameStates.JOGANDO

    def update_highscore(self):
        if self.__player.score > self.__highscore:
            self.__highscore = self.__player.score  

    def get_highscores(self):
        return self.__hsDAO.getAllScores()
