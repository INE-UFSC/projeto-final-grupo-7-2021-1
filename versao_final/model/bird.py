from model.obstaculos import Obstaculo


TAMANHO = 30

class Passaro(Obstaculo):
    def __init__(self, x, y, margem):
        filename = 'obsPequeno.png'
        scale = (54,76)
        super().__init__(x, y , margem, filename, scale)
        