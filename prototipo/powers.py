from abc import ABC, abstractmethod
from pygame import Rect

#Configurações
TAMANHO = 10
ROXO = (155,0,155)
BRANCO = (255,255,255)

#Class abstrata de poderes

class Poder(Rect, ABC):
    @abstractmethod
    def __init__(self, x, y, cor, tempo):
        self.__cor = cor
        self.__tempo = tempo
        super().__init__(x, y-TAMANHO, TAMANHO, TAMANHO)
    
    @property
    def cor(self):
        return self.__cor
    
    # Tempo que o poder permanece ativado
    @property
    def tempo(self):
        return self.__tempo

    def mover(self, vel):
        self.x -= vel + 2
        self.__atualizar()

    # Atualiza o Rect 
    def __atualizar(self):
        self.update(self.x, self.y, self.width, self.height)

    #Efeito gerado pelo poder
    @abstractmethod
    def efeito(self, game_speed, jump_speed):
        #error caso não seja implementado
        raise NotImplementedError

class PoderLento(Poder):
    def __init__(self, x, y):
        super().__init__(x, y, ROXO, 5000)
    
    def efeito(self, velocidadeJogo, velocidadePulo):
        return True, 2, 2 


class PoderInvulnerabilidade(Poder):
    def __init__(self, x, y):
        super().__init__(x, y, BRANCO, 4000)
    
    def efeito(self, velocidadeJogo, velocidadePulo):
        return False, velocidadeJogo + 20 , velocidadePulo


