import pygame
from pygame.constants import *
from pygame.mixer import pause
from view import View
from player import Player
from cenario import Cenario
from highScore import HighScoreDAO


#configs
WIDTH = 900
HEIGHT = 500
FPS = 60
COMECO_CHAO = 380
PULO_MAX = COMECO_CHAO - 120 #pulo de 120 px
TEMPO_PAUSE = 500 #esc deve ficar pressionado por 500 ms para entrar na tela de pause
TEMPO_ACRES_SCORE = 100 #a cada 100 ms o score aumenta 1

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
        self.__player = Player(COMECO_CHAO)
        self.__cenario = Cenario(WIDTH, HEIGHT, COMECO_CHAO)
        self.__view = View(self, WIDTH, HEIGHT)
        self.__hsDAO = HighScoreDAO('highScores.pkl')
        self.__highScore = self.__hsDAO.getHighScore()
        #ponteiros que controlam o jogo
        self.__running = True
        self.__pausado = False
        self.__endGame = False
        self.__habilitaColisao = True

    @property
    def player(self):
        return self.__player

    @property
    def cenario(self):
        return self.__cenario

    @property
    def pausado(self):
        return self.__pausado
    @property
    def highScore(self):
        return self.__highScore

    def mainloop(self):
        clock = pygame.time.Clock()
        while self.__running:
            clock.tick(FPS)

            now = pygame.time.get_ticks() #conta o numero de ticks desde que o programa começou

            self.__view.desenhar()
            self.perform_actions(now)

            for event in pygame.event.get():
                if event.type == WINDOWCLOSE:
                    self.__running = False

            pygame.display.update()

    #apenas para criterios de legibilidade
    def perform_actions(self, now):
        self.key_handler(now)
        if not self.__pausado:
            self.updateHighScore()
            self.checar_pulando()
            self.__cenario.gerar_elementos(now)
            self.__cenario.mover_elementos(vel_jogo)
            self.contador_score(now)
            self.terminar_efeito(now)
            if self.__habilitaColisao:
                self.checar_colissoes(now)

    def key_handler(self, now):
        keys = pygame.key.get_pressed()
        self.__keys_player(keys)
        self.__key_escape(keys, now)
        self.__key_return(keys, now)
        
    def __keys_player(self, keys):
        if keys[K_w] or keys[K_UP]:
            if not self.__player.pulando:
                self.__player.pular(vel_pulo, PULO_MAX, COMECO_CHAO)
        if keys[K_s] or keys[K_DOWN]:
            if not self.__player.pulando and not self.__player.agachando:
                self.__player.agachar()
        else:
            if self.__player.agachando:
                self.__player.soltar()
    
    def __key_escape(self, keys, now):
        if keys[K_ESCAPE] and self.__pauseTimer(now):
            if not self.__pausado:
                self.__pausado = True
                self.__view.tela_pause()
            else:
                self.__pausado = False

    def __key_return(self, keys, now):
        if self.__endGame and keys[K_RETURN]:
            self.reiniciar(now)

    def __pauseTimer(self,now):
        global pause_tempo
        if not self.__endGame:
            if now - pause_tempo >= TEMPO_PAUSE:
                pause_tempo = now
                return True

    def checar_pulando(self):
        if self.__player.pulando:
            self.__player.pular(vel_pulo, PULO_MAX, COMECO_CHAO)
    
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
        if now - ultimo_acres_score > TEMPO_ACRES_SCORE:
            self.__player.score += 1
            ultimo_acres_score = now
            if poder_usado != None: 
                #como alguns poderes mexem com a velocidade do jogo
                #não podemos afetar essa velocidade durante o tempo de uso do poder
                self.incrementar_vel(self.__player.score)

    def get_score(self):
        return self.__player.score

    def incrementar_vel(self, score):
        global vel_jogo, vel_jogo_salvo, ultimo_acres_vel
        if score - ultimo_acres_vel == 100:
            ultimo_acres_vel = score
            vel_jogo += 0.5
            vel_jogo_salvo = vel_jogo

    def end_game(self):
        self.__pausado = True
        self.__endGame = True
        self.__hsDAO.add(self.__player.score)
        self.__highScore = self.__hsDAO.getHighScore()
        pygame.time.wait(500)
        self.__view.tela_endgame()

    def reiniciar(self, now):
        global vel_jogo, vel_jogo_salvo
        vel_jogo = 4
        vel_jogo_salvo = vel_jogo
        self.__pausado = False
        self.__endGame = False
        self.__player.resetar(COMECO_CHAO)
        self.__cenario.limpar(now)

    def updateHighScore(self):
        print(self.__player.score, self.__highScore, self.__hsDAO.getHighScore())
        if self.__player.score > self.__highScore:
            self.__highscore = self.__player.score        

