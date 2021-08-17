from prototipo.controller import WIDTH
from obstaculos import Obstacle

class SmallObs(Obstacle):
    def __init__(self, x, y, margin):
        width = 20
        height = 40
        super().__init__(x, y-height, width, height, margin)

class LargeObs(Obstacle):
    def __init__(self, x, y, margin):
        width = 30
        height = 60
        super().__init__(x, y-height, width, height, margin)

