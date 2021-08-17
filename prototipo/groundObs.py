from prototipo.controller import WIDTH
from obstaculos import Obstaculo


class ObsPequeno(Obstaculo):
    def __init__(self, x, y, margem):
        width = 20
        height = 40
        super().__init__(x, y-height, width, height, margem)

class ObsGrande(Obstaculo):
    def __init__(self, x, y, margem):
        width = 30
        height = 60
        super().__init__(x, y-height, width, height, margem)

