import pygame
from pygame.constants import *
from view import View
from player import Player
from cenario import Cenario


#configs
WIDTH = 900
HEIGHT = 500
FPS = 60
COMECO_CHAO = 380
PULO_MAX = COMECO_CHAO - 120 #pulo de 120 px

#variaveis auxiliares
vel_jogo = 4
vel_jogo_salvo = 4
vel_pulo = 5
vel_pulo_salvo = 5
poder_usado = None
poder_tempo = 0


class Controller:
    def __init__(self):
        self.__player = Player(COMECO_CHAO)
        self.__cenario = Cenario(WIDTH, HEIGHT, COMECO_CHAO)
        self.__view = View(self, WIDTH, HEIGHT)
        self.__running = True
        self.__paused = False
        self.__habilitaColisao = True

    @property
    def player(self):
        return self.__player

    @property
    def cenario(self):
        return self.__cenario

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
        self.key_handler()
        self.checar_pulando()
        self.__cenario.gerar_elementos(now)
        self.__cenario.mover_elementos(vel_jogo)
        self.checar_colissoes(now)
        self.terminar_efeito(now)

    def key_handler(self):
        keys = pygame.key.get_pressed()
        if keys[K_w] or keys[K_UP]:
            if not self.__player.pulando:
                self.__player.pular(vel_pulo, PULO_MAX, COMECO_CHAO)
        if keys[K_s] or keys[K_DOWN]:
            if not self.__player.pulando and not self.__player.agachando:
                self.__player.agachar()
        else:
            if self.__player.agachando:
                self.__player.soltar()

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
                print('colidiu')

    # colisão entre player x poder
    def __checar_poder_colide(self, now):
        global vel_jogo, poder_usado, poder_tempo, vel_pulo
        for poder in self.__cenario.poderes:
            if self.__player.colliderect(poder):
                self.__player.cor = poder.cor
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
                self.__player.resetarCor()

    



