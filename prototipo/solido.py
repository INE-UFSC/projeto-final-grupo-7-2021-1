from obstaculo import IObstaculo

class Solido(IObstaculo):
  def __init__(self, width, height, cor, margem, velocidade):
      super().__init__(width, height, cor, margem, velocidade)

  def mover(self):
    pass