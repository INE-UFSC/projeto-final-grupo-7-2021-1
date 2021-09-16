from state_logic.states.state import State
from views.endgameView import EndgameView


class EndgameState(State):
    def __init__(self):
        super().__init__(EndgameView(), 'endgame')

    def perform_actions(self, screen, **kwargs):
        final_score = kwargs['final_score']
        mouse_up = kwargs['mouse_up']
        return self.view.display(screen, final_score, mouse_up)