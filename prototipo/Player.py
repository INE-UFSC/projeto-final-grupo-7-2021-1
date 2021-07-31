class Player:
  def __init__(self,highscore,poder1,poder2,poder3):
    self.__score = 0
    """ De onde vai vim esse highscore?? """
    self.__highscore = highscore
    self.__pulando = False
    self.__poderes = [poder1,poder2,poder3]
    """ Diagrama mostra usando poder como string, acho melhor usar boolean """
    self.__usando_poder = False
    """ se cooldown for o tempo que o poder fica ativo, talvez seja necessário outra variável para um tempo de recarga do poder...  """
    self.__cooldown = 15

  def pular(self):
    pass

  def agachar(self):
    pass

  def usar_poder(self):
    pass