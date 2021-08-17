from abc import ABC, abstractmethod
from pygame import Rect

#Configurações
TAMANHO = 10
ROXO = (155,0,155)
BRANCO = (255,255,255)

#Class abstrata de poderes

class Poder(Rect, ABC):
    @abstractmethod
    def __init__(self, x, y, cor, recarga):
        self.__cor = cor
        self.__recarga = recarga
        super().__init__(x, y- TAMANHO, TAMANHO, TAMANHO)
    
    @property
    def cor(self):
        return self.__cor
    
    # Tempo recarga
    @property
    def recarga(self):
        return self.__recarga
    # Atualiza o Rect 
    def __atualizar(self):
        self.atualizar(self.x, self.y, self.width, self.height)

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
        super().__init__(x, y, BRANCO, 2000)
    
    def efeito(self, velocidadeJogo, velocidadePulo):
        return False, velocidadeJogo + 20 , velocidadePulo


