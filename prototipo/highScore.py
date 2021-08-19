import pickle


class HighScoreDAO:
    def __init__(self, datasource="default.pkl"):
        self.__cache = []
        self.__datasource = datasource
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()
            self.__initialize_file()

    @property
    def cache(self):
        return self.__cache

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, "wb"))

    def __initialize_file(self):
        self.__cache = [0,0,0,0,0]
        self.__dump()
    
    def add(self,highScore):
        x = highScore
        for index, value in enumerate(self.__cache):
            if x > value:
                self.__cache[index] = x
                x = value
        
        self.__dump()
    
    def getHighScore(self):
        return self.__cache[0]
    
    def getAllScores(self):
        return self.__cache