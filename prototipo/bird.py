from obstaculos import Obstaculo


TAMANHO = 30

class Passaro(Obstaculo):
    def __init__(self, x, y, margem):
        super().__init__(x, y-TAMANHO, TAMANHO, TAMANHO, margem)
        