from model.obstaculos import Obstaculo


class ObsPequeno(Obstaculo):
    def __init__(self, x, y, margem):
        filename = 'obsPequeno.png'
        scale = (54,76)
        super().__init__(x, y, margem, filename, scale)

class ObsGrande(Obstaculo):
    def __init__(self, x, y, margem):
        filename = 'obsGrande.png'
        scale = (112,84)
        super().__init__(x, y , margem, filename, scale)

