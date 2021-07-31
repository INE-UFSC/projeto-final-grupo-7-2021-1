class Cenario:
  def __init__(self):
    self.__obstaculos = []
    self.__buracos = []
    self.__poderes = []
    self.__inimigos = []

""" precisa mesmo de todas essas variáveis?
      talvez pudessemos colocar tudo em obstaculos msm.
      vai ter repetição de código..
     """
  def incluir_obstaculo(self,obstaculo):
    if isinstance(obstaculo,Buraco):
      self.__buracos.append(obstaculo)
    elif isinstance(obstaculo,Inimigo):
      self.__inimigos.append(obstaculo)
    else:
      self.__obstaculos.append(obstaculo)
  
  def remover_obstaculo(self,obstaculo):
    if isinstance(obstaculo,Buraco):
      self.__buracos.remove(obstaculo)
    elif isinstance(obstaculo,Inimigo):
      self.__inimigos.remove(obstaculo)
    else:
      self.__obstaculos.remove(obstaculo)
    
  def incluir_poderes(self,poder):
    self.__poderes.append(poder)

  def remover_poder(self,poder):
    self.__poderes.append(poder)