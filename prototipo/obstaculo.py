from abc import ABC, abstractmethod

class IObstaculo(ABC):
   """ Parametros demais """
   def __init__(self,width,height,cor,margem,velocidade):
      self.__width = width
      self.__height = height
      self.__cor = cor
      self.__margem = margem
      self.__velocidade = velocidade

      @abstractmethod
      def mover(self):
         pass