from views.menuView import MenuView
from state_logic.state import State
from views.rankingView import RankingView
from views.settingsView import SettingsView
from views.instructionView import InstructionView
from views.avatarView import AvatarView
from views.backgroundView import BackgroundView


class MenuState(State):
    def __init__(self):
        super().__init__(MenuView(), 'menu')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)

class InstructionState(State):
    def __init__(self):
        super().__init__(InstructionView(), 'instrucoes')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)

class SettingsState(State):
    def __init__(self):
        super().__init__(SettingsView(), 'configuracoes')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)

class RankingState(State):
    def __init__(self):
        super().__init__(RankingView(), 'ranking')
    
    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        top_scores = kwargs['top_scores']
        return self.view.display(screen, mouse_up, top_scores)

class SelAvatarState(State):
    def __init__(self):
        super().__init__(AvatarView(), 'sel_avatar')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)

class SelBgState(State):
    def __init__(self):
        super().__init__(BackgroundView(), 'sel_bg')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)