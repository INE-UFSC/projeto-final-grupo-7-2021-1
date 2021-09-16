from state_logic.states.state import State
from views.settingsView import SettingsView


class SettingsState(State):
    def __init__(self):
        super().__init__(SettingsView(), 'configuracoes')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)
