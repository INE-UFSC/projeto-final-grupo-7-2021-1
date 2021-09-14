from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, view, nome):
        self.__view = view
        self.__nome = nome
    
    @property
    def view(self):
        return self.__view

    @property
    def nome(self):
        return self.__nome

    @abstractmethod
    def perform_actions(self, screen):
        raise NotImplementedError