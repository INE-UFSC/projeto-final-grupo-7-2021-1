from obstaculo import IObstaculo

class Inimigo(IObstaculo):
  def __init__(self, width, height, cor, margem, velocidade, poderAttack):
      super().__init__(width, height, cor, margem, velocidade)
      self.__poderAttack = poderAttack
    
  def atacar(self):
    pass

  def mover(self):
    pass