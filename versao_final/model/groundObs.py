from model.obstaculos import Obstaculo


class ObsPequeno(Obstaculo):
    def __init__(self, x, y, margem):
        filename = 'obsPequeno.png'
        scale = (72, 72)
        super().__init__(x, y, margem, filename, scale)

class ObsGrande(Obstaculo):
    def __init__(self, x, y, margem):
        filename = 'obsGrande.png'
        scale = (102,102)
        super().__init__(x, y, margem, filename, scale)
