from model.obstaculos import Obstaculo


class Passaro(Obstaculo):
    def __init__(self, x, y, margem):
        filename = 'bird.png'
        scale = (76, 76)
        super().__init__(x, y, margem, filename, scale)
