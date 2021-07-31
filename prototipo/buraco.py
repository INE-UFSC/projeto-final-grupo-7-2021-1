from obstaculo import IObstaculo

class Buraco(IObstaculo):
  def __init__(self, width, height, cor, margem, velocidade,preenchimento):
      super().__init__(width, height, cor, margem, velocidade)
      self.__preenchimento = preenchimento
  
  def move(self):
    """ movimentação velocidade do buraco """
    pass