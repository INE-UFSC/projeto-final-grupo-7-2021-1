from pygame import Rect


#Duas classes auxiliares só pra diferenciar o cenário
class Chao(Rect):
    def __init__(self, width, height, chao):
        super().__init__(0, chao, width, height)

class Ceu(Rect):
    def __init__(self, width, heigth):
        super().__init__(0, 0, width, heigth)

class Cenario:
    def __init__(self, width, height, chao):
        self.__screen_width = width
        self.__screen_height = height
        self.__comeco_chao = chao
        self.__ceu = Ceu(self.__screen_width, self.__screen_height)
        self.__chao = Chao(self.__screen_width, self.__screen_height, self.__comeco_chao)
        self.__obstaculos = []
        self.__poderes = []

    @property
    def ceu(self):
        return self.__ceu

    @property
    def chao(self):
        return self.__chao

    @property
    def obstaculos(self):
        return self.__obstaculos

    @property
    def poderes(self):
        return self.__poderes

    def gerarObs(self):
        pass

    def gerarPoder(self):
        pass

    def moverObs(self):
        pass

    def moverPoderes(self):
        pass
