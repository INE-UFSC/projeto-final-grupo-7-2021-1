import pygame
from pygame.constants import *
from model.player import Player
from model.cenario import Cenario
from controller.highScore import HighScoreDAO
from settings.gameSettings import GameSettings
from state_logic.stateMachine import StateMachine


#variaveis auxiliares
vel_jogo = 4
vel_jogo_salvo = vel_jogo
vel_pulo = 5
poder_usado = None
poder_tempo = 0 #registra o tempo que o player colidiu com o poder
pause_tempo = 0 #registra o tempo que a tecla de pause foi pressionada (para evitar bugs)
ultimo_acres_score = 0
ultimo_acres_vel = 0 #a cada 100 pontos a velocidade aumenta em 0.5

GAME_SETTINGS = GameSettings()

class Controller:
    def __init__(self):
        self.__player = Player()
        self.__cenario = Cenario()
        self.__window = pygame.display.set_mode((GAME_SETTINGS.WIDTH, GAME_SETTINGS.HEIGHT))
        self.__state_machine = StateMachine(self)
        self.__hsDAO = HighScoreDAO('highScores.pkl')
        self.__highscore = self.__hsDAO.getHighScore()
        self.__final_score = 0
        #ponteiros que controlam o jogo
        self.__habilitaColisao = True
        self.__mouse_pressed = False
        self.__keydown = False
        self.__colidiu = False

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
            clock.tick(GAME_SETTINGS.FPS)

            now = pygame.time.get_ticks() #conta o numero de ticks desde que o programa começou

            self.__state_machine.run(self.__window, self.__mouse_pressed, self.__keydown, self.__colidiu)
            self.perform_actions(now)

            self.__mouse_pressed = False
            self.__keydown = False
            for event in pygame.event.get():
                if event.type == WINDOWCLOSE:
                    running = False
                elif event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        self.__mouse_pressed = True
                elif event.type == KEYDOWN:
                    self.__keydown = True

            pygame.display.update()

    def perform_actions(self, now):
        if self.__state_machine.currentState == 'jogando':
            self.key_handler()
            self.checar_pulando()
            self.__cenario.gerar_elementos(now)
            self.__cenario.mover_elementos(vel_jogo)
            self.contador_score(now)
            self.terminar_efeito(now)
            self.update_highscore()
            self.__player.animaPlayer(now)

            if self.__habilitaColisao:
                self.checar_colissoes(now)
        elif self.__state_machine.currentState == 'menu':
            self.reiniciar()
        else:
            self.__colidiu = False

    def key_handler(self):
        keys = pygame.key.get_pressed()
        if keys[K_w] or keys[K_UP]:
            if not self.__player.pulando:
                self.__player.pular(vel_pulo)
        if keys[K_s] or keys[K_DOWN]:
            if not self.__player.pulando and not self.__player.agachando:
                self.__player.agachar()
        else:
            if self.__player.agachando:
                self.__player.soltar()

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
            if self.__player.rect.colliderect(obstaculo.rect):
                self.end_game()

    # colisão entre player x poder
    def __checar_poder_colide(self, now):
        global vel_jogo, poder_usado, poder_tempo, vel_pulo
        for poder in self.__cenario.poderes:
            if self.__player.rect.colliderect(poder.rect):
                poder_usado = poder
                poder_tempo = now
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
   
    def contador_score(self, now):
        global ultimo_acres_score, poder_usado
        if now - ultimo_acres_score > GAME_SETTINGS.TEMPO_ACRES_SCORE:
            self.__player.score += 1
            ultimo_acres_score = now
            if poder_usado == None:
                #como alguns poderes mexem com a velocidade do jogo
                #não podemos afetar essa velocidade durante o tempo de uso do poder
                self.incrementar_vel()

    def get_score(self):
        return self.__player.score

    def get_final_score(self):
        return self.__final_score

    def get_highscores(self):
        return self.__hsDAO.getAllScores()

    def incrementar_vel(self):
        global vel_jogo, vel_jogo_salvo, ultimo_acres_vel
        if self.__player.score - ultimo_acres_vel >= 100:
            ultimo_acres_vel = self.__player.score
            vel_jogo += 0.5
            vel_jogo_salvo = vel_jogo

    def end_game(self):
        self.__final_score = self.__player.score
        self.__hsDAO.add(self.__player.score)
        self.__highscore = self.__hsDAO.getHighScore()
        self.__colidiu = True
        self.reiniciar()

    def reiniciar(self):
        global vel_jogo, vel_jogo_salvo
        vel_jogo = 4
        vel_jogo_salvo = vel_jogo
        self.__player.resetar()
        self.__cenario.limpar()

    def update_highscore(self):
        if self.__player.score > self.__highscore:
            self.__highscore = self.__player.score
