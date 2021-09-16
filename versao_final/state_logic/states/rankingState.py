from state_logic.states.state import State
from views.rankingView import RankingView


class RankingState(State):
    def __init__(self):
        super().__init__(RankingView(), 'ranking')
    
    def perform_actions(self, screen, **kwargs):
        mouse_up = kwargs['mouse_up']
        top_scores = kwargs['top_scores']
        return self.view.display(screen, mouse_up, top_scores)
