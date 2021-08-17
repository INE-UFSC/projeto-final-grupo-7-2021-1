from obstaculos import Obstaculo

class Passaro(Obstaculo):
    def __init__(self, x, y, margem):
        TAMANHO = 30
        super().__init__(x, y-TAMANHO, TAMANHO, TAMANHO, margem)
        