from obstaculos import Obstacle

class Bird(Obstacle):
    def __init__(self, x, y, margin):
        size = 30
        super().__init__(x, y-size, size, size, margin)
        