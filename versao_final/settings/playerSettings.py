import os
from settings.singleton import Singleton


class PlayerSettings(Singleton):
    def __init__(self):
        self.SIZE = 40 #quadrado
        self.JUMP_SCALE = ()
        self.RUN_SCALE = ()
        self.SLIDE_SCALE = ()
        self.DEFAULT_X_POS = 300
        self.DEFAULT_COLOR = (255,0,0)
        self.__path = os.path.join(os.getcwd(), 'assets', 'characters', 'adventurer_boy')
        self.__run_images = os.listdir(os.path.join(self.__path, 'run'))
        self.__jump_images = os.listdir(os.path.join(self.__path, 'jump'))
        self.__slide_images = os.listdir(os.path.join(self.__path, 'slide'))
        self.__dead_images = os.listdir(os.path.join(self.__path, 'dead'))

    @property
    def path(self):
        return self.__path

    @property
    def run_images(self):
        return self.__run_images

    @property
    def jump_images(self):
        return self.__jump_images

    @property
    def slide_images(self):
        return self.__slide_images

    @property
    def dead_images(self):
        return self.__dead_images

    def set_new_avatar(self, new_avatar_path):
        self.__path = new_avatar_path
        self.__run_images = os.listdir(os.path.join(self.__path, 'run'))
        self.__jump_images = os.listdir(os.path.join(self.__path, 'jump'))
        self.__slide_images = os.listdir(os.path.join(self.__path, 'slide'))
        self.__dead_images = os.listdir(os.path.join(self.__path, 'dead'))
