from state_logic.states.state import State
from views.backgroundView import BackgroundView


class SelBgState(State):
    def __init__(self):
        super().__init__(BackgroundView(), 'sel_bg')

    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, mouse_up)