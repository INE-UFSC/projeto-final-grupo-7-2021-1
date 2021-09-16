import os
from settings.singleton import Singleton


class PlayerSettings(Singleton):
    def __init__(self):
        self.ANIMACAOTEMPO = 100
        self.JUMP_SCALE = (122,160)
        self.RUN_SCALE = (124,152)
        self.SLIDE_SCALE = (118,116)
        self.DEFAULT_X_POS = 200
        self.__path = os.path.join(os.getcwd(), 'assets', 'characters', 'adventurer_boy')
        self.__run_images = sorted(os.listdir(os.path.join(self.__path, 'run')))
        self.__jump_images = sorted(os.listdir(os.path.join(self.__path, 'jump')))
        self.__slide_images = sorted(os.listdir(os.path.join(self.__path, 'slide')))
        self.__dead_images = sorted(os.listdir(os.path.join(self.__path, 'dead')))

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
        self.__run_images = sorted(os.listdir(os.path.join(self.__path, 'run')))
        self.__jump_images = sorted(os.listdir(os.path.join(self.__path, 'jump')))
        self.__slide_images = sorted(os.listdir(os.path.join(self.__path, 'slide')))
        self.__dead_images = sorted(os.listdir(os.path.join(self.__path, 'dead')))
