from state_logic.states.state import State
from views.menuView import MenuView
from settings.soundSettings import SoundSettings

SOUND_SETTINGS = SoundSettings()

class MenuState(State):
    def __init__(self):
        super().__init__(MenuView(), 'menu')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)
