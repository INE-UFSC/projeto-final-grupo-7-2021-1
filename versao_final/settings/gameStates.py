from enum import Enum, auto

class GameStates(Enum):
    MENU = auto()
    JOGANDO = auto()
    PAUSADO = auto()
    ENDGAME = auto()
    INSTRUCOES1 = auto()
    INSTRUCOES2 = auto()
    INSTRUCOES3 = auto()
    CONFIGURACOES = auto()
    SEL_AVATAR = auto()
    SEL_BG = auto()
    RANKING = auto()
